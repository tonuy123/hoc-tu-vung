// run-cdp.js - open page in Chrome (CDP), inject page tests, report results,
// then run mobile viewport checks + screenshot + noscript check.
// Usage: node tests/run-cdp.js <file-url>
const fs = require('fs');
const path = require('path');
const PORT = 9222;
const URL = process.argv[2];
const SHOT_DIR = path.join(__dirname, '..', 'report');

async function newTarget(url) {
  const res = await fetch(`http://127.0.0.1:${PORT}/json/new?${encodeURIComponent(url)}`, { method: 'PUT' });
  return res.json();
}

async function main() {
  if (!URL) throw new Error('missing page URL');
  const target = await newTarget(URL);
  const ws = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => { ws.onopen = resolve; ws.onerror = reject; });

  let id = 0;
  const pending = new Map();
  ws.onmessage = (ev) => {
    const m = JSON.parse(ev.data);
    if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); }
  };
  const send = (method, params) => new Promise((resolve) => {
    const i = ++id; pending.set(i, resolve);
    ws.send(JSON.stringify({ id: i, method, params: params || {} }));
  });
  async function evaljs(expr) {
    const r = await send('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true });
    if (!r.result) return 'NO_RESULT ' + JSON.stringify(r).slice(0, 200);
    if (r.result.exceptionDetails) return 'EXCEPTION: ' + (r.result.exceptionDetails.exception ? r.result.exceptionDetails.exception.description : r.result.exceptionDetails.text);
    return r.result.result ? r.result.result.value : 'NO_VALUE';
  }

  await send('Runtime.enable');
  await send('Page.enable');

  let appReady = false;
  for (let i = 0; i < 80; i++) {
    const st = await evaljs("(typeof DATASETS === 'undefined' || typeof showScreen !== 'function' || document.querySelectorAll('.screen').length !== 4 || document.querySelectorAll('.bnav button').length !== 5) ? 'no' : 'yes'");
    if (st === 'yes') { appReady = true; break; }
    await new Promise((r) => setTimeout(r, 500));
  }
  console.log('APP_READY:', appReady);

  const testCode = fs.readFileSync(path.join(__dirname, 'page-tests.js'), 'utf8');
  const injected = await evaljs('(function(){ ' + testCode + ' return "INJECTED"; })()');
  console.log('INJECT:', injected);

  let out = null;
  for (let i = 0; i < 260; i++) {
    await new Promise((r) => setTimeout(r, 500));
    out = await evaljs("(function(){ var el = document.getElementById('TESTOUT'); return el ? el.textContent : ''; })()");
    if (out && String(out).indexOf('TESTRESULT') === 0) break;
  }
  console.log(out || 'TESTOUT NOT FOUND');
  if (!out || String(out).indexOf('TESTRESULT') !== 0) {
    const dbg = await evaljs("(function(){return JSON.stringify({step: window.__testStep, errs: window.__terrors, bar: (document.getElementById('errBar')||{}).textContent});})()");
    console.log('DEBUG:', dbg);
  }

  // ---- mobile viewport: home + dictionary (reload with metrics = realistic phone load) ----
  await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
  await send('Page.reload', {});
  await new Promise((r) => setTimeout(r, 2500));
  await evaljs("(function(){ showScreen('home'); return 1; })()");
  await new Promise((r) => setTimeout(r, 500));
  const home = JSON.parse(await evaljs(`JSON.stringify({sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth, nav: document.querySelectorAll('.bnav button').length, cards: document.querySelectorAll('#homeGrid [data-goto-ex]').length})`));
  console.log('MOBILE_HOME:', JSON.stringify(home));
  console.log('MOBILE_HOME_OK:', home.sw <= home.cw + 1);

  await evaljs("(function(){ showScreen('dict'); return 1; })()");
  await new Promise((r) => setTimeout(r, 700));
  const mob = JSON.parse(await evaljs(`JSON.stringify({sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth, rows: document.querySelectorAll('#dictBody .drow').length, letter: (document.querySelector('#dictAZ .az.on')||{}).textContent, nav: document.querySelectorAll('.bnav button').length})`));
  console.log('MOBILE_DICT:', JSON.stringify(mob));
  console.log('MOBILE_OVERFLOW_OK:', mob.sw <= mob.cw + 1);
  const shot = await send('Page.captureScreenshot', { format: 'png', fromSurface: true });
  if (shot.result && shot.result.data) {
    fs.writeFileSync(path.join(SHOT_DIR, 'mobile-dict.png'), Buffer.from(shot.result.data, 'base64'));
    console.log('SHOT: report/mobile-dict.png');
  }
  await send('Emulation.clearDeviceMetricsOverride');

  // ---- noscript check ----
  await send('Emulation.setScriptExecutionDisabled', { value: true });
  await send('Page.reload', {});
  await new Promise((r) => setTimeout(r, 2500));
  const ns = await evaljs("(function(){ return document.body ? document.body.innerText.indexOf('Quick Look') !== -1 : false; })()");
  console.log('NOSCRIPT_BANNER_VISIBLE:', ns);
  await send('Emulation.setScriptExecutionDisabled', { value: false });
  await send('Page.reload', {});
  await new Promise((r) => setTimeout(r, 2500));
  const back = await evaljs("(function(){ return typeof DATASETS !== 'undefined' && document.querySelectorAll('.screen').length === 4 && document.querySelectorAll('.bnav button').length === 5; })()");
  console.log('JS_REENABLED_BOOT_OK:', back);

  ws.close();
}

main().catch((e) => { console.error('CDP_ERR', e && e.message); process.exit(1); });
