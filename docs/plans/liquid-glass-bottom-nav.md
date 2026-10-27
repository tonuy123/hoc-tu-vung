# Liquid Glass Bottom Navigation — Implementation Plan

**Status:** implemented + pushed (2026-10-27)
**Final pass:** exact Superdesign v6 nav — neutral glass `rgba(30,30,30,.45)`, blur 10px, bottom 34px, five icons Home · Play · Heart · Search · Avatar. Avatar opens the theme-aware glass **Hồ sơ** (profile — dark navy/lime on dark devices, light glass on light devices) with device avatar upload, nav avatar sync, EN/DE and settings. 137/137 tests. The "App port" suggestions below were the first draft and are superseded by this final pass.
**Target:** `hoc-tu-vung` single-file app (`src/template.html` → `index.html`)  
**Source:** Superdesign project `5369c3ed-1fde-4aa6-8429-9c5e0af21562`, draft `72a309a0-ac54-4b3e-b7cc-730f966110ba`, version **v6**  
**Preview:** https://p.superdesign.dev/draft/72a309a0-ac54-4b3e-b7cc-730f966110ba  
**References:** [`assets/liquid-glass-nav.png`](assets/liquid-glass-nav.png) · [`assets/liquid-glass-nav.reference.html`](assets/liquid-glass-nav.reference.html)

> The reference HTML uses Tailwind, Iconify and the Satoshi font from CDNs. This app is an **offline single-file** app, so none of those dependencies are shipped. The plan ports the nav's visual language with vanilla CSS and the existing inline SVG icons.

---

## 1. Design DNA to port

| Element | Superdesign v6 | App port |
|---|---|---|
| Bar fill | `rgba(30,30,30,.45)` | `rgba(18,26,42,.58)` — navy-tinted glass so it belongs to the app palette |
| Backdrop | `blur(10px) saturate(180%)` | same; **10px, not the old 18px** |
| Border | `1px solid rgba(255,255,255,.10)` | same |
| Shadow | `0 8px 32px rgba(0,0,0,.3)` + inset highlights | same |
| Pill | 20% width, top/bottom 8px, `translateX(index*100%)` | same; index driven by `--nav-i` |
| Pill fill | `rgba(255,255,255,.15)` | same |
| Pill blur | `blur(8px)` | same (progressive enhancement) |
| Pill glow | `0 0 20px rgba(0,240,255,.15)` + inset highlight | same |
| Pill motion | `.5s cubic-bezier(.34,1.56,.64,1)` | same |
| Active icon | warm `drop-shadow(0 0 12px rgba(255,230,150,.8))` | `10px` warm glow, slightly softer |
| Badge | `#ff2d55`, 2px border, `softPulse` 2s | same; border matches the glass bar |
| Bar size | `68px`, `max-width:380px`, floating | same |
| Refraction beam | removed in v6 | **do not add** |
| Demo page (hero, cards, background texture, view-transition) | reference only | **out of scope** — only the nav changes |

## 2. Mapping to the app's 5 slots

The app has 5 tabs but not the demo's home/play/heart/search/profile:

| Slot | Current item | New visual | Active behavior |
|---|---|---|---|
| 0 | `EN` language | text monogram, 12.5px | small blue glow dot below; no pill |
| 1 | `DE` language | text monogram, 12.5px | small blue glow dot below; no pill |
| 2 | Home | house SVG | **pill** |
| 3 | Từ điển | magnifier SVG | **pill** |
| 4 | Từ sai | circular avatar + count badge | **pill**; red pulse badge |

- The pill represents the **screen**, not the language. It moves only between slots 2/3/4.
- Tapping `EN`/`DE` switches language and updates the dot; the pill stays on the current screen.
- During **wrong-word practice** (`CUR_DS === 'wrong'` while `settings.screen === 'exercise'`), highlight slot 4 (`Từ sai` avatar) instead of Home. This is more truthful than the current "Home for every exercise" behavior and matches the nav semantics.
- Normal exercise screens (1k/3k questions) keep the pill on Home.

## 3. Current code map

| Area | Location | Change |
|---|---|---|
| Content bottom padding | `src/template.html:29`, `:234` | increase for the floating 68px bar |
| Nav CSS | `src/template.html:219-230` | replace `.bnav` block, add pill/item/badge/dot/keyframes |
| Nav HTML | `src/template.html:403-416` | add pill element, `.bnav-item`, `.ico` wrappers, ARIA |
| `updateNav()` | `src/template.html:653-661` | compute `--nav-i`, ARIA, wrong-count label |
| `rerender()` / `showScreen()` / `practiceWrong()` | `:1093`, `:1197`, `:1264` | no logic change needed; they already call `updateNav()` |
| Init | `src/template.html` end of script | add `.is-ready` after first paint to avoid a load animation |
| Tests | `tests/page-tests.js:43-45`, `:88`; `tests/run-cdp.js` mobile block | add pill/index/language/badge/reduced-motion assertions |
| Build | `python tools/build.py` | rebuild only; never edit `index.html` |

## 4. Proposed CSS (replace `.bnav` block)

```css
/* ---------- liquid glass bottom nav ---------- */
.bnav{
  position:fixed; left:50%; bottom:calc(22px + env(safe-area-inset-bottom));
  transform:translateX(-50%); z-index:70;
  width:min(calc(100vw - 32px), 380px); height:68px;
  display:flex; align-items:center; padding:0; overflow:hidden;
  border-radius:999px;
  background:rgba(18,26,42,.58);
  backdrop-filter:blur(10px) saturate(180%);
  -webkit-backdrop-filter:blur(10px) saturate(180%);
  border:1px solid rgba(255,255,255,.10);
  box-shadow:
    0 8px 32px rgba(0,0,0,.35),
    inset 0 1px 1px rgba(255,255,255,.05),
    inset 0 -1px 1px rgba(255,255,255,.02);
}
.bnav-pill{
  position:absolute; top:8px; bottom:8px; left:0; width:20%;
  border-radius:999px;
  background:rgba(255,255,255,.15);
  backdrop-filter:blur(8px); -webkit-backdrop-filter:blur(8px);
  border:1px solid rgba(255,255,255,.08);
  box-shadow:inset 0 1px 4px rgba(255,255,255,.10), 0 0 20px rgba(0,240,255,.15);
  transform:translateX(calc(var(--nav-i, 2) * 100%));
  transition:transform .5s cubic-bezier(.34,1.56,.64,1);
  will-change:transform; pointer-events:none; z-index:2;
}
.bnav:not(.is-ready) .bnav-pill{transition:none}

.bnav-item{
  position:relative; z-index:3; flex:1 1 0;
  height:52px; display:flex; align-items:center; justify-content:center;
  border:0; background:transparent; border-radius:999px; cursor:pointer;
  color:rgba(230,237,247,.62); -webkit-tap-highlight-color:transparent;
}
.bnav-item svg{width:25px;height:25px;display:block;transition:color .2s,filter .2s}
.bnav-item:hover{color:#fff}
.bnav-item.active{color:#fff}
.bnav-item.active svg{filter:drop-shadow(0 0 10px rgba(255,230,150,.72))}
.bnav-item .ico{position:relative;display:inline-flex}

/* language toggles: no second pill, only a small dot */
.bnav .lang{font-size:12.5px;font-weight:800;letter-spacing:.5px}
.bnav .lang.on{color:#fff}
.bnav .lang.on::after{
  content:''; position:absolute; left:50%; bottom:9px;
  width:4px; height:4px; margin-left:-2px; border-radius:50%;
  background:var(--accent); box-shadow:0 0 8px var(--accent);
}

/* wrong-word badge */
.bnav .badge{
  position:absolute; top:-6px; right:-10px;
  min-width:18px; height:18px; padding:0 5px; border-radius:999px;
  background:#ff2d55; color:#fff; font-size:10px; font-weight:800;
  line-height:14px; text-align:center;
  border:2px solid rgba(18,26,42,.94);
  box-shadow:0 2px 8px rgba(0,0,0,.3);
  animation:softPulse 2s infinite ease-in-out;
}
@keyframes softPulse{
  0%,100%{transform:scale(1);opacity:1}
  50%{transform:scale(1.1);opacity:.9}
}

/* fallback when backdrop-filter is unavailable */
@supports not ((backdrop-filter:blur(1px)) or (-webkit-backdrop-filter:blur(1px))){
  .bnav{background:rgba(15,24,40,.94)}
  .bnav-pill{background:rgba(255,255,255,.17)}
}

@media (prefers-reduced-motion:reduce){
  .bnav-pill{transition:none}
  .bnav .badge{animation:none}
}
```

Content padding: `.wrap` → `calc(116px + env(safe-area-inset-bottom))`; mobile media query → same or `calc(112px + env(...))`. The bar top is `22 + 68 = 90px`; 112–116px leaves 22–26px clearance.

## 5. Proposed HTML

```html
<nav class="bnav" id="bnav" aria-label="Điều hướng chính">
  <span class="bnav-pill" aria-hidden="true"></span>

  <button type="button" class="bnav-item lang" data-lang="en" aria-label="Tiếng Anh" aria-pressed="true">EN</button>
  <button type="button" class="bnav-item lang" data-lang="de" aria-label="Tiếng Đức" aria-pressed="false">DE</button>

  <button type="button" class="bnav-item nav" data-nav="home" aria-label="Trang chủ" aria-current="page">
    <span class="ico">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/></svg>
    </span>
  </button>

  <button type="button" class="bnav-item nav" data-nav="wrong" aria-label="Từ sai">
    <span class="ico">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h12v18l-6-4-6 4z"/></svg>
      <span class="badge" id="navBadge" aria-hidden="true" hidden>0</span>
    </span>
  </button>

  <button type="button" class="bnav-item nav" data-nav="dict" aria-label="Từ điển">
    <span class="ico">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4.5A2.5 2.5 0 0 1 6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5z"/><path d="M4 17.5h16"/><path d="M8 7h8"/></svg>
    </span>
  </button>
</nav>
```

## 6. Proposed JS (`updateNav` + init)

```js
function navIndex(){
  if (settings.screen === 'dict') return 4;
  if (settings.screen === 'wrong' || (settings.screen === 'exercise' && CUR_DS === 'wrong')) return 3;
  return 2; // home + normal exercises
}

function updateNav(){
  const wn = wrong[settings.lang].length;
  const badge = $('navBadge');
  if (badge){ badge.textContent = fmt(wn); badge.hidden = wn === 0; }

  const idx = navIndex();
  const nav = $('bnav');
  if (nav) nav.style.setProperty('--nav-i', String(idx));

  const activeName = idx === 4 ? 'dict' : idx === 3 ? 'wrong' : 'home';
  $$('.bnav .nav').forEach(function(b){
    const on = b.dataset.nav === activeName;
    b.classList.toggle('active', on);
    if (on) b.setAttribute('aria-current', 'page');
    else b.removeAttribute('aria-current');
  });

  $$('.bnav .lang').forEach(function(b){
    const on = b.dataset.lang === settings.lang;
    b.classList.toggle('on', on);
    b.setAttribute('aria-pressed', on ? 'true' : 'false');
  });

  const wrongBtn = document.querySelector('.bnav [data-nav="wrong"]');
  if (wrongBtn) wrongBtn.setAttribute('aria-label', wn ? 'Từ sai, ' + fmt(wn) + ' từ' : 'Từ sai');
}
```

Initial priming after `showScreen(settings.screen)`:

```js
requestAnimationFrame(function(){
  const nav = $('bnav');
  if (nav) nav.classList.add('is-ready');
});
```

No changes needed in `showScreen`/`showExercise`/`practiceWrong`/`setLang`: they all route through `rerender()` or `updateChrome()`, which call `updateNav()`.

## 7. Test plan

Update `tests/page-tests.js`:

1. `boot: bottom nav 5 buttons` — still 5.
2. `boot: nav home active` — still slot 2; add `--nav-i === '2'`.
3. `nav: pill moves home → wrong → dict`:
   - `showScreen('wrong')` → `--nav-i === '3'`
   - `showScreen('dict')` → `--nav-i === '4'`
   - `showScreen('home')` → `--nav-i === '2'`
4. `nav: wrong practice highlights Từ sai` — add a wrong word, `practiceWrong()`, `--nav-i === '3'`.
5. `nav: language toggle does not move the pill` — set a screen, click DE, pill index unchanged; `.lang.on` on DE; `aria-pressed`.
6. `nav: badge pulse` — visible badge has class `.badge`; computed `animationName` contains `softPulse`; hidden when count 0.
7. `nav: 5 equal slots` — `getBoundingClientRect()` widths differ by ≤1px; pill width ≈ 20% of nav.
8. `nav: active icon glow` — active SVG computed `filter` contains `drop-shadow`.
9. `nav: no external dependencies` — no `script[src]` / external stylesheet / font import in `index.html`.
10. `nav: aria` — active screen has `aria-current="page"`; language buttons have `aria-pressed`; badge is `aria-hidden`.

`tests/run-cdp.js`:
- Mobile 390×844: assert `.bnav` width ≤ 380, height 68, bottom offset ≥ 16px, no horizontal overflow.
- Capture `report/mobile-nav.png` with the nav over the dictionary (bright content) and over Home.
- Emulate `prefers-reduced-motion: reduce` and assert the pill transition duration is near zero.
- Keep the existing noscript check.

## 8. Acceptance criteria

- [ ] Bar uses 10px blur, 180% saturation, 1px white 10% border, layered shadow; no refraction beam.
- [ ] Pill is exactly 20% wide, 8px inset, 0.5s spring; moves only Home/Wrong/Dict.
- [ ] First paint does not animate the pill across the bar.
- [ ] Wrong-word badge is `#ff2d55`, 2px glass border, 2s soft pulse; count and ARIA label stay in sync.
- [ ] Active icon has a warm glow; inactive icons remain legible over blurred content.
- [ ] EN/DE show a small active dot and `aria-pressed`; they never receive the pill.
- [ ] Safe area respected; content can scroll fully above the bar; no overlap at 360/390/430px.
- [ ] Reduced motion disables pill transition and badge pulse.
- [ ] Fallback for browsers without `backdrop-filter` remains opaque and readable.
- [ ] No external fonts/scripts/CDNs; remains offline single-file.
- [ ] `python tools/build.py`; CDP suite 68+ assertions pass; no JS errors; mobile overflow check passes.

## 9. Risks / decisions

1. **Navy vs neutral glass.** The design uses neutral graphite over black; the app is navy. Recommendation: navy-tinted glass (`rgba(18,26,42,.58)`) so it doesn't look pasted on. Verify over the brightest content (dictionary rows).
2. **Bottom offset.** Design uses 34px on a 600px mock. Recommendation: `22px + safe-area` so Android and iPhone both look intentional; adjust after device QA.
3. **Nested blur.** The pill has its own `backdrop-filter` inside the bar's. On some Android GPUs this can flicker or cost frames. If it does, remove the pill's blur and use `linear-gradient(180deg, rgba(255,255,255,.18), rgba(255,255,255,.10))`.
4. **Pill during wrong practice.** Recommendation: highlight Từ sai. This is a behavior change from "Home for every exercise"; call it out in the release note.
5. **Language active indicator.** The design has no language toggles. The dot is the smallest deviation; do not add a second pill.
6. **Icon size.** Design uses 28px; the app's stroke icons at 25px keep the same visual weight without crowding the 380px bar.
7. **Contrast.** Translucent glass over busy content can reduce contrast. Keep bar alpha ≥ .58 and test with the brightest dictionary rows; if needed, add a subtle `linear-gradient(180deg, rgba(10,18,32,.18), rgba(10,18,32,.42))` overlay inside the bar.

## 10. Rollout

1. Edit `src/template.html` only (CSS/HTML/JS); do not touch `index.html`.
2. `python tools/build.py`
3. Start Chrome headless with `--remote-debugging-port=9222`; run `node tests/run-cdp.js "file:///.../index.html"`.
4. Visual QA at 360/390/430px: Home, exercise, wrong list, dictionary, sheet open (nav must stay under the sheet).
5. Rebuild and commit only after tests + visual QA pass; push triggers GitHub Pages (~1 min).

Estimated effort: **2–3 hours** (one template file + tests), no data or build-pipeline changes.
