(function () {
  var R = { pass: 0, fail: 0, logs: [] };
  function ok(name, cond, info) { if (cond) { R.pass++; } else { R.fail++; } R.logs.push((cond ? 'PASS' : 'FAIL') + ' | ' + name + (info ? '  >> ' + info : '')); }
  function $(id) { return document.getElementById(id); }
  function $$(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }
  function waitFor(fn, cb, tries) {
    tries = (tries == null) ? 50 : tries;
    if (fn()) {
      try { cb(true); } catch (e) { R.fail++; R.logs.push('FAIL | ASYNC EXCEPTION | ' + (e && e.message)); finish(); }
      return;
    }
    if (tries <= 0) {
      try { cb(false); } catch (e) { R.fail++; R.logs.push('FAIL | ASYNC EXCEPTION | ' + (e && e.message)); finish(); }
      return;
    }
    setTimeout(function () { waitFor(fn, cb, tries - 1); }, 100);
  }
  window.__terrors = [];
  window.addEventListener('error', function (e) { window.__terrors.push(String(e.message)); });

  var steps = [];
  function step(fn) { steps.push(fn); }
  function run(i) {
    window.__testStep = i;
    if (i >= steps.length) { finish(); return; }
    try { steps[i](function () { run(i + 1); }); }
    catch (e) { R.fail++; R.logs.push('FAIL | EXCEPTION @step' + i + ' | ' + (e && e.message)); run(i + 1); }
  }
  function finish() {
    window.__testStep = 'done';
    var pre = document.createElement('pre');
    pre.id = 'TESTOUT';
    pre.textContent = 'TESTRESULT ' + R.pass + ' pass, ' + R.fail + ' fail\n' + R.logs.join('\n');
    document.body.appendChild(pre);
  }

  /* ---------- 1. boot: home shell ---------- */
  step(function (next) {
    clearData();
    updateChrome();
    showScreen('home');
    ok('boot: 5 screens', $$('.screen').length === 5, 'got ' + $$('.screen').length);
    ok('boot: bottom nav 5 buttons', $$('.bnav button').length === 5, 'got ' + $$('.bnav button').length);
    ok('boot: home active', (document.querySelector('.screen.active') || {}).id === 'screen-home');
    ok('boot: nav home active', document.querySelector('.bnav .nav.active').dataset.nav === 'home');
    ok('boot: 4 exercise cards', $$('.qa-row [data-goto-ex]').length === 4);
    ok('boot: no auto-speak checkbox', !document.querySelector('input[type=checkbox]'));
    ok('boot: removed old subtitle', !$('heroSub'));
    ok('boot: 4 exercise panels', $$('.expanel').length === 4);
    next();
  });

  /* ---------- 2. open exercise from card ---------- */
  step(function (next) {
    document.querySelector('.qa-row [data-goto-ex="mc-en"]').click();
    ok('exercise: screen active', (document.querySelector('.screen.active') || {}).id === 'screen-exercise');
    ok('exercise: 50 questions', $$('#list-mc-en .q').length === 50, 'got ' + $$('#list-mc-en .q').length);
    var allFour = $$('#list-mc-en .q').every(function (q) { return q.querySelectorAll('.opt').length === 4; });
    ok('exercise: every question has 4 options', allFour);
    ok('exercise: no POS chip in questions', $$('#list-mc-en .tchip').length === 0);
    ok('exercise: stat total 50', $('stTotal').textContent === '50', $('stTotal').textContent);
    var opts = $$('.opt', $('mc-en-q0'));
    var seen = {};
    var uniq = true;
    opts.forEach(function (o) { if (seen[o.dataset.key]) uniq = false; seen[o.dataset.key] = 1; });
    ok('exercise: 4 unique option keys', uniq);
    window.__optKeys = opts.map(function (o) { return o.dataset.key; });
    next();
  });

  /* ---------- 3. answer wrong -> bank + badge ---------- */
  step(function (next) {
    var s1 = S.en1k['mc-en'];
    var v0 = s1.items[0];
    var q0 = $('mc-en-q0');
    var opts = $$('.opt', q0);
    var correct = null, wrongOpt = null;
    for (var i = 0; i < opts.length; i++) {
      if (opts[i].dataset.key === v0.meaning) correct = opts[i];
      else if (!wrongOpt) wrongOpt = opts[i];
    }
    ok('answer: correct option present', !!correct);
    ok('answer: wrong option present', !!wrongOpt);
    wrongOpt.click();
    ok('answer: recorded wrong', !!s1.answers[0] && s1.answers[0].ok === false);
    ok('answer: correct option revealed', correct.classList.contains('correct'));
    ok('answer: wrong bank en = 1', wrong.en.length === 1, 'got ' + wrong.en.length);
    ok('answer: nav badge = 1', $('navBadge').textContent === '1' && $('navBadge').hidden === false);
    ok('answer: feedback shows answer', $('fb-mc-en-0').textContent.indexOf('Đáp án') !== -1);
    window.__v0 = v0;
    next();
  });

  /* ---------- 4. option order stable across re-render ---------- */
  step(function (next) {
    selectEx('mc-vn');
    selectEx('mc-en');
    var now = $$('.opt', $('mc-en-q0')).map(function (o) { return o.dataset.key; });
    ok('options: order stable after tab switch', JSON.stringify(now) === JSON.stringify(window.__optKeys), now.join('|').slice(0, 80));
    ok('options: answered question keeps highlight', !!$('mc-en-q0').querySelector('.opt.correct'));
    next();
  });

  /* ---------- 5. draft survives tab switch ---------- */
  step(function (next) {
    selectEx('write-vn');
    var inp = $('wv-in0');
    ok('draft: write input exists', !!inp);
    inp.value = 'draft-test';
    inp.dispatchEvent(new Event('input', { bubbles: true }));
    selectEx('mc-vn');
    selectEx('write-vn');
    ok('draft: value preserved', $('wv-in0').value === 'draft-test', $('wv-in0').value);
    $('wv-in0').value = '';
    $('wv-in0').dispatchEvent(new Event('input', { bubbles: true }));
    next();
  });

  /* ---------- 6. reveal counts as wrong and goes to bank ---------- */
  step(function (next) {
    selectEx('write-en');
    var s = S.en1k['write-en'];
    var v0 = s.items[0];
    var before = stats.answered;
    document.querySelector('[data-reveal="write-en:0"]').click();
    ok('reveal: recorded as wrong', !!s.answers[0] && s.answers[0].ok === false);
    ok('reveal: stats incremented', stats.answered === before + 1, 'answered=' + stats.answered);
    ok('reveal: word added to bank', wrong.en.some(function (w) { return w.word === v0.word && w.meaning === v0.meaning; }));
    ok('reveal: input readonly', $('we-in0').readOnly);
    var hasEx = !!(v0.ex && v0.ex.length);
    ok('reveal: example block matches data', ($$('#fb-write-en-0 .exfb').length > 0) === hasEx);
    var sampleFb = fbHtml('mc-en', { word: 'test', meaning: 'thử', ex: [{ s: 'This is a sample sentence.', t: 'Đây là một câu ví dụ.' }] }, { ok: false });
    ok('feedback: renders example sentence', sampleFb.indexOf('This is a sample sentence.') !== -1);
    next();
  });

  /* ---------- 7. wrong screen + practice + back ---------- */
  step(function (next) {
    showScreen('wrong');
    ok('wrong: screen active', (document.querySelector('.screen.active') || {}).id === 'screen-wrong');
    ok('wrong: rows match bank', $$('#wrongBody .drow').length === wrong.en.length, 'rows=' + $$('#wrongBody .drow').length + ' bank=' + wrong.en.length);
    ok('wrong: practice enabled', !$('wrongPractice').disabled);
    settings.ex = 'mc-en';
    $('wrongPractice').click();
    ok('wrong: practice screen active', (document.querySelector('.screen.active') || {}).id === 'screen-exercise');
    ok('wrong: nav pill on wrong', $('bnav').style.getPropertyValue('--nav-i') === '2', $('bnav').style.getPropertyValue('--nav-i'));
    ok('wrong: dataset is wrong', CUR_DS === 'wrong');
    ok('wrong: questions built from bank', $$('#list-mc-en .q').length === wrong.en.length, 'q=' + $$('#list-mc-en .q').length);
    ok('wrong: chips hidden', $('exChips').hidden === true);
    ok('wrong: chips visually hidden', $('exChips').offsetHeight === 0);
    document.querySelector('[data-back]').click();
    ok('wrong: back returns to wrong screen', (document.querySelector('.screen.active') || {}).id === 'screen-wrong');
    ok('wrong: back restores dataset', CUR_DS === 'en1k');
    next();
  });

  /* ---------- 8. dictionary A-Z + search + detail + synonyms ---------- */
  step(function (next) {
    showScreen('dict');
    ok('dict: screen active', (document.querySelector('.screen.active') || {}).id === 'screen-dict');
    ok('dict: EN selected', settings.lang === 'en');
    ok('dict: 27 letter chips', $$('#dictAZ .az').length === 27, 'got ' + $$('#dictAZ .az').length);
    waitFor(function () { return $$('#dictBody .drow').length > 0; }, function (done) {
      ok('dict: letter A rows rendered', done, 'rows=' + $$('#dictBody .drow').length);
      var rows = $$('#dictBody .drow');
      var allA = rows.every(function (r) { return fold(r.querySelector('.dword').textContent).charAt(0) === 'a'; });
      ok('dict: A rows start with A', allA);
      var meta = $('dictMeta').textContent;
      ok('dict: meta shows letter', meta.indexOf('A ·') === 0, meta);

      $('dictQ').value = 'ban do';
      renderDict();
      var hits = $$('#dictBody .drow');
      ok('dict: search accent-insensitive', hits.some(function (r) { return r.querySelector('.dword').textContent.indexOf('map') === 0; }), 'hits=' + hits.length);
      ok('dict: AZ chips hidden in search', $('dictAZ').offsetHeight === 0);
      ok('dict: search meta', $('dictMeta').textContent.indexOf('Tìm thấy') === 0, $('dictMeta').textContent);

      var mapRow = hits.filter(function (r) { return r.querySelector('.dword').textContent.indexOf('map') === 0; })[0];
      if (mapRow) mapRow.click();
      ok('dict: detail sheet opens', $('sheetWrap').hidden === false);
      ok('dict: sheet has word + close', !!document.querySelector('.sheet-word') && $$('[data-sheet-close]').length >= 1);
      ok('dict: sheet has examples or empty note', document.querySelector('.sheet .ex-none') !== null || $$('.sheet .exlist li').length > 0);
      closeSheet();
      ok('dict: sheet closes', $('sheetWrap').hidden === true);

      $('dictQ').value = 'apple';
      renderDict();
      var appleRow = $$('#dictBody .drow').filter(function (r) { return r.querySelector('.dword').textContent.indexOf('apple') === 0; })[0];
      ok('dict: apple row found', !!appleRow);
      if (appleRow) appleRow.click();
      ok('dict: apple sheet shows 3 examples', $$('.sheet .exlist li').length === 3, 'got ' + $$('.sheet .exlist li').length);
      closeSheet();

      $('dictQ').value = 'chắc chắn';
      renderDict();
      var gt = document.querySelector('#dictBody .dgt');
      ok('dict: synonym group header', !!gt && gt.textContent.indexOf('Cùng nghĩa') !== -1, gt ? gt.textContent : 'none');
      next();
    });
  });

  /* ---------- 9. dictionary DE ---------- */
  step(function (next) {
    setDictLang('de');
    ok('dict: DE selected', settings.lang === 'de');
    $('dictQ').value = 'thema';
    renderDict();
    var hits = $$('#dictBody .drow');
    ok('dict: DE search finds Thema', hits.some(function (r) { return r.querySelector('.dword').textContent.indexOf('Thema') !== -1; }), 'hits=' + hits.length);
    next();
  });

  /* ---------- 9b. grammar dictionary + 200k bank ---------- */
  step(function (next) {
    if (settings.lang !== 'en') setLang('en');
    showScreen('dict');
    setDictMode('grammar');
    ok('grammar: mode grammar', settings.dictMode === 'grammar', settings.dictMode);
    ok('grammar: language segment hidden', $('dictLangSeg').hidden === true);
    ok('grammar: 46 topics rendered', $$('#dictBody .grow').length === 46, 'got ' + $$('#dictBody .grow').length);
    ok('grammar: 5 category chips', $$('#dictCats .chip').length === 5, 'got ' + $$('#dictCats .chip').length);
    ok('grammar: 12 tense rows show bank', $$('#dictBody .gbank').length === 12, 'got ' + $$('#dictBody .gbank').length);
    ok('grammar: bank total 2.4m', grammarBankTotal() === 2400000, String(grammarBankTotal()));
    ok('grammar: capacity 200k only for tenses', grammarCapacity('present-simple') === 200000 && grammarCapacity('articles') === 0);

    var g1 = grammarItem('present-simple', 42);
    var g2 = grammarItem('present-simple', 42);
    ok('grammar: deterministic item', !!g1 && !!g2 && g1.answer === g2.answer && g1.tokens.join(' ') === g2.tokens.join(' '));
    ok('grammar: tokens keep all words', g1.tokens.slice().sort().join(' ') === g1.answer.split(' ').sort().join(' '), g1.answer);
    ok('grammar: last index valid', !!grammarItem('present-simple', 199999));
    ok('grammar: index clamped', grammarItem('present-simple', 999999).id === 'present-simple:199999');
    ok('grammar: malformed input safe', grammarItem('nope') === null && grammarItem('articles') === null && !!grammarItem('present-simple', 'abc'));

    ok('grammar: 3s negative uses base verb', grammarItem('present-simple', 18433).answer.indexOf('He does not read') === 0, grammarItem('present-simple', 18433).answer);
    ok('grammar: 3s question uses base verb', grammarItem('present-simple', 18434).answer.indexOf('Does he read') === 0, grammarItem('present-simple', 18434).answer);
    ok('grammar: 3s fronted time uses -s', grammarItem('present-simple', 18435).answer.indexOf('Every day, he reads') === 0, grammarItem('present-simple', 18435).answer);
    ok('grammar: past negative uses base verb', grammarItem('past-simple', 18817).answer.indexOf('He did not write') === 0, grammarItem('past-simple', 18817).answer);
    var tenseBad = 0;
    Object.keys(TENSE_PROFILE).forEach(function (id) {
      for (var pi = 0; pi < 4; pi++) {
        var it = grammarItem(id, pi);
        if (!it || /\{/.test(it.answer) || it.answer.indexOf('  ') !== -1 || it.tokens.slice().sort().join(' ') !== it.answer.split(' ').sort().join(' ')) tenseBad++;
      }
    });
    ok('grammar: 12 tenses x 4 templates valid', tenseBad === 0, 'bad=' + tenseBad);

    $('dictQ').value = 'perfect';
    renderDict();
    var perfectRows = $$('#dictBody .grow');
    var perfectTitles = perfectRows.map(function (x) { return x.querySelector('.gtitle').textContent; });
    ok('grammar: search perfect finds 7', perfectRows.length === 7 && perfectRows.every(function (x) { return fold(x.textContent).indexOf('perfect') !== -1; }), perfectTitles.join(', '));

    $('dictQ').value = '';
    setGrammarCat('Thì');
    ok('grammar: cat Thì = 12', $$('#dictBody .grow').length === 12, 'got ' + $$('#dictBody .grow').length);
    setGrammarCat('TOEIC & IELTS');
    ok('grammar: cat TOEIC = 4', $$('#dictBody .grow').length === 4, 'got ' + $$('#dictBody .grow').length);
    setGrammarCat('all');
    ok('grammar: cat all = 46', $$('#dictBody .grow').length === 46);

    $$('#dictBody .grow')[0].click();
    ok('grammar: detail opens', $('sheetWrap').hidden === false);
    ok('grammar: detail formula + use', !!document.querySelector('.sheet-gformula') && !!document.querySelector('.sheet-guse'));
    ok('grammar: detail signals + exam', !!document.querySelector('.sheet-gsig') && !!document.querySelector('.sheet-gexam'));
    ok('grammar: detail bank note', !!document.querySelector('.sheet-gbank') && document.querySelector('.sheet-gbank').textContent.indexOf('200') !== -1);
    closeSheet();

    var firstRow = $$('#dictBody .grow')[0];
    firstRow.focus();
    firstRow.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', bubbles: true }));
    ok('grammar: Enter opens detail', $('sheetWrap').hidden === false);
    closeSheet();
    openGrammar('nope');
    ok('grammar: unknown topic ignored', $('sheetWrap').hidden === true);

    $('dictQ').value = '';
    setDictMode('words');
    ok('grammar: back to words mode', settings.dictMode === 'words' && $('dictLangSeg').hidden === false);
    next();
  });

  /* ---------- 10. settings + language ---------- */
  step(function (next) {
    if (settings.lang !== 'en') setLang('en');
    showScreen('settings');
    ok('settings: screen active', (document.querySelector('.screen.active') || {}).id === 'screen-settings');
    ok('settings: nav pill on settings', $('bnav').style.getPropertyValue('--nav-i') === '4', $('bnav').style.getPropertyValue('--nav-i'));
    ok('settings: EN active', document.querySelector('[data-set-lang="en"]').classList.contains('active'));
    document.querySelector('[data-set-lang="de"]').click();
    ok('lang: hero says Đức', $('heroLang').textContent === 'Đức', $('heroLang').textContent);
    ok('lang: ds de3k', settings.ds === 'de3k', settings.ds);
    ok('settings: DE active', document.querySelector('[data-set-lang="de"]').classList.contains('active'));
    ok('settings: pill stays on avatar', $('bnav').style.getPropertyValue('--nav-i') === '4', $('bnav').style.getPropertyValue('--nav-i'));
    showScreen('home');
    ok('lang: only DE dataset', settings.ds === 'de3k' && $('heroDsLabel').textContent.indexOf('Deutsch') !== -1, settings.ds + ' / ' + $('heroDsLabel').textContent);
    showScreen('settings');
    document.querySelector('[data-set-lang="en"]').click();
    ok('lang: back to en1k', settings.ds === 'en1k', settings.ds);
    ok('settings: EN active again', document.querySelector('[data-set-lang="en"]').classList.contains('active'));
    showScreen('home');
    ok('lang: EN dataset', settings.ds === 'en1k' && $('heroDsLabel').textContent.indexOf('1.000') !== -1, settings.ds + ' / ' + $('heroDsLabel').textContent);
    next();
  });

  /* ---------- 11. profile + avatar ---------- */
  step(function (next) {
    showScreen('settings');
    ok('profile: profile mode on', document.body.classList.contains('profile-mode'));
    ok('profile: screen active', (document.querySelector('.screen.active') || {}).id === 'screen-settings');
    ok('profile: hero + avatar', !!$('profileHero') && !!$('profileAvatarImg'));
    ok('profile: stats rendered', $('setAnswered').textContent === fmt(stats.answered));
    ok('profile: language seg active', document.querySelector('[data-set-lang="en"]').classList.contains('active'));
    ok('profile: tag active', document.querySelector('[data-tag-lang="en"]').classList.contains('active'));
    ok('profile: file input image', $('avatarFile').accept.indexOf('image/') !== -1);
    ok('profile: size select sync', $('setSizeSel').value === String(settings.size));
    ok('profile: settings rows', !!document.querySelector('[data-nav="wrong"]') && !!document.querySelector('[data-nav="dict"]'));
    var darkScheme = matchMedia('(prefers-color-scheme: dark)').matches;
    var pfInk = getComputedStyle(document.querySelector('.profile-sec-title')).color;
    ok('profile: follows device theme', pfInk === (darkScheme ? 'rgb(242, 246, 255)' : 'rgb(15, 23, 42)'), pfInk);
    ok('profile: color-scheme matches theme', getComputedStyle(document.body).colorScheme === (darkScheme ? 'dark' : 'light'), getComputedStyle(document.body).colorScheme);

    document.querySelector('[data-tag-lang="de"]').click();
    ok('profile: tag switches language', settings.lang === 'de');
    ok('profile: DE tag active', document.querySelector('[data-tag-lang="de"]').classList.contains('active'));
    document.querySelector('[data-tag-lang="en"]').click();
    ok('profile: back to English', settings.lang === 'en');

    var px = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9Zl1sAAAAASUVORK5CYII=';
    setAvatar(px);
    ok('profile: nav avatar photo', $('navAvatarImg').getAttribute('src') === px);
    ok('profile: profile avatar photo', $('profileAvatarImg').getAttribute('src') === px);
    ok('profile: home avatar photo', $('homeAvatarImg').getAttribute('src') === px);
    ok('profile: home avatar visible', $('homeAvatarImg').hidden === false);
    ok('profile: nav avatar has-photo', document.querySelector('.bnav .avatar-img').classList.contains('has-photo'));
    ok('profile: hero has-photo', $('profileHero').classList.contains('has-photo'));
    ok('profile: hero bg uses photo', $('profileHeroBg').style.backgroundImage.indexOf('data:image/png') !== -1);
    ok('profile: avatar persisted', LS.get('v4t:avatar', null) === px);
    ok('profile: clear button visible', $('avatarClear').hidden === false);
    clearAvatar();
    ok('profile: nav avatar cleared', $('navAvatarImg').hidden === true);
    ok('profile: home avatar cleared', $('homeAvatarImg').hidden === true);
    ok('profile: avatar storage cleared', LS.get('v4t:avatar', null) === null);
    ok('profile: nav avatar has-photo off', !document.querySelector('.bnav .avatar-img').classList.contains('has-photo'));

    showScreen('home');
    ok('profile: profile mode off', !document.body.classList.contains('profile-mode'));
    next();
  });

  /* ---------- 12. liquid glass bottom nav ---------- */
  step(function (next) {
    showScreen('home');
    var nav = $('bnav');
    var pill = document.querySelector('.bnav-pill');
    var items = $$('.bnav-item');
    ok('nav: 5 equal slots', items.length === 5 && (function () {
      var w = items.map(function (b) { return b.getBoundingClientRect().width; });
      return Math.max.apply(null, w) - Math.min.apply(null, w) < 1.5;
    })(), items.map(function (b) { return Math.round(b.getBoundingClientRect().width); }).join(','));
    ok('nav: pill index home', nav.style.getPropertyValue('--nav-i') === '0', nav.style.getPropertyValue('--nav-i'));
    ok('nav: pill matches slot width', Math.abs(pill.getBoundingClientRect().width - items[0].getBoundingClientRect().width) < 1.5, pill.getBoundingClientRect().width + ' vs ' + items[0].getBoundingClientRect().width);
    ok('nav: active icon glow', getComputedStyle(document.querySelector('.bnav .nav.active svg')).filter.indexOf('drop-shadow') !== -1);
    ok('nav: badge pulse', getComputedStyle($('navBadge')).animationName.indexOf('softPulse') !== -1, getComputedStyle($('navBadge')).animationName);
    ok('nav: no external assets', $$('script[src],link[href^="http"]').length === 0);

    document.querySelector('.bnav [data-nav="exercise"]').click();
    ok('nav: play opens exercise', (document.querySelector('.screen.active') || {}).id === 'screen-exercise');
    ok('nav: pill on exercise', nav.style.getPropertyValue('--nav-i') === '1', nav.style.getPropertyValue('--nav-i'));
    ok('nav: exercise active', document.querySelector('.bnav [data-nav="exercise"]').classList.contains('active'));

    showScreen('wrong');
    ok('nav: pill on wrong', nav.style.getPropertyValue('--nav-i') === '2', nav.style.getPropertyValue('--nav-i'));
    showScreen('dict');
    ok('nav: pill on dict', nav.style.getPropertyValue('--nav-i') === '3', nav.style.getPropertyValue('--nav-i'));
    showScreen('settings');
    ok('nav: pill on settings', nav.style.getPropertyValue('--nav-i') === '4', nav.style.getPropertyValue('--nav-i'));
    showScreen('home');
    ok('nav: pill back home', nav.style.getPropertyValue('--nav-i') === '0', nav.style.getPropertyValue('--nav-i'));
    next();
  });

  /* ---------- 13. fintech home ---------- */
  step(function (next) {
    showScreen('home');
    ok('home: mode on', document.body.classList.contains('home-mode'));
    ok('home: top bar', !!$('homeAvatarImg') && !!$('homeBellDot') && !!$('homeGreet'));
    ok('home: hero value', $('heroValue').textContent.indexOf('2') === 0, $('heroValue').textContent);
    ok('home: hero pill', $('heroPill').textContent.indexOf('% đúng') !== -1, $('heroPill').textContent);
    ok('home: 4 quick actions', $$('.qa-row [data-goto-ex]').length === 4);
    ok('home: 7 week bars', $$('#chart .chart-col').length === 7, 'got ' + $$('#chart .chart-col').length);
    ok('home: week total', $('chartTotal').textContent === '2', $('chartTotal').textContent);
    ok('home: peak bar', $$('#chart .chart-bar.peak').length === 1);
    ok('home: bell dot', $('homeBellDot').hidden === false);
    ok('home: recent rows', $$('#recentBody .act-row').length === 2, 'got ' + $$('#recentBody .act-row').length);
    ok('home: recent amount', $$('#recentBody .act-amount').length === 2);

    document.querySelector('[data-chart="month"]').click();
    ok('home: month mode', settings.chart === 'month' && $$('#chart .chart-col').length === 4, 'got ' + $$('#chart .chart-col').length);
    document.querySelector('[data-chart="week"]').click();
    ok('home: back to week', settings.chart === 'week' && $$('#chart .chart-col').length === 7);

    var dsBefore = settings.ds;
    document.querySelector('[data-ds-cycle]').click();
    ok('home: dataset cycles', settings.ds !== dsBefore, settings.ds);
    document.querySelector('[data-ds-cycle]').click();
    ok('home: dataset restored', settings.ds === dsBefore, settings.ds);

    document.querySelector('[data-activity-all]').click();
    ok('home: activity sheet', $('sheetWrap').hidden === false);
    ok('home: activity sheet rows', $$('#sheetBody .act-row').length === 2, 'got ' + $$('#sheetBody .act-row').length);
    closeSheet();

    document.querySelector('.home-bell').click();
    ok('home: bell opens wrong', (document.querySelector('.screen.active') || {}).id === 'screen-wrong');
    showScreen('home');
    ok('home: back home', (document.querySelector('.screen.active') || {}).id === 'screen-home');
    next();
  });

  /* ---------- 14. data sanity ---------- */
  step(function (next) {
    var total = DATASETS.en1k.words.length + DATASETS.en3k.words.length + DATASETS.de3k.words.length;
    ok('data: total words', total === 7514, 'got ' + total);
    ok('data: mc option pools not POS-locked', (function () {
      var s = S.en1k['mc-en'];
      if (!s) return false;
      var types = {};
      s.items.slice(0, 5).forEach(function (w) { types[primaryType(w.type)] = 1; });
      return Object.keys(types).length > 1;
    })());
    ok('data: every word has examples', (function () {
      var missing = 0;
      ['en1k', 'en3k', 'de3k'].forEach(function (k) {
        DATASETS[k].words.forEach(function (w) { if (!w.ex || !w.ex.length) missing++; });
      });
      return missing === 0;
    })());
    ok('runtime: no JS errors', window.__terrors.length === 0, JSON.stringify(window.__terrors.slice(0, 3)));

    localStorage.setItem('v4t:debug', '1');
    window.dispatchEvent(new ErrorEvent('error', { message: 'TypeError: real app bug' }));
    ok('errors: debug banner shows real error', $('errBar').style.display === 'block', $('errBar').style.display);
    $('errBar').style.display = 'none';
    window.dispatchEvent(new ErrorEvent('error', { message: "TypeError: undefined is not an object (evaluating 'window.__firefox__.reader')" }));
    ok('errors: firefox reader noise filtered', $('errBar').style.display !== 'block', $('errBar').style.display);
    localStorage.removeItem('v4t:debug');
    window.__terrors.length = 0;
    next();
  });

  run(0);
})();
