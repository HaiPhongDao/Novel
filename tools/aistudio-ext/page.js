// Các bước trong trang AI Studio; background.js gọi window.__novel.<bước>(job). Lỗi trả về {error, kind}.
(() => {
  const QUOTA = /quota|rate.?limit|resource.?exhausted|\b429\b|reached .{0,30}limit|try again later/i;
  const PROMPT = 'textarea[aria-label="Enter a prompt"]';
  const RUN = 'ms-run-button button';
  const $ = s => document.querySelector(s);
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const visible = el => el.getClientRects().length > 0;
  const hasId = (el, id) => new RegExp(`(^|\\s)${id.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}(\\s|$)`).test(el.innerText);
  const running = () => /Stop/.test($(RUN)?.innerText || '');

  async function waitFor(fn, ms, what) {
    const end = Date.now() + ms;
    while (Date.now() < end) {
      const v = fn();
      if (v) return v;
      await sleep(250);
    }
    throw new Error(`không thấy ${what}`);
  }

  // Gán value kiểu Angular nhận được (setter gốc + sự kiện input).
  function setText(el, v) {
    Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', { bubbles: true }));
    el.dispatchEvent(new Event('change', { bubbles: true }));
  }

  function pageError() {
    for (const s of ['mat-snack-bar-container', '.mat-mdc-snack-bar-container', 'ms-callout', '.error'])
      for (const el of document.querySelectorAll(s)) {
        const t = visible(el) && el.innerText.trim();
        if (t) return t;
      }
    return '';
  }

  function closePanel() {
    $('[aria-label="Close panel"]')?.click();
    $('.cdk-overlay-backdrop')?.click();
  }

  // Bảng Run settings (model, thinking, SI) có thể đang đóng, nhất là ở tab hẹp/chạy nền.
  async function openRunSettings() {
    if ($('button.model-selector-card')) return;
    const label = b => b.getAttribute('aria-label') || '';
    const btns = [...document.querySelectorAll('button')];
    btns.find(b => /run settings/i.test(label(b)) && !/close/i.test(label(b)))?.click();
    try {
      await waitFor(() => $('button.model-selector-card'), 5000, 'bảng Run settings');
    } catch {
      throw new Error(`không mở được bảng Run settings; nút có: ${btns.map(label).filter(Boolean).join(', ')}`);
    }
  }

  async function setModel(model) {
    if (hasId($('button.model-selector-card'), model)) return;
    $('button.model-selector-card').click();
    const find = () => [...document.querySelectorAll('ms-model-carousel-row')].find(r => hasId(r, model));
    await waitFor(() => $('ms-model-carousel-row'), 10000, 'danh sách model');
    if (!find()) {  // mặc định chỉ hiện "Featured"; model cũ hơn nằm trong "All"
      [...document.querySelectorAll('button, [role=tab]')].find(b => b.innerText.trim() === 'All')?.click();
    }
    const row = await waitFor(find, 10000, `model ${model}`);
    row.querySelector('button.content-button').click();
    await sleep(1000);
    if ($('ms-model-carousel-row')) closePanel();
    await sleep(300);
    await openRunSettings();  // ở tab hẹp, "Close panel" có thể đóng luôn bảng Run settings
    if (!hasId($('button.model-selector-card'), model)) throw new Error(`không chọn được model ${model}`);
  }

  async function setThinking(level) {
    await openRunSettings();
    const sel = $('mat-select[aria-label="Thinking Level"]');
    if (!sel || sel.innerText.trim() === level) return;
    sel.click();
    const opt = await waitFor(() => [...document.querySelectorAll('mat-option')].find(o => o.innerText.trim() === level),
      5000, `mục thinking ${level}`);
    opt.click();
    await sleep(400);
    if (sel.innerText.trim() !== level) throw new Error(`không đặt được thinking ${level}`);
  }

  async function setSi(si) {
    await openRunSettings();
    $('button.system-instructions-card').click();
    const box = await waitFor(() => $('textarea[aria-label="System instructions"]'), 10000, 'ô System instructions');
    setText(box, si);
    await sleep(300);
    if (box.value.length !== si.length) throw new Error('SI dán không đủ');
    closePanel();
    await sleep(300);
    await openRunSettings();
  }

  // Bản markdown qua nút "Copy as markdown", chặn writeText để không đụng clipboard của máy.
  let mdError = '';
  async function copyMarkdown(turn) {
    let got = null;
    navigator.clipboard.writeText = t => { got = t; return Promise.resolve(); };
    navigator.clipboard.write = async items => {
      for (const it of items) if (it.types.includes('text/plain')) got = await (await it.getType('text/plain')).text();
    };
    const exec = document.execCommand;
    document.execCommand = function (cmd, ...rest) {
      if (String(cmd).toLowerCase() !== 'copy') return exec.call(this, cmd, ...rest);
      const a = document.activeElement;
      got = a && 'value' in a ? a.value : String(getSelection());
      return true;
    };
    try {
      turn.querySelector('ms-chat-turn-options button').click();
      const item = await waitFor(() => [...document.querySelectorAll('[role=menuitem]')]
        .find(b => /Copy as markdown/.test(b.innerText)), 3000, 'Copy as markdown');
      item.click();
      await waitFor(() => got !== null, 3000, 'markdown');
      return got.trim();
    } catch (e) {
      mdError = e.message;
      closePanel();
      return '';
    } finally {
      delete navigator.clipboard.writeText;
      delete navigator.clipboard.write;
      document.execCommand = exec;
    }
  }

  // Chữ của các lượt Model sau lượt User cuối, bỏ phần suy nghĩ.
  function lastReply() {
    const turns = [...document.querySelectorAll('ms-chat-turn')];
    const role = t => t.querySelector('[data-turn-role]')?.getAttribute('data-turn-role');
    let i = turns.length - 1;
    while (i >= 0 && role(turns[i]) !== 'User') i--;
    const models = turns.slice(i + 1).filter(t => role(t) === 'Model');
    const text = models.map(t => [...t.querySelectorAll('ms-text-chunk')]
      .filter(c => !c.closest('ms-thought-chunk'))
      .map(c => c.innerText.trim()).join('\n\n')).join('\n\n').trim();
    return { models, text };
  }

  // Đếm request GenerateContent đang chạy: ở tab nền nút Stop không cập nhật, nên đây mới là dấu hiệu "đang viết".
  function hookGenerate() {
    if (window.__novelGen) return;
    const gen = window.__novelGen = { started: 0, active: new Set() };
    const open = XMLHttpRequest.prototype.open;
    const send = XMLHttpRequest.prototype.send;
    XMLHttpRequest.prototype.open = function (m, url, ...rest) {
      this.__novelGen = /GenerateContent/.test(String(url));
      return open.call(this, m, url, ...rest);
    };
    XMLHttpRequest.prototype.send = function (...a) {
      if (this.__novelGen) {
        gen.started++;
        gen.active.add(this);
        this.addEventListener('loadend', () => gen.active.delete(this));
      }
      return send.apply(this, a);
    };
  }

  const steps = {
    async prepare(job) {
      hookGenerate();
      await waitFor(() => $(PROMPT), 60000, 'ô prompt');
      await sleep(1000);
      await openRunSettings();
      if (job.mode === 'new') {
        await setModel(job.model);
        await setSi(job.si);
      }
      await setThinking(job.thinking);
      return { url: location.href, account: $('button.account-switcher-button')?.getAttribute('aria-label') || '?' };
    },

    async send(job) {
      const box = $(PROMPT);
      setText(box, job.prompt);
      await sleep(300);
      if (box.value.length !== job.prompt.length) throw new Error('prompt dán không đủ');
      const n = document.querySelectorAll('ms-chat-turn').length;
      const btn = await waitFor(() => { const b = $(RUN); return b && !b.disabled && b; }, 10000, 'nút Run bật');
      btn.click();
      const end = Date.now() + 60000;
      while (Date.now() < end) {
        if (running() || document.querySelectorAll('ms-chat-turn').length > n) return { started: true };
        const e = pageError();
        if (QUOTA.test(e)) return { error: e, kind: 'quota' };
        // Hộp thoại mời nâng cấp gói = tài khoản này hết lượt (hoặc không có lượt) cho model này.
        const up = [...document.querySelectorAll('mat-dialog-container, .cdk-overlay-pane')].filter(visible)
          .find(d => /Go further with AI Studio|ways to upgrade|plan limits/i.test(d.innerText));
        if (up) {
          up.querySelector('button[aria-label*="lose" i], button')?.click();
          return { error: `hộp thoại nâng cấp: ${up.innerText.trim().replace(/\s+/g, ' ').slice(0, 120)}`, kind: 'quota' };
        }
        await sleep(500);
      }
      const b = $(RUN);
      const dialogs = [...document.querySelectorAll('mat-dialog-container, .cdk-overlay-pane')].filter(visible)
        .map(d => d.innerText.trim().replace(/\s+/g, ' ').slice(0, 200)).filter(Boolean);
      throw new Error(`bấm Run nhưng không chạy: ${pageError() || 'không rõ lý do'} [nút "${b?.innerText.trim()
        .replace(/\s+/g, ' ')}" disabled=${b?.disabled} aria-disabled=${b?.getAttribute('aria-disabled')} | `
        + `ô prompt ${$(PROMPT)?.value.length} | lượt ${document.querySelectorAll('ms-chat-turn').length} | `
        + `hộp thoại: ${dialogs.join(' // ') || 'không'}]`);
    },

    async status() {
      const gen = window.__novelGen || { started: 0, active: new Set() };
      const busy = [...gen.active].some(x => x.readyState !== 4);
      return { running: running() || busy, started: gen.started > 0,
               textLen: lastReply().text.length, err: pageError() };
    },

    async collect() {
      await sleep(1500);
      const { models, text } = lastReply();
      const err = pageError();
      if (!text) {
        const msg = err || models.map(t => t.innerText).join('\n').slice(-600) || 'không có câu trả lời';
        const tags = models.map(t => [...new Set([...t.querySelectorAll('*')].map(e => e.tagName.toLowerCase())
          .filter(n => n.startsWith('ms-')))].join(',')).join(' / ');
        return { error: `${msg.slice(-300)} [model turns ${models.length}: ${tags} | tab ${document.visibilityState}]`,
                 kind: QUOTA.test(msg) ? 'quota' : 'error' };
      }
      const md = await copyMarkdown(models.at(-1));
      return { text, md, url: location.href, warning: [err, md ? '' : `copy markdown: ${mdError}`].filter(Boolean).join(' | ') };
    },
  };

  window.__novel = Object.fromEntries(Object.entries(steps).map(([k, f]) => [k, async a => {
    try { return (await f(a)) || {}; } catch (e) { return { error: String(e.message || e) }; }
  }]));
})();
