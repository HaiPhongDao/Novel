// Hỏi aistudio_run.py có việc không (long-poll), làm việc trong một tab AI Studio riêng, gửi kết quả về.
// Service worker tắt sau ~30s rảnh: alarm đánh thức mỗi 30s, và mỗi vòng gọi một API extension để giữ nó sống.
const SERVER = 'http://127.0.0.1:8765';
const sleep = ms => new Promise(r => setTimeout(r, ms));

chrome.alarms.create('poll', { periodInMinutes: 0.5 });
chrome.alarms.onAlarm.addListener(loop);
chrome.runtime.onStartup.addListener(loop);
chrome.runtime.onInstalled.addListener(loop);

// Nhiều việc chạy cùng lúc, mỗi việc một tab (aistudio_run.py --batch giao mỗi tài khoản một việc).
const MAX_JOBS = 4;
const running = new Set();

let looping = false;
async function loop() {
  if (looping) return;
  looping = true;
  try {
    if (!running.size) await closeTabs();  // tab sót lại từ lần service worker chết giữa chừng
    for (;;) {
      await chrome.runtime.getPlatformInfo();  // giữ service worker sống
      if (running.size >= MAX_JOBS) { await sleep(3000); continue; }
      let r;
      try { r = await fetch(`${SERVER}/job?wait=20`); } catch {  // script chưa chạy (hoặc đã xong)
        if (!running.size) return;
        await sleep(3000);
        continue;
      }
      const job = r.status === 200 ? await r.json() : null;
      if (await codeChanged(r.headers.get('X-Ext-Hash'))) {
        if (job) await post('/release', { id: job.id });  // trả việc lại, bản mới nạp xong sẽ nhận
        if (!running.size) return chrome.runtime.reload();
        await sleep(3000);  // chờ các việc đang chạy xong rồi mới nạp lại
        continue;
      }
      if (job) {
        post('/log', { id: job.id, msg: `extension nhận việc, đang chạy ${running.size + 1} việc` });
        running.add(job.id);
        runJob(job).finally(() => running.delete(job.id));
      } else if (r.status !== 204 && !running.size) return;
    }
  } finally {
    looping = false;
  }
}

// Script gửi kèm hash các file extension trên đĩa; khác hash lúc nạp thì tự reload (storage.session mất khi reload).
async function codeChanged(hash) {
  if (!hash) return false;
  const { loadedHash } = await chrome.storage.session.get('loadedHash');
  if (!loadedHash) {
    await chrome.storage.session.set({ loadedHash: hash });
    return false;
  }
  return loadedHash !== hash;
}

// Script còn chờ việc này không (bị Ctrl-C / hết giờ thì thôi).
const alive = id => fetch(`${SERVER}/alive?id=${id}`).then(r => r.ok, () => false);

const post = (path, body) => fetch(SERVER + path, {
  method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body),
}).catch(() => {});

async function runJob(job) {
  const log = msg => post('/log', { id: job.id, msg });
  let tabId;
  try {
    tabId = await openTab(job.id, job.url);
    const info = await call(tabId, 'prepare', job);
    log(`mở ${info.url} | ${info.account}`);
    await call(tabId, 'send', job);
    // Xong khi request GenerateContent đã kết thúc và chữ đứng yên qua hai lần kiểm (hoặc có lỗi).
    // Dự phòng: chữ đứng yên 30s cũng coi là xong; 60s chưa có request nào thì thôi, để collect báo lỗi.
    const deadline = Date.now() + job.timeoutMin * 60000;
    const sent = Date.now();
    // Request đã xong mà 20s không có chữ (lỗi in trong lượt Model, kiểu chưa gặp) cũng coi là xong để collect báo lỗi.
    let lastLen = -1, stillSince = Date.now(), emptySince = 0;
    for (;;) {
      await sleep(3000);
      if (!(await alive(job.id))) throw new Error('script đã dừng, bỏ việc');
      const s = await call(tabId, 'status');
      if (s.textLen !== lastLen) stillSince = Date.now();
      if (s.textLen > 0 && Date.now() - stillSince > 30000) break;
      if (!s.running) {
        if (s.err || (s.started && s.textLen > 0 && s.textLen === lastLen)) break;
        if (!s.started && Date.now() - sent > 60000) break;
        if (s.started && s.textLen === 0) {
          emptySince ||= Date.now();
          if (Date.now() - emptySince > 20000) break;
        } else emptySince = 0;
      } else emptySince = 0;
      lastLen = s.textLen;
      if (Date.now() > deadline) throw new Error(`quá ${job.timeoutMin} phút chưa xong`);
    }
    const out = await call(tabId, 'collect');
    await post('/result', { id: job.id, ok: true, account: info.account, ...out });
  } catch (e) {
    await post('/result', { id: job.id, ok: false, kind: e.kind || 'error', error: String(e.message || e) });
  } finally {
    await closeTab(job.id);
  }
}

// Tab của từng việc ghi trong storage.local (còn nhớ sau khi extension reload): { jobId: tabId }.
const getTabs = async () => (await chrome.storage.local.get('tabs')).tabs || {};
let tabsLock = Promise.resolve();
const editTabs = fn => (tabsLock = tabsLock.then(async () => {
  const tabs = await getTabs();
  fn(tabs);
  await chrome.storage.local.set({ tabs });
}));

async function removeTab(tabId) {
  await chrome.debugger.detach({ tabId }).catch(() => {});
  await chrome.tabs.remove(tabId).catch(() => {});
}

// Xong việc thì gỡ debugger và đóng tab làm việc; chat đã tự lưu trên AI Studio, lần sau mở lại theo URL.
async function closeTab(jobId) {
  const tabId = (await getTabs())[jobId];
  if (tabId) await removeTab(tabId);
  await editTabs(t => delete t[jobId]);
}

async function closeTabs() {
  for (const tabId of Object.values(await getTabs())) await removeTab(tabId);
  await chrome.storage.local.remove(['tabs', 'tabId']);
}

// Một tab riêng cho việc này (mở nền, không chiếm tab đang dùng), đóng khi xong việc.
async function openTab(jobId, url) {
  const tabId = (await chrome.tabs.create({ url, active: false })).id;
  await editTabs(t => { t[jobId] = tabId; });
  await sleep(1000);
  const end = Date.now() + 60000;
  for (;;) {
    const tab = await chrome.tabs.get(tabId);
    if (tab.status === 'complete') {
      if (!tab.url.startsWith('https://aistudio.google.com/')) throw new Error(`chưa đăng nhập: ${url} → ${tab.url}`);
      await keepAwake(tabId);
      return tabId;
    }
    if (Date.now() > end) throw new Error(`tab không tải xong: ${url}`);
    await sleep(500);
  }
}

// Tab ẩn (chạy nền, Edge bị che, máy khoá) thì AI Studio huỷ GenerateContent: gắn debugger và giả lập
// tab đang được dùng. Edge hiện thanh "đang được gỡ lỗi" trong lúc chạy.
async function keepAwake(tabId) {
  const target = { tabId };
  await chrome.debugger.attach(target, '1.3').catch(e => {
    if (!/already attached/i.test(e.message)) throw e;
  });
  await chrome.debugger.sendCommand(target, 'Emulation.setFocusEmulationEnabled', { enabled: true });
  await chrome.debugger.sendCommand(target, 'Page.setWebLifecycleState', { state: 'active' }).catch(() => {});
}

// Chạy một bước của page.js trong trang (world MAIN để bắt được nút "Copy as markdown").
async function call(tabId, name, arg) {
  await chrome.scripting.executeScript({ target: { tabId }, world: 'MAIN', files: ['page.js'] });
  const [res] = await chrome.scripting.executeScript({
    target: { tabId }, world: 'MAIN', args: [name, arg ?? null],
    func: (n, a) => window.__novel[n](a),
  });
  const v = res?.result;
  if (!v) throw new Error(`bước ${name} không trả kết quả`);
  if (v.error) throw Object.assign(new Error(v.error), { kind: v.kind || 'error' });
  return v;
}
