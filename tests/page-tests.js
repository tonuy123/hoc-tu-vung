(function () {
  var R = { pass: 0, fail: 0, logs: [] };
  function ok(name, cond, info) { if (cond) { R.pass++; } else { R.fail++; } R.logs.push((cond ? 'PASS' : 'FAIL') + ' | ' + name + (info ? '  >> ' + info : '')); }
  function $(id) { return document.getElementById(id); }
  function $$(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }
  function waitFor(fn, cb, tries) {
    tries = (tries == null) ? 50 : tries;
    if (fn()) { cb(true); return; }
    if (tries <= 0) { cb(false); return; }
    setTimeout(function () { waitFor(fn, cb, tries - 1); }, 100);
  }
  window.__terrors = [];
  window.addEventListener('error', function (e) { window.__terrors.push(String(e.message)); });

  var steps = [];
  function step(fn) { steps.push(fn); }
  function run(i) {
    if (i >= steps.length) { finish(); return; }
    try { steps[i](function () { run(i + 1); }); }
    catch (e) { R.fail++; R.logs.push('FAIL | EXCEPTION @step' + i + ' | ' + (e && e.message)); run(i + 1); }
  }
  function finish() {
    var pre = document.createElement('pre');
    pre.id = 'TESTOUT';
    pre.textContent = 'TESTRESULT ' + R.pass + ' pass, ' + R.fail + ' fail\n' + R.logs.join('\n');
    document.body.appendChild(pre);
  }

  /* ---------- 1. boot ---------- */
  step(function (next) {
    clearData();
    updateTexts(); updateWrongChip(); renderFoot();
    showTab('mc-en', true);
    ok('boot: 50 mc-en questions built', $$('#list-mc-en .q').length === 50, 'got ' + $$('#list-mc-en .q').length);
    var allFour = $$('#list-mc-en .q').every(function (q) { return q.querySelectorAll('.opt').length === 4; });
    ok('boot: every question has 4 options', allFour);
    ok('boot: total = 50', $('stTotal').textContent === '50', 'got ' + $('stTotal').textContent);
    ok('boot: 6 tabs present', $$('.tab').length === 6, 'got ' + $$('.tab').length);
    next();
  });

  /* ---------- 2. answer wrong -> bank + note ---------- */
  step(function (next) {
    var s1 = S.en1k['mc-en'];
    var v0 = s1.items[0];
    var q0 = $('mc-en-q0');
    var opts = $$('.opt', q0);
    var correctOpt = null, wrongOpt = null;
    for (var i = 0; i < opts.length; i++) {
      if (opts[i].dataset.key === v0.meaning) correctOpt = opts[i]; else wrongOpt = opts[i];
    }
    ok('mc: correct option present', !!correctOpt);
    wrongOpt.click();
    ok('mc: answer recorded wrong', !!s1.answers[0] && s1.answers[0].ok === false);
    ok('mc: correct option revealed', correctOpt.classList.contains('correct'));
    ok('mc: wrong bank en = 1', wrong.en.length === 1, 'got ' + wrong.en.length);
    var fbTxt = $('fb-mc-en-0').textContent;
    ok('mc: feedback notes saved to bank', fbTxt.indexOf('Từ sai') !== -1, 'fb=' + fbTxt.slice(0, 90));
    window.__v0 = v0;
    next();
  });

  /* ---------- 3. list-1k render ---------- */
  step(function (next) {
    showTab('list-1k', true);
    waitFor(function () { return $$('#lst-body-1k .lrow').length === 1000; }, function (done) {
      ok('list-1k: renders all 1000 rows', done, 'rows=' + $$('#lst-body-1k .lrow').length);
      ok('list-1k: meta total', $('lst-meta-1k').textContent === 'Tổng 1.000 từ', $('lst-meta-1k').textContent);
      var v = window.__v0;
      var row = $$('#lst-body-1k .lrow').filter(function (r) { return r.querySelector('.lnum').textContent === String(v.num); })[0];
      ok('list-1k: row for answered word exists', !!row);
      if (row) {
        ok('list-1k: bank badge on wrong word', !!row.querySelector('.lsaved'));
        var wordBtn = row.querySelector('.spk2');
        ok('list-1k: speak button present', !!wordBtn);
      }
      next();
    });
  });

  /* ---------- 4. search 1k + accent-insensitive ---------- */
  step(function (next) {
    var q = $('lst-q-1k');
    q.value = 'ban do';
    q.dispatchEvent(new Event('input', { bubbles: true }));
    setTimeout(function () {
      var rows = $$('#lst-body-1k .lrow');
      ok('search: results non-empty for "ban do"', rows.length > 0, 'rows=' + rows.length);
      var hit = rows.filter(function (r) { return r.querySelector('.lnum').textContent === '504'; })[0];
      ok('search: accent-insensitive finds "map" (bản đồ)', !!hit, 'map row found=' + !!hit);
      var allMatch = rows.every(function (r) {
        var w = r.querySelector('.lword').textContent, m = r.querySelector('.lmean').textContent;
        var s = fold(w + ' ' + m);
        return s.indexOf('ban') !== -1 && s.indexOf('do') !== -1;
      });
      ok('search: every row matches all tokens', allMatch);
      ok('search: meta count format', /^Tìm thấy [\d.]+ \/ 1\.000 từ$/.test($('lst-meta-1k').textContent), $('lst-meta-1k').textContent);
      next();
    }, 400);
  });

  /* ---------- 5. clear button ---------- */
  step(function (next) {
    document.querySelector('[data-lstclear="list-1k"]').click();
    setTimeout(function () {
      ok('clear: input emptied', $('lst-q-1k').value === '');
      ok('clear: meta back to total', $('lst-meta-1k').textContent === 'Tổng 1.000 từ', $('lst-meta-1k').textContent);
      next();
    }, 400);
  });

  /* ---------- 6. language switch -> de list ---------- */
  step(function (next) {
    setLang('de');
    ok('lang de: tab 1k hidden', $('tabList1k').hidden === true);
    ok('lang de: tab 3k relabeled', $('tabList3k').textContent.indexOf('Deutsch') !== -1, $('tabList3k').textContent);
    showTab('list-3k', true);
    waitFor(function () { return $$('#lst-body-3k .lrow').length === 3035; }, function (done) {
      ok('list-de: renders all 3035 rows', done, 'rows=' + $$('#lst-body-3k .lrow').length);
      ok('list-de: meta total', $('lst-meta-3k').textContent === 'Tổng 3.035 từ', $('lst-meta-3k').textContent);
      $('lst-q-3k').value = 'thema';
      $('lst-q-3k').dispatchEvent(new Event('input', { bubbles: true }));
      setTimeout(function () {
        var rows = $$('#lst-body-3k .lrow');
        var hit = rows.filter(function (r) { return r.querySelector('.lnum').textContent === '1501'; })[0];
        ok('list-de: search "thema" finds das Thema', !!hit, 'rows=' + rows.length);
        next();
      }, 400);
    });
  });

  /* ---------- 7. switch back to en, session intact ---------- */
  step(function (next) {
    setLang('en');
    ok('lang en: tab 1k visible again', $('tabList1k').hidden === false);
    showTab('mc-en', true);
    ok('back: mc-en restored with answer', !!S.en1k['mc-en'].answers[0]);
    ok('back: stat wrong = 1', $('stWrong').textContent === '1', $('stWrong').textContent);
    ok('runtime: no JS errors', window.__terrors.length === 0, JSON.stringify(window.__terrors.slice(0, 3)));
    next();
  });

  run(0);
})();
