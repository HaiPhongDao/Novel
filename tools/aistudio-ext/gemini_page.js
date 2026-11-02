// Các bước trong trang Gemini Web (gemini.google.com); background.js gọi window.__novel.<bước>(job).
(() => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const $ = s => document.querySelector(s);
  const $$ = s => [...document.querySelectorAll(s)];

  async function waitFor(fn, ms, what) {
    const end = Date.now() + ms;
    while (Date.now() < end) {
      const v = fn();
      if (v) return v;
      await sleep(250);
    }
    throw new Error(`không thấy ${what}`);
  }

  function findInput() {
    return $('rich-textarea .ql-editor[contenteditable="true"]')
        || $('rich-textarea [contenteditable="true"]')
        || $('[role="textbox"][contenteditable="true"]')
        || $('div.ql-editor[contenteditable="true"]')
        || $('rich-textarea')
        || $('textarea[aria-label*="prompt" i]')
        || $('textarea');
  }

  function findSendButton() {
    const btns = $$('button');
    return btns.find(b => {
      const label = (b.getAttribute('aria-label') || '').toLowerCase();
      const testId = (b.getAttribute('data-test-id') || '').toLowerCase();
      const cls = (b.className || '').toLowerCase();
      return (label.includes('send') || label.includes('gửi')
          || testId.includes('send') 
          || cls.includes('send-button')
          || b.querySelector('mat-icon[fonticon="send"]')
          || b.querySelector('mat-icon[data-mat-icon-name="send"]')
          || b.querySelector('svg path[d*="M2.01 21L23 12 2.01 3"]'))
          && b.getClientRects().length > 0;
    });
  }

  function findStopButton() {
    const btns = $$('button');
    return btns.find(b => {
      const label = (b.getAttribute('aria-label') || '').toLowerCase();
      const testId = (b.getAttribute('data-test-id') || '').toLowerCase();
      const cls = (b.className || '').toLowerCase();
      return (label.includes('stop') || label.includes('dừng') || testId.includes('stop') || cls.includes('stop-button'))
          && b.getClientRects().length > 0;
    });
  }

  function getResponses() {
    const list = $$('message-content, .model-response-text, response-container, model-response, .response-content');
    return list.filter(el => el.getClientRects().length > 0 || el.innerText.trim().length > 0);
  }

  function setTextInQuill(el, text) {
    el.focus();
    // 1. execCommand insertText cập nhật chuẩn Delta của Quill
    document.execCommand('selectAll', false, null);
    let ok = false;
    try {
      ok = document.execCommand('insertText', false, text);
    } catch (e) {}

    // 2. Dự phòng gán thẻ p trực tiếp
    if (!ok || !el.innerText.trim()) {
      const html = text.split('\n')
        .map(l => `<p>${l ? l.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;') : '<br>'}</p>`)
        .join('');
      el.innerHTML = html;
      el.dispatchEvent(new Event('input', { bubbles: true }));
      el.dispatchEvent(new Event('change', { bubbles: true }));
    }
  }

  async function setModeAndThinking(modelName, thinkingLevel) {
    const modeBtn = $('[data-test-id="bard-mode-menu-button"]');
    if (!modeBtn) return;

    const needThinking = thinkingLevel && !['off', 'false'].includes(String(thinkingLevel).toLowerCase());
    const targetModel = modelName || 'Argon';

    modeBtn.click();
    await sleep(500);

    const items = $$('[role="menuitem"], [role="option"], mat-option, .mat-mdc-menu-item, button.mat-mdc-menu-item');
    
    // Chọn Model nếu chưa chọn
    if (targetModel) {
      const modelItem = items.find(i => (i.innerText || '').toLowerCase().includes(targetModel.toLowerCase()));
      if (modelItem && !modelItem.classList.contains('selected') && !modelItem.classList.contains('active')) {
        modelItem.click();
        await sleep(500);
        modeBtn.click();
        await sleep(500);
      }
    }

    // Chọn Thinking level (Low / Medium / High)
    if (needThinking) {
      const refreshedItems = $$('[role="menuitem"], [role="option"], mat-option, .mat-mdc-menu-item, button.mat-mdc-menu-item');
      const targetLevel = String(thinkingLevel).toLowerCase(); // 'low', 'medium', 'high'
      const thinkItem = refreshedItems.find(i => {
        const t = (i.innerText || '').toLowerCase();
        return t.startsWith(targetLevel) || t.includes(targetLevel);
      });
      if (thinkItem) {
        thinkItem.click();
        await sleep(400);
        return;
      }
    }

    // Bấm ra ngoài để đóng menu nếu không click mục nào
    $('body').click();
    await sleep(200);
  }

  window.__novel = {
    async prepare(job) {
      await waitFor(findInput, 15000, 'ô nhập câu hỏi trên Gemini Web');
      try {
        await setModeAndThinking(job.model || 'Argon', job.thinking || 'High');
      } catch (e) {
        console.warn('Lưu ý khi đặt mode / thinking:', e);
      }
      return { url: window.location.href, account: 'gemini-web' };
    },

    async send(job) {
      const input = await waitFor(findInput, 5000, 'ô nhập câu hỏi');
      setTextInQuill(input, job.prompt);
      await sleep(600);

      const sendBtn = await waitFor(findSendButton, 5000, 'nút Gửi trên Gemini Web');
      
      window.__novel_initial_count = getResponses().length;
      window.__novel_sent_time = Date.now();
      window.__novel_started = false;

      sendBtn.click();
      await sleep(1000);

      if (findStopButton() || getResponses().length > window.__novel_initial_count) {
        window.__novel_started = true;
      } else {
        input.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }));
        await sleep(1000);
      }
      return { ok: true };
    },

    status() {
      const stopBtn = findStopButton();
      const responses = getResponses();
      const isNewResponse = responses.length > (window.__novel_initial_count || 0);
      const lastResp = responses[responses.length - 1];
      const textLen = lastResp ? lastResp.innerText.trim().length : 0;
      
      if (stopBtn || isNewResponse) {
        window.__novel_started = true;
      }

      const isRunning = Boolean(stopBtn) || (isNewResponse && Date.now() - (window.__novel_sent_time || 0) < 5000 && textLen === 0);

      return {
        running: isRunning,
        started: Boolean(window.__novel_started),
        textLen: textLen,
        err: ''
      };
    },

    collect() {
      const responses = getResponses();
      if (!responses.length) {
        throw new Error('không tìm thấy câu trả lời nào trên trang Gemini Web');
      }
      const lastResp = responses[responses.length - 1];

      let thinkText = '';
      const thoughtEl = lastResp.querySelector('thought-box, .thought-container, details.thought-details, .thinking-process, [aria-label*="thought" i], [aria-label*="thinking" i], [data-test-id*="thought" i]');
      if (thoughtEl) {
        thinkText = thoughtEl.innerText.trim();
      }

      const clone = lastResp.cloneNode(true);
      for (const th of clone.querySelectorAll('thought-box, .thought-container, details, .action-button, button, mat-icon')) {
        th.remove();
      }

      const text = clone.innerText.trim();
      return {
        text: text,
        think: thinkText,
        url: window.location.href,
        md: text
      };
    }
  };
})();
