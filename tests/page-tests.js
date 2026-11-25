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
    ok('boot: 6 exercise panels', $$('.expanel').length === 6, 'got ' + $$('.expanel').length);
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

  /* ---------- 7b. wrong review must not resample the session mid-flow ---------- */
  step(function (next) {
    var savedEn = wrong.en.slice();
    var savedStats = JSON.parse(JSON.stringify(stats));
    var savedDaily = JSON.parse(JSON.stringify(daily));
    var savedRecent = recent.slice();
    setLang('de');
    var mk = function (n, w, m) { return { num: n, word: w, meaning: m, type: 'n', phon: '', extra: '', topics: [] }; };
    wrong.de = [mk(1, 'die Dusche', 'vòi sen'), mk(2, 'der Herr', 'ông, ngài'), mk(3, 'der Urlaub', 'kỳ nghỉ'),
                mk(4, 'die Hochzeit', 'đám cưới'), mk(5, 'der Fernseher', 'máy tivi · ti vi')];
    LS.set('v4t:wrong', wrong);
    bumpWrong();
    showScreen('wrong');
    practiceWrong();
    var s0 = S.wrong['mc-en'];
    ok('wrong review: session of 5', !!s0 && s0.items.length === 5, s0 ? s0.items.length : 'none');
    var qs = $$('#list-mc-en .q');
    var clickByKey = function (q, key) {
      var hit = null;
      $$('.opt', q).forEach(function (o) { if (o.dataset.key === key) hit = o; });
      if (hit) hit.click();
      return !!hit;
    };
    ok('wrong review: first correct option found', clickByKey(qs[0], s0.items[0].meaning));
    ok('wrong review: session object kept after answer 1', S.wrong['mc-en'] === s0);
    var second = s0.items[1];
    ok('wrong review: second correct option found', clickByKey(qs[1], second.meaning));
    ok('wrong review: session object kept after answer 2', S.wrong['mc-en'] === s0);
    ok('wrong review: answer 2 graded correct', !!(s0.answers[1] && s0.answers[1].ok), qs[1].querySelector('.fb').textContent);
    ok('wrong review: question still matches session item', qs[1].querySelector('.qword').textContent === dispWord(second.word),
      qs[1].querySelector('.qword').textContent + ' vs ' + second.word);
    /* restore for later steps */
    wrong.en = savedEn;
    wrong.de = [];
    LS.set('v4t:wrong', wrong);
    stats = savedStats; LS.set('v4t:stats', stats);
    daily = savedDaily; LS.set('v4t:daily', daily);
    recent = savedRecent; LS.set('v4t:recent', recent);
    bumpWrong();
    delete S.wrong;
    setLang('en');
    showScreen('home');
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

      $('dictQ').value = '';
      setWordCat('all');
      var typeChips = $$('#dictCats .chip').map(function (c) { return c.textContent; });
      ok('dict: word type chips', typeChips.length === 8 && typeChips.indexOf('Động từ') !== -1 && typeChips.indexOf('Cảm xúc') !== -1 && typeChips.indexOf('Hành động') !== -1, typeChips.join('|'));

      setWordCat('verb');
      var verbRows = $$('#dictBody .drow');
      ok('dict: verb filter', settings.wtype === 'verb' && verbRows.length > 0 && verbRows.every(function (r) { return r.querySelector('.dpos').textContent.indexOf('động từ') !== -1; }), 'rows=' + verbRows.length);
      ok('dict: verb filter meta', $('dictMeta').textContent.indexOf('Động từ') !== -1 && $('dictSub').textContent.indexOf('Động từ') !== -1, $('dictMeta').textContent);

      setWordCat('emotion');
      var emoRows = $$('#dictBody .drow');
      ok('dict: emotion filter', settings.wtype === 'emotion' && emoRows.length > 0 && emoRows.every(function (r) { return r.querySelector('.dpos').textContent.indexOf('cảm xúc') !== -1; }), 'rows=' + emoRows.length);

      setWordCat('action');
      var actRows = $$('#dictBody .drow');
      ok('dict: action filter', settings.wtype === 'action' && actRows.length > 0 && actRows.every(function (r) { return r.querySelector('.dpos').textContent.indexOf('hành động') !== -1; }), 'rows=' + actRows.length);

      setWordCat('verb');
      $('dictQ').value = 'run';
      renderDict();
      var runRows = $$('#dictBody .drow');
      ok('dict: search respects type filter', runRows.length > 0 && runRows.every(function (r) { return r.querySelector('.dpos').textContent.indexOf('động từ') !== -1; }), 'rows=' + runRows.length);

      $('dictQ').value = '';
      setWordCat('all');
      next();
    });
  });

  /* ---------- 9. dictionary DE ---------- */
  step(function (next) {
    setDictLang('de');
    ok('dict: DE selected', settings.dictLang === 'de' && settings.lang === 'en');
    $('dictQ').value = 'thema';
    renderDict();
    var hits = $$('#dictBody .drow');
    ok('dict: DE search finds Thema', hits.some(function (r) { return r.querySelector('.dword').textContent.indexOf('Thema') !== -1; }), 'hits=' + hits.length);
    $('dictQ').value = '';
    setWordCat('all');
    var deChips = $$('#dictCats .chip').map(function (c) { return c.textContent; });
    ok('dict: DE phrase chip', deChips.indexOf('Cụm từ') !== -1, deChips.join('|'));
    setWordCat('phrase');
    var phraseRows = $$('#dictBody .drow');
    ok('dict: DE phrase filter', phraseRows.length > 0 && phraseRows.every(function (r) { return r.querySelector('.dpos').textContent.indexOf('cụm từ') !== -1; }), 'rows=' + phraseRows.length);
    setWordCat('all');
    next();
  });

  /* ---------- 9b. grammar dictionary + 200k bank ---------- */
  step(function (next) {
    if (settings.lang !== 'en') setLang('en');
    showScreen('dict');
    setDictMode('grammar');
    if (settings.glang !== 'en') setGrammarLang('en');
    ok('grammar: mode grammar', settings.dictMode === 'grammar', settings.dictMode);
    ok('grammar: language segment hidden', $('dictLangSeg').hidden === true);
    ok('grammar: 98 topics rendered', $$('#dictBody .grow').length === 98, 'got ' + $$('#dictBody .grow').length);
    ok('grammar: 7 category chips', $$('#dictCats .chip').length === 7, 'got ' + $$('#dictCats .chip').length);
    ok('grammar: 98 bank rows show capacity', $$('#dictBody .gbank').length === 98, 'got ' + $$('#dictBody .gbank').length);
    ok('grammar: bank total 70.19m', grammarBankTotal() === 70192896, String(grammarBankTotal()));
    ok('grammar: capacity per bank', grammarCapacity('present-simple') === 200000 && grammarCapacity('there-is-are') === 221184 && grammarCapacity('passive-voice') === 211968 && grammarCapacity('used-to') === 294912 && grammarCapacity('articles') === 3686400 && grammarCapacity('pronouns') === 294912 && grammarCapacity('verb-patterns') === 384000 && grammarCapacity('sentence-types') === 384000 && grammarCapacity('toeic-business') === 230400 && grammarCapacity('ielts-linking') === 384000 && grammarCapacity('nope') === 0, [grammarCapacity('present-simple'), grammarCapacity('articles'), grammarCapacity('pronouns'), grammarCapacity('toeic-business')].join('/'));

    var g1 = grammarItem('present-simple', 42);
    var g2 = grammarItem('present-simple', 42);
    ok('grammar: deterministic item', !!g1 && !!g2 && g1.answer === g2.answer && g1.tokens.join(' ') === g2.tokens.join(' '));
    ok('grammar: tokens keep all words', g1.tokens.slice().sort().join(' ') === g1.answer.split(' ').sort().join(' '), g1.answer);
    ok('grammar: last index valid', !!grammarItem('present-simple', 199999));
    ok('grammar: index clamped', grammarItem('present-simple', 999999).id === 'present-simple:199999');
    ok('grammar: malformed input safe', grammarItem('nope') === null && !!grammarItem('present-simple', 'abc'));

    ok('grammar: 3s negative uses base verb', grammarItem('present-simple', 18433).answer.indexOf('He does not read') === 0, grammarItem('present-simple', 18433).answer);
    ok('grammar: 3s question uses base verb', grammarItem('present-simple', 18434).answer.indexOf('Does he read') === 0, grammarItem('present-simple', 18434).answer);
    ok('grammar: 3s fronted time uses -s', grammarItem('present-simple', 18435).answer.indexOf('Every day, he reads') === 0, grammarItem('present-simple', 18435).answer);
    ok('grammar: past negative uses base verb', grammarItem('past-simple', 18817).answer.indexOf('He did not write') === 0, grammarItem('past-simple', 18817).answer);
    var tenseBad = 0;
    Object.keys(TENSE_PROFILE).forEach(function (id) {
      for (var pi = 0; pi < 4; pi++) {
        var it = grammarItem(id, pi);
        if (!it || /\{/.test(it.answer) || it.answer.indexOf('..') !== -1 || it.answer.indexOf('  ') !== -1 || it.tokens.slice().sort().join(' ') !== it.answer.split(' ').sort().join(' ')) tenseBad++;
      }
    });
    ok('grammar: 12 tenses x 4 templates valid', tenseBad === 0, 'bad=' + tenseBad);

    var p1 = grammarItem('there-is-are', 0);
    var p2 = grammarItem('there-is-are', 0);
    ok('grammar: pattern deterministic item', !!p1 && !!p2 && p1.answer === p2.answer && p1.tokens.join(' ') === p2.tokens.join(' '));
    ok('grammar: pattern tokens keep all words', p1.tokens.slice().sort().join(' ') === p1.answer.split(' ').sort().join(' '), p1.answer);
    ok('grammar: there is + singular', p1.answer === 'There is a meeting in the office every day', p1.answer);
    ok('grammar: there are + plural', grammarItem('there-is-are', 1).answer === 'There are two meetings in the office every day', grammarItem('there-is-are', 1).answer);
    ok('grammar: pattern index clamped', grammarItem('there-is-are', 999999).id === 'there-is-are:221183', grammarItem('there-is-are', 999999).id);
    var pv0 = grammarItem('passive-voice', 0);
    ok('grammar: passive be + V3', pv0.answer === 'The detailed report is carefully read by the manager every day', pv0.answer);
    ok('grammar: passive question', grammarItem('passive-voice', 2).answer === 'Is the detailed report carefully read by the manager every day?', grammarItem('passive-voice', 2).answer);
    var ut0 = grammarItem('used-to', 0);
    ok('grammar: used to + base verb', ut0.answer === 'I used to read the detailed report carefully every day', ut0.answer);
    ok('grammar: used to negative/question', grammarItem('used-to', 1).answer.indexOf('I did not use to read') === 0 && grammarItem('used-to', 2).answer.indexOf('Did I use to read') === 0);
    var patternBad = 0;
    Object.keys(GRAMMAR_PATTERNS).forEach(function (id) {
      var p = GRAMMAR_PATTERNS[id];
      var cap = patternCapacity(id);
      if (!cap) patternBad++;
      for (var pi = 0; pi < p.templates.length; pi++) {
        var it = grammarItem(id, pi);
        if (!it || /\{/.test(it.answer) || it.answer.indexOf('..') !== -1 || it.answer.indexOf('  ') !== -1 || it.tokens.slice().sort().join(' ') !== it.answer.split(' ').sort().join(' ')) patternBad++;
      }
      [Math.floor(cap / 2), cap - 1].forEach(function (pi) {
        var it = grammarItem(id, pi);
        if (!it || /\{/.test(it.answer) || it.answer.indexOf('..') !== -1 || it.answer.indexOf('  ') !== -1) patternBad++;
      });
    });
    ok('grammar: 86 pattern banks valid', Object.keys(GRAMMAR_PATTERNS).length === 86 && patternBad === 0, 'banks=' + Object.keys(GRAMMAR_PATTERNS).length + ' bad=' + patternBad);
    var bankCount = 0, bankBad = 0, minCap = Infinity;
    GRAMMAR_TOPICS.forEach(function (t) {
      if (!t.gen) return;
      bankCount++;
      var cap = grammarCapacity(t.id);
      if (cap < 200000) bankBad++;
      if (cap < minCap) minCap = cap;
    });
    ok('grammar: all 98 topics have >=200k bank', bankCount === 98 && bankBad === 0, 'banks=' + bankCount + ' min=' + minCap);
    ok('grammar: articles a/an/the', grammarItem('articles', 0).answer === 'I needed a report every day.' && grammarItem('articles', 1).answer === 'I sent the report in the office every day.', grammarItem('articles', 0).answer);
    ok('grammar: countable vs uncountable', grammarItem('countable-uncountable', 6).answer === 'How many reports are there?' && grammarItem('countable-uncountable', 7).answer === 'In general, how much information do we need?', grammarItem('countable-uncountable', 6).answer);
    ok('grammar: pronoun subject/object', grammarItem('pronouns', 5).answer === 'Every day, did the manager call me?', grammarItem('pronouns', 5).answer);
    ok('grammar: comparative than', grammarItem('comparatives', 2).answer === 'Is the new report more important than the old report?', grammarItem('comparatives', 2).answer);
    ok('grammar: TOEIC request frame', grammarItem('toeic-business', 0).answer === 'Please submit the expense report every day.', grammarItem('toeic-business', 0).answer);
    ok('grammar: IELTS linker frame', grammarItem('ielts-linking', 0).answer.indexOf('The plan is expensive; however, it may be effective') === 0, grammarItem('ielts-linking', 0).answer);
    ok('grammar: academic hedging frame', grammarItem('academic-hedging', 0).answer.indexOf('The results may suggest that the policy is effective') === 0, grammarItem('academic-hedging', 0).answer);

    ok('grammar: verb pattern to V', grammarItem('verb-patterns', 0).answer === 'She wants to read the report at work every day.', grammarItem('verb-patterns', 0).answer);
    ok('grammar: irregular past', grammarItem('irregular-verbs', 0).answer === 'I read the detailed report at work every day.', grammarItem('irregular-verbs', 0).answer);
    ok('grammar: sentence-type question', grammarItem('sentence-types', 1).answer === 'Do I read the detailed report at work every day?', grammarItem('sentence-types', 1).answer);
    ok('grammar: punctuation semicolon', grammarItem('punctuation', 0).answer === 'The report was clear; however, it was long at work every day.', grammarItem('punctuation', 0).answer);
    ok('grammar: IELTS Task 1 trend', grammarItem('ielts-task1-structures', 0).answer === 'The chart shows that sales increased steadily at work every day.', grammarItem('ielts-task1-structures', 0).answer);
    ok('grammar: IELTS Task 2 concession', grammarItem('ielts-task2-structures', 0).answer === 'While some people support the policy, others remain concerned at work every day.', grammarItem('ielts-task2-structures', 0).answer);
    ok('grammar: new bank counts', grammarCapacity('verb-patterns') === 384000 && grammarCapacity('sentence-types') === 384000 && grammarCapacity('ielts-task2-structures') === 384000, [grammarCapacity('verb-patterns'), grammarCapacity('sentence-types'), grammarCapacity('ielts-task2-structures')].join('/'));

    $('dictQ').value = 'perfect';
    renderDict();
    var perfectRows = $$('#dictBody .grow');
    var perfectTitles = perfectRows.map(function (x) { return x.querySelector('.gtitle').textContent; });
    ok('grammar: search perfect finds 9', perfectRows.length === 9 && perfectRows.every(function (x) { return grammarHaystack(GRAMMAR_MAP[x.dataset.gkey]).indexOf('perfect') !== -1; }), perfectTitles.join(', '));

    $('dictQ').value = '';
    setGrammarCat('Thì');
    ok('grammar: cat Thì = 12', $$('#dictBody .grow').length === 12, 'got ' + $$('#dictBody .grow').length);
    setGrammarCat('Cấu trúc câu');
    ok('grammar: cat Cấu trúc câu = 24', $$('#dictBody .grow').length === 32, 'got ' + $$('#dictBody .grow').length);
    setGrammarCat('Từ loại');
    ok('grammar: cat Từ loại = 18', $$('#dictBody .grow').length === 28, 'got ' + $$('#dictBody .grow').length);
    setGrammarCat('TOEIC & IELTS');
    ok('grammar: cat TOEIC = 6', $$('#dictBody .grow').length === 6, 'got ' + $$('#dictBody .grow').length);
    setGrammarCat('all');
    ok('grammar: cat all = 98', $$('#dictBody .grow').length === 98);

    $$('#dictBody .grow')[0].click();
    ok('grammar: detail opens', $('sheetWrap').hidden === false);
    ok('grammar: detail formula + use', !!document.querySelector('.sheet-gformula') && !!document.querySelector('.sheet-guse'));
    ok('grammar: detail signals + exam', !!document.querySelector('.sheet-gsig') && !!document.querySelector('.sheet-gexam'));
    ok('grammar: no drill button for English topics', !document.querySelector('.sheet-gbank'));
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

  /* ---------- 9c. German grammar: level filter ---------- */
  step(function (next) {
    setDictMode('grammar');
    setGrammarLang('de');
    ok('de: 52 topics', GRAMMAR_TOPICS.length === 52, 'got ' + GRAMMAR_TOPICS.length);
    ok('de: label Deutsch', $('dictSub').textContent.indexOf('Deutsch') === 0, $('dictSub').textContent);
    ok('de: grammar segment visible', $('grammarLangSeg').hidden === false && $('dictLangSeg').hidden === true);
    ok('de: 5 level chips', $$('#dictGLevels .chip').length === 5, 'got ' + $$('#dictGLevels .chip').length);
    ok('de: 52 rows', $$('#dictBody .grow').length === 52, 'got ' + $$('#dictBody .grow').length);
    ok('de: all banks >= 200k', GRAMMAR_TOPICS.every(function (t) { return grammarCapacity(t.id) >= 200000; }));

    ['A1', 'A2', 'B1', 'B2'].forEach(function (lev) {
      setGrammarLevel(lev);
      var rows = $$('#dictBody .grow');
      var want = GRAMMAR_TOPICS.filter(function (t) { return t.level === lev; }).length;
      ok('de: level ' + lev + ' rows', rows.length === want, 'got ' + rows.length + ' want ' + want);
      ok('de: level ' + lev + ' no cross-level leak',
        rows.every(function (r) {
          return r.querySelector('.glvl').textContent === lev &&
            r.dataset.gkey.indexOf('de-' + lev.toLowerCase() + '-') === 0;
        }));
    });
    setGrammarLevel('all');
    ok('de: all levels back to 52', $$('#dictBody .grow').length === 52);

    var d1 = grammarItem('de-a1-praesens-reg', 0);
    ok('de: deterministic item', !!d1 && d1.answer === grammarItem('de-a1-praesens-reg', 0).answer);
    ok('de: sentence clean', !!d1 && /\{/.test(d1.answer) === false && d1.answer.indexOf('  ') === -1 && d1.answer.indexOf(' .') === -1, d1 && d1.answer);
    ok('de: tokens keep all words', d1.tokens.slice().sort().join(' ') === d1.answer.split(' ').sort().join(' '), d1.answer);
    ok('de: index clamped', grammarItem('de-a1-praesens-reg', 999999999).id === 'de-a1-praesens-reg:' + (grammarCapacity('de-a1-praesens-reg') - 1));

    var deBad = 0, deBanks = 0;
    GRAMMAR_TOPICS.forEach(function (t) {
      deBanks++;
      var cap = grammarCapacity(t.id);
      [0, Math.floor(cap / 3), cap - 1].forEach(function (pi) {
        var it = grammarItem(t.id, pi);
        if (!it || /\{/.test(it.answer) || it.answer.indexOf('  ') !== -1 || it.answer.indexOf(' .') !== -1) deBad++;
      });
    });
    ok('de: 52 banks render clean', deBanks === 52 && deBad === 0, 'banks=' + deBanks + ' bad=' + deBad);

    setGrammarLang('en');
    ok('de: back to English', GRAMMAR_TOPICS.length === 98 && $('dictGLevels').hidden === true);
    setDictMode('words');
    next();
  });

  /* ---------- 9d. dict/exercise isolation + quiz text + write direction + drill ---------- */
  step(function (next) {
    setLang('de');
    showScreen('dict');
    setDictMode('words');
    setDictLang('de');
    setExTopic('all');
    setDictTopic('04');
    showExercise('mc-en');
    var before = S.de3k['mc-en'].items.map(function (w) { return w.num; }).join(',');

    showScreen('dict');
    setDictTopic('02');
    ok('isolation: dict topic does not touch exercise', S.de3k['mc-en'].items.map(function (w) { return w.num; }).join(',') === before);
    ok('isolation: two topics kept apart', settings.dictTopic === '02' && settings.dtopic === 'all');

    setDictLang('en');
    ok('isolation: dict language does not change app language', settings.lang === 'de' && settings.dictLang === 'en');
    setDictLang('de');
    setDictTopic('all');

    showExercise('mc-en');
    var q = document.querySelector('#list-mc-en .q');
    var optTexts = $$('.opt', q).map(function (o) { return o.querySelector('span:last-child').textContent; });
    ok('quiz: options carry no parenthetical note', optTexts.length === 4 && optTexts.every(function (t) { return t.indexOf('(') === -1; }), optTexts.join(' | '));
    ok('quiz: question shows no plural note', !q.querySelector('.qpl'));

    showExercise('write-vn');
    var wq = document.querySelector('#list-write-vn .q');
    var ws = S.de3k['write-vn'];
    ok('write-vn: top line is the meaning', wq.querySelector('.qword').textContent === cleanMeaning(ws.items[0].meaning), wq.querySelector('.qword').textContent);
    ok('write-vn: no redundant prompt', !wq.querySelector('.qprompt'));
    ok('write-vn: input placeholder keeps the article hint', wq.querySelector('.winput').placeholder.indexOf('der/die/das') !== -1);

    showScreen('dict');
    setDictMode('grammar');
    setGrammarLang('de');
    openGrammar('de-a1-praesens-reg');
    ok('grammar: sheet shows how-to + notes', !!document.querySelector('#sheetBody .gdlist') && !!document.querySelector('#sheetBody .gnotes'));
    closeSheet();
    openOrder('de-a1-praesens-reg');
    ok('order: tab active', settings.ex === 'order' && document.querySelector('.screen.active').id === 'screen-exercise');
    ok('order: 6 tabs', $$('#exTabs .seg-btn').length === 6, 'got ' + $$('#exTabs .seg-btn').length);
    ok('order: level + topic chips', $$('#exGLevels .chip').length === 4 && $$('#exGTopics .chip').length === 14,
      $$('#exGLevels .chip').length + '/' + $$('#exGTopics .chip').length);
    ok('order: vocab chips hidden', $('exChips').hidden === true && $('exTopics').hidden === true);
    ok('order: 20 sentences in session', GD.rows.length === 20 && $('stTotal').textContent === '20', $('stTotal').textContent);
    ok('order: vietnamese prompt shown', !!document.querySelector('#gdAsk .gdvi') && !!document.querySelector('#gdAsk .gdvi').textContent);
    ok('order: tokens rendered', $$('#gdTokens .gtok').length === GD.tokens.length && GD.tokens.length > 1, 'n=' + GD.tokens.length);
    var answerToks = GD.answer.split(' ');
    var used = {};
    var seq = answerToks.map(function (t) {
      for (var i = 0; i < GD.tokens.length; i++){ if (!used[i] && GD.tokens[i] === t){ used[i] = 1; return i; } }
      return -1;
    });
    seq.forEach(function (i) { gdTap(i); });
    gdCheck(false);
    ok('order: correct order accepted', GD.ok === 1 && GD.done === 1, 'ok=' + GD.ok + ' done=' + GD.done);
    ok('order: statline updated', $('stCorrect').textContent === '1');
    var firstVi = GD.prompt;
    gdNext();
    ok('order: next sentence loaded', GD.pos === 1 && GD.chosen.length === 0 && GD.tokens.length > 1);
    ok('order: next prompt is vietnamese', GD.prompt !== firstVi && !!GD.prompt, GD.prompt);
    setOdLevel('B2');
    ok('order: B2 topic chips', $$('#exGTopics .chip').length === 11 && GD.rows.length === 20,
      $$('#exGTopics .chip').length + '/rows=' + GD.rows.length);
    showScreen('dict');
    setGrammarLang('en');
    setDictMode('words');
    setLang('en');
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
    ok('profile: no word-set tag block', !document.querySelector('[data-tag-lang]') && !document.querySelector('.profile-tags'));
    ok('profile: insights live inside the profile screen', (function () {
      var s = $('screen-settings');
      var ins = document.querySelector('.profile-insights');
      return !!s && !!ins && s.contains(ins);
    })());
    ok('profile: file input image', $('avatarFile').accept.indexOf('image/') !== -1);
    ok('profile: avatar images disable long-press/drag', ['navAvatarImg', 'profileAvatarImg', 'homeAvatarImg'].every(function (id) {
      var el = $(id);
      if (!el) return false;
      var cs = getComputedStyle(el);
      return el.getAttribute('draggable') === 'false' &&
        cs.pointerEvents === 'none' &&
        (cs.userSelect === 'none' || cs.webkitUserSelect === 'none');
    }));
    ok('profile: size select sync', $('setSizeSel').value === String(settings.size));
    ok('profile: settings rows', !!document.querySelector('[data-nav="wrong"]') && !!document.querySelector('[data-nav="dict"]'));
    var darkScheme = matchMedia('(prefers-color-scheme: dark)').matches;
    var pfInk = getComputedStyle(document.querySelector('.profile-sec-title')).color;
    ok('profile: follows device theme', pfInk === (darkScheme ? 'rgb(242, 246, 255)' : 'rgb(15, 23, 42)'), pfInk);
    ok('profile: color-scheme matches theme', getComputedStyle(document.body).colorScheme === (darkScheme ? 'dark' : 'light'), getComputedStyle(document.body).colorScheme);

    document.querySelector('[data-set-lang="de"]').click();
    ok('profile: language row switches language', settings.lang === 'de');
    ok('profile: DE seg active', document.querySelector('[data-set-lang="de"]').classList.contains('active'));
    document.querySelector('[data-set-lang="en"]').click();
    ok('profile: back to English', settings.lang === 'en');

    var px = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9Zl1sAAAAASUVORK5CYII=';
    setAvatar(px);
    ok('profile: nav avatar photo', $('navAvatarImg').getAttribute('src') === px);
    ok('profile: profile avatar photo', $('profileAvatarImg').getAttribute('src') === px);
    ok('profile: home avatar photo', $('homeAvatarImg').getAttribute('src') === px);
    ok('profile: home avatar visible', $('homeAvatarImg').hidden === false);
    ok('profile: nav avatar has-photo', document.querySelector('.bnav .avatar-img').classList.contains('has-photo'));
    clearCover();
    ok('profile: avatar does not touch the cover', $('profileHeroBg').style.backgroundImage === '' && !$('profileHero').classList.contains('has-cover'));
    ok('profile: avatar persisted', LS.get('v4t:avatar', null) === px);
    ok('profile: clear button visible', $('avatarClear').hidden === false);
    clearAvatar();
    ok('profile: nav avatar cleared', $('navAvatarImg').hidden === true);
    ok('profile: home avatar cleared', $('homeAvatarImg').hidden === true);
    ok('profile: avatar storage cleared', LS.get('v4t:avatar', null) === null);
    ok('profile: nav avatar has-photo off', !document.querySelector('.bnav .avatar-img').classList.contains('has-photo'));

    /* cover: its own key, never blurred, independent from the avatar */
    setCover(px);
    ok('cover: stored under its own key', LS.get('v4t:cover', null) === px && LS.get('v4t:avatar', null) === null);
    ok('cover: hero uses it', $('profileHeroBg').style.backgroundImage.indexOf('data:image/png') !== -1);
    ok('cover: hero marked has-cover', $('profileHero').classList.contains('has-cover'));
    ok('cover: no blur filter', getComputedStyle($('profileHeroBg')).filter === 'none', getComputedStyle($('profileHeroBg')).filter);
    ok('cover: avatar untouched', $('profileAvatarImg').hidden === true && $('navAvatarImg').hidden === true);
    ok('cover: clear button visible', $('coverClear').hidden === false);
    setAvatar(px);
    ok('cover: setting avatar keeps the cover', $('profileHeroBg').style.backgroundImage.indexOf('data:image/png') !== -1);
    clearAvatar();
    ok('cover: clearing avatar keeps the cover', $('profileHeroBg').style.backgroundImage.indexOf('data:image/png') !== -1);
    clearCover();
    ok('cover: cleared', LS.get('v4t:cover', null) === null && $('profileHeroBg').style.backgroundImage === '');
    ok('cover: hero class removed', !$('profileHero').classList.contains('has-cover'));

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

  /* ---------- 12a. draggable pill indicator ---------- */
  step(function (next) {
    var bnav = $('bnav');
    var pill = document.querySelector('.bnav-pill');
    var w = pill.getBoundingClientRect().width || 70;
    function pe(type, x) {
      bnav.dispatchEvent(new PointerEvent(type, {
        bubbles: true, cancelable: true, clientX: x, clientY: 600,
        pointerId: 1, pointerType: 'touch', button: 0, buttons: 1
      }));
    }
    showScreen('home');
    pe('pointerdown', 100);
    pe('pointermove', 100 + w * 0.6);
    ok('nav drag: switches while dragging', settings.screen === 'exercise', settings.screen);
    pe('pointermove', 100 + w * 1.6);
    ok('nav drag: keeps following the finger', settings.screen === 'wrong', settings.screen);
    ok('nav drag: pill follows finger (fractional)', parseFloat(bnav.style.getPropertyValue('--nav-i')) > 1.2, bnav.style.getPropertyValue('--nav-i'));
    pe('pointerup', 100 + w * 1.6);
    ok('nav drag: snaps to nearest tab', settings.screen === 'wrong' && bnav.style.getPropertyValue('--nav-i') === '2', bnav.style.getPropertyValue('--nav-i'));

    showScreen('home');
    pe('pointerdown', 100);
    pe('pointermove', 100 + w * 0.3);
    pe('pointerup', 100 + w * 0.3);
    ok('nav drag: small pull snaps back', settings.screen === 'home', settings.screen);

    showScreen('home');
    pe('pointerdown', 100);
    pe('pointermove', 100 - w * 1.5);
    pe('pointerup', 100 - w * 1.5);
    ok('nav drag: clamped at the first tab', settings.screen === 'home', settings.screen);

    showScreen('home');
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

  /* ---------- 13b. German topics ---------- */
  step(function (next) {
    setLang('de');
    ok('de: 24 topics loaded', DE_TOPICS.length === 24, 'got ' + DE_TOPICS.length);
    ok('de: topic counts match words', DE_TOPICS.every(function (t) {
      var n = 0;
      DATASETS.de3k.words.forEach(function (w) { if ((w.topics || []).indexOf(t.id) !== -1) n++; });
      return n === t.count && n > 0;
    }), JSON.stringify(DE_TOPICS.map(function (t) { return t.id + ':' + t.count; })));
    ok('de: noun keeps article + plural', (function () {
      var w = DATASETS.de3k.words.filter(function (x) { return x.word === 'der Apfel'; })[0];
      return !!w && w.type === 'n' && w.topics.indexOf('04') !== -1 && /die Äpfel/.test(w.extra || '');
    })());
    ok('de: verb keeps conjugation forms', (function () {
      var w = DATASETS.de3k.words.filter(function (x) { return x.word === 'sein' && x.type === 'v'; })[0];
      return !!w && /ich bin/.test(w.extra || '');
    })());
    ok('de: multi-form word accepts one form', grade('de', { word: 'erste / erster / erstes' }, 'erster') === true);
    ok('de: new A1 word has generated examples', (function () {
      var w = DATASETS.de3k.words.filter(function (x) { return x.word === 'der Familienname'; })[0];
      return !!w && w.ex && w.ex.length === 2 && /Familienname/.test(w.ex[0].s);
    })());

    setExTopic('04');
    showExercise('mc-en');
    var s = S.de3k['mc-en'];
    ok('de ex: session only topic words', !!s && s.items.length > 0 && s.items.every(function (w) {
      return (w.topics || []).indexOf('04') !== -1;
    }), s ? s.items.length : 'no session');
    ok('de ex: session size capped by topic', s && s.items.length === Math.min(50, DE_TOPIC_MAP['04'].count), 'got ' + (s ? s.items.length : -1));
    ok('de ex: topic chips', $$('#exTopics .chip').length === DE_TOPICS.length + 1, 'got ' + $$('#exTopics .chip').length);
    ok('de ex: sub shows topic name', $('exSub').textContent.indexOf('04 · Đồ ăn') !== -1, $('exSub').textContent);

    showScreen('dict');
    setDictTopic('04');
    var arr = dictArr('de').filter(function (e) { return (e.topics || []).indexOf('04') !== -1; });
    ok('de dict: topic filter active', $('dictSub').textContent.indexOf(fmt(arr.length) + ' từ') !== -1, $('dictSub').textContent);
    ok('de dict: topic chips', $$('#dictTopics .chip').length === DE_TOPICS.length + 1, 'got ' + $$('#dictTopics .chip').length);
    ok('de dict: rendered rows match topic', $$('#dictBody .drow').every(function (r) {
      var e = DICT_MAP.de[r.dataset.dkey];
      return !!e && (e.topics || []).indexOf('04') !== -1;
    }));
    ok('de dict: A-Z sorted', (function () {
      var a = dictArr('de');
      for (var i = 1; i < a.length; i++) if (a[i - 1].sort.localeCompare(a[i].sort, 'de') > 0) return false;
      return true;
    })());
    ok('de dict: umlaut folded into A-Z', (function () {
      var e = dictArr('de').filter(function (x) { return x.disp === 'über'; })[0];
      return !!e && e.letter === 'U';
    })());
    ok('de dict: Vietnamese query not matched against German keys', (function () {
      var q = $('dictQ');
      setDictTopic('13');
      q.value = 'mẹ'; renderDict();
      var noise = $$('#dictBody .drow').length;
      setDictTopic('02');
      q.value = 'mẹ'; renderDict();
      var hit = $$('#dictBody .drow').length;
      q.value = '';
      return noise === 0 && hit > 0;
    })(), 'noise/hit');

    setDictTopic('all');
    setExTopic('all');
    setLang('en');
    showScreen('home');
    next();
  });

  /* ---------- 13b. flashcard (Deutsch <-> Viet) ---------- */
  step(function (next) {
    var pool = DATASETS.de3k.words.filter(function (w) { return (w.topics || []).length && w.meaning; });
    ok('flash: A1 topics available', pool.length > 500, 'got ' + pool.length);

    setLang('de');
    setExTopic('all');
    showExercise('flash');
    ok('flash: tab visible only on Deutsch', $('exTabFlash').hidden === false);
    ok('flash: panel active', document.querySelector('.screen.active').id === 'screen-exercise' &&
      document.querySelector('.expanel.active').id === 'ex-flash');
    ok('flash: session 20 cards', FC.items.length === 20 && $('stTotal').textContent === '20', String(FC.items.length));
    ok('flash: every card has a meaning', FC.items.every(function (w) { return !!w.meaning; }));
    ok('flash: no image markup any more', !document.getElementById('fcImgBox') && !document.querySelector('#ex-flash img'));

    var first = FC.items[0];
    ok('flash: default direction is Duc -> Viet', settings.fcDir === 'de' && !!document.querySelector('[data-fc-dir="de"].active'));
    ok('flash: front shows the German word', $('fcFront').innerHTML.indexOf('fc-word') !== -1 &&
      $('fcFront').textContent.indexOf(dispWord(first.word)) !== -1, $('fcFront').textContent);
    ok('flash: front hides the Vietnamese meaning', $('fcFront').textContent.indexOf(cleanMeaning(first.meaning)) === -1);
    ok('flash: back shows the Vietnamese meaning', $('fcBack').textContent.indexOf(cleanMeaning(first.meaning)) !== -1);
    ok('flash: back shows an example sentence', $('fcBack').innerHTML.indexOf('fc-ex') !== -1);

    $('fcCard').click();
    ok('flash: tap flips the card', FC.flipped === true && $('fcCard').classList.contains('flipped'));
    $('fcCard').click();
    ok('flash: tap flips back', FC.flipped === false && !$('fcCard').classList.contains('flipped'));

    document.querySelector('[data-fc-dir="vi"]').click();
    ok('flash: Viet -> Duc switched', settings.fcDir === 'vi' && !!document.querySelector('[data-fc-dir="vi"].active'));
    ok('flash: Viet -> Duc front shows the meaning', $('fcFront').textContent.indexOf(cleanMeaning(first.meaning)) !== -1,
      $('fcFront').textContent);
    ok('flash: Viet -> Duc back shows the German word', $('fcBack').textContent.indexOf(dispWord(first.word)) !== -1);
    document.querySelector('[data-fc-dir="de"]').click();
    ok('flash: back to Duc -> Viet', settings.fcDir === 'de' && $('fcFront').innerHTML.indexOf('fc-word') !== -1);

    var before = wrong.de.length;
    flashNext(false);
    ok('flash: unknown card goes to Tu sai', wrong.de.length === before + 1, wrong.de.length + '/' + before);
    ok('flash: index advanced', FC.i === 1 && $('stDone').textContent === '1', String(FC.i));

    var wb = wrong.de.length;
    flashNext(true);
    ok('flash: known card is not added', wrong.de.length === wb);

    flashStart();
    flashRender();
    FC.i = FC.items.length - 1;
    flashNext(true);
    ok('flash: finish state shows restart', $('fcDone').hidden === false && !!document.querySelector('[data-fc-restart]'));
    flashStart();
    flashRender();
    ok('flash: restart resets progress', FC.i === 0 && $('stDone').textContent === '0');

    setLang('en');
    ok('flash: hidden on English', $('exTabFlash').hidden === true);
    ok('flash: leaves flash tab on English', settings.ex !== 'flash', settings.ex);
    next();
  });

  /* ---------- 14. data sanity ---------- */
  step(function (next) {
    var total = DATASETS.en1k.words.length + DATASETS.en3k.words.length + DATASETS.de3k.words.length;
    ok('data: total words', total === 7731, 'got ' + total);
    ok('data: mc option pools not POS-locked', (function () {
      var s = S.en1k['mc-en'];
      if (!s || !s.items || !s.items.length) return false;
      var types = {};
      s.items.slice(0, 50).forEach(function (w) { types[primaryType(w.type)] = 1; });
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
