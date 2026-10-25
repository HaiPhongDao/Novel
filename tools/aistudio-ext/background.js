// Hỏi aistudio_run.py có việc không (long-poll), làm việc trong một tab AI Studio riêng, gửi kết quả về.
// Service worker tắt sau ~30s rảnh: alarm đánh thức mỗi 30s, và mỗi vòng gọi một API extension để giữ nó sống.
// Nhiều cổng: mỗi cổng một vòng riêng và một tab riêng, nên chạy được nhiều aistudio_run.py cùng lúc
// (--port 8765 / 8766 / 8767).
const SERVERS = ['http://127.0.0.1:8765', 'http://127.0.0.1:8766', 'http://127.0.0.1:8767'];
const sleep = ms => new Promise(r => setTimeout(r, ms));

chrome.alarms.create('poll', { periodInMinutes: 0.5 });


const loops = new Set();
const kick = () => { SERVERS.forEach(loop); };
chrome.alarms.onAlarm.addListener(kick);
chrome.runtime.onStartup.addListener(kick);
chrome.runtime.onInstalled.addListener(kick);
kick();

async function loop(SERVER) {
  if (loops.has(SERVER)) return;   // mỗi cổng một vòng riêng, không chặn nhau
  loops.add(SERVER);
  try {
    for (;;) {
      await chrome.runtime.getPlatformInfo();  // giữ service worker sống
      let r;
      try { r = await fetch(`${SERVER}/job?wait=20`); } catch { return; }  // script chưa chạy
      const job = r.status === 200 ? await r.json() : null;
      if (await codeChanged(r.headers.get('X-Ext-Hash'))) {
        if (job) await post(SERVER, '/release', { id: job.id });  // trả việc lại, bản mới nạp xong sẽ nhận
        return chrome.runtime.reload();
      }
      if (job) await runJob(SERVER, job);
      else if (r.status !== 204) return;
    }
  } finally {
    loops.delete(SERVER);
  }
}

// Script gửi kèm hash các file extension trên đĩa; khác hash lúc nạp thì tự reload (storage.session mất khi reload).
async function codeChanged(hash) {
  if (!hash) return false;
  const { loadedHash } = await chrome.storage.session.get('loadedHash');
  if (!loadedHash) {
    await chrome.storage.session.set('loadedHash', hash);
    return false;
  }
  return loadedHash !== hash;
}

// Script còn chờ việc này không (bị Ctrl-C / hết giờ thì thôi).
const alive = (SERVER, id) => fetch(`${SERVER}/alive?id=${id}`).then(r => r.ok, () => false);

const post = (SERVER, path, body) => fetch(SERVER + path, {
  method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body),
}).catch(() => {});

async function runJob(SERVER, job) {
  const log = msg => post(SERVER, '/log', { id: job.id, msg });
  try {
    const tabId = await openTab(SERVER, job.url);
    const info = await call(tabId, 'prepare', job);
    log(`mở ${info.url} | ${info.account}`);
    await call(tabId, 'send', job);
    // Xong khi request GenerateContent đã kết thúc và chữ đứng yên qua hai lần kiểm (hoặc có lỗi).
    // Dự phòng: chữ đứng yên 30s cũng coi là xong; 60s chưa có request nào thì thôi, để collect báo lỗi.
    const deadline = Date.now() + job.timeoutMin * 60000;
    const sent = Date.now();
    let lastLen = -1, stillSince = Date.now();
    for (;;) {
      await sleep(3000);
      if (!(await alive(SERVER, job.id))) throw new Error('script đã dừng, bỏ việc');
      const s = await call(tabId, 'status');
      if (s.textLen !== lastLen) stillSince = Date.now();
      if (s.textLen > 0 && Date.now() - stillSince > 30000) break;
      if (!s.running) {
        if (s.err || (s.started && s.textLen > 0 && s.textLen === lastLen)) break;
        if (!s.started && Date.now() - sent > 60000) break;
      }
      lastLen = s.textLen;
      if (Date.now() > deadline) throw new Error(`quá ${job.timeoutMin} phút chưa xong`);
    }
    const out = await call(tabId, 'collect');
    await post(SERVER, '/result', { id: job.id, ok: true, account: info.account, ...out });
  } catch (e) {
    await post(SERVER, '/result', { id: job.id, ok: false, kind: e.kind || 'error', error: String(e.message || e) });
  } finally {
    await closeTab(SERVER);
  }
}

// Xong việc thì gỡ debugger và đóng tab làm việc; chat đã tự lưu trên AI Studio, lần sau mở lại theo URL.
async function closeTab(SERVER) {
  const key = `tabId:${SERVER}`;
  const { [key]: tabId } = await chrome.storage.local.get(key);
  if (!tabId) return;
  await chrome.debugger.detach({ tabId }).catch(() => {});
  await chrome.tabs.remove(tabId).catch(() => {});
  await chrome.storage.local.remove(key);
}

// Một tab riêng cho việc này (mở nền, không chiếm tab đang dùng), đóng khi xong việc.
async function openTab(SERVER, url) {
  const key = `tabId:${SERVER}`;
  let { [key]: tabId } = await chrome.storage.local.get(key);  // storage.local: còn nhớ sau khi extension reload
  const old = tabId && await chrome.tabs.get(tabId).catch(() => null);
  if (old) await chrome.tabs.update(tabId, { url });
  else {
    tabId = (await chrome.tabs.create({ url, active: false })).id;
    await chrome.storage.local.set({ [key]: tabId });
  }
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
