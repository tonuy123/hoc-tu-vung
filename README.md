# Học Từ Vựng Anh · Đức

App học từ vựng **1 file HTML duy nhất** — chạy offline, không server, không dependency.

**Mở online:** https://tonuy123.github.io/hoc-tu-vung/

> Trên iPhone: **đừng mở file bằng Files app / Quick Look preview** — Apple chặn JavaScript trong preview (từ iOS 13), câu hỏi sẽ không hiện. Mở bằng **Safari/Chrome** qua URL trên, hoặc cài app xem HTML hỗ trợ JS.

## Tính năng

- **7.731 từ**: 1.000 từ Anh cơ bản · 3.479 từ Anh thông dụng · 3.252 từ Đức (mạo từ der/die/das, số nhiều, **24 chủ đề A1**)
- **Bottom navigation 5 mục đúng bản gốc**: Home · Play · Heart (Từ sai) · Search (Từ điển) · Avatar (Hồ sơ) — liquid glass (blur 10px, saturate 180%), pill trượt 20% với glow, active icon glow, badge đỏ pulse, bar 68px/380px đặt cách đáy 34px.
- **Hồ sơ (avatar)**: glass **theo theme thiết bị** — máy tối → navy/green + lime, máy sáng → light glass; avatar tròn **đổi ảnh từ máy** (resize 256px, lưu localStorage, nav avatar sync ngay), stats, tags bộ từ, ngôn ngữ EN/DE, số câu/phiên, xóa tiến độ.
- **Home dashboard (fintech style)**: top bar avatar + lời chào + chuông từ sai; hero tổng câu/độ chính xác + đổi bộ từ; 4 quick action bài tập; chart tuần/tháng theo hoạt động ngày; danh sách hoạt động gần đây + sheet xem tất cả. Avatar đồng bộ từ Hồ sơ.
- **4 dạng bài tập**: Chọn nghĩa · Viết nghĩa · Viết từ · Chọn từ. **Tiếng Đức lọc theo 24 chủ đề** (Chào hỏi, Gia đình, Đồ ăn, Động từ, Số đếm…) — mỗi chủ đề một phiên riêng, đổi chủ đề tự xáo bộ mới.
- **Mục "Từ sai"**: màn danh sách riêng (search, phát âm) + nút Ôn tập; làm sai tự lưu theo ngôn ngữ, ôn lại làm đúng thì tự xóa (tối đa 1.000 từ).
- **Từ điển A-Z**: EN (merge 1k + 3k) và DE; lọc theo chữ cái A-Z (tiếng Đức gộp Ä→A, Ö→O, Ü→U, ß→S nên không sót từ); **tiếng Đức lọc thêm 24 chủ đề** (kết hợp được với lọc loại từ); **lọc loại từ** (danh từ, động từ, tính từ, trạng từ, tính từ cảm xúc, động từ hành động, cụm từ, khác); tìm kiếm **cả từ lẫn nghĩa**, **gõ không dấu vẫn ra**; gom nhóm **cùng nghĩa tiếng Việt**; tap từ mở chi tiết có phon, từ loại, nghĩa, **số nhiều / dạng chia động từ / chủ đề**, **2-3 câu ví dụ + bản dịch** (tổng 15.088 câu), nút nghe.
- **Từ điển ngữ pháp**: tab `Từ vựng | Ngữ pháp` ngay trong màn Từ điển — **98 chuyên đề** (12 thì, 12 động từ, 32 cấu trúc câu, 8 câu nâng cao, 28 từ loại, 6 TOEIC & IELTS), lọc theo nhóm, search cả công thức/ví dụ/lỗi thường gặp, sheet chi tiết có công thức, cách dùng, dấu hiệu, ví dụ, lỗi sai và ghi chú thi cử.
- **Ngân hàng câu luyện tập**: **98 bank, mỗi bank tối thiểu 200.000 câu, tổng 70.192.896 câu** địa chỉ hóa được, sinh bằng generator seed cố định — không nhồi hàng trăm MB text vào file HTML; mỗi câu có sẵn token đã xáo trộn cho bài tập sắp xếp từ. Gồm 12 thì, 12 bank động từ, 86 pattern bank cấu trúc/từ loại/exam.
- **Chống mẹo trắc nghiệm**: distractor random từ toàn bộ pool ngôn ngữ (EN 1k+3k), không lộ từ loại, tối đa 2 option cùng POS, thứ tự đáp án ổn định theo seed.
- Tiến độ + từ sai + cài đặt tự lưu localStorage, khôi phục sau khi đóng trang.
- Phát âm Web Speech API bằng nút 🔊 thủ công (đã bỏ tự động đọc).
- Toàn bộ data nhúng trong 1 file — copy đi đâu cũng chạy, mở `file://` trực tiếp trên desktop browser cũng chạy.

## Cấu trúc repo

```
index.html              ← build output (GitHub Pages serve file này) — KHÔNG sửa tay
src/template.html       ← UI + logic app (sửa ở đây)
src/data/en1k.json      ← 1.000 từ Anh cơ bản (1 entry / dòng)
src/data/en3k.json      ← 3.479 từ Anh thông dụng
src/data/de3k.json      ← 3.035 từ Đức gốc (build merge thêm A1 → 3.252)
src/data/de_a1.json     ← 925 từ Đức A1 trích từ file Word, gắn 24 chủ đề
src/data/de_topics.json ← metadata 24 chủ đề (id, tên đầy đủ, tên ngắn, số từ)
src/data/grammar.json   ← 98 chuyên đề + lexicon + 86 pattern bank + cấu hình 200k câu
src/data/ex/en1k.json   ← ví dụ đã merge (num → [{s,t}]) — build tự nhúng vào app
src/data/ex/en3k.json
src/data/ex/de3k.json
report/examples/        ← batch gốc ví dụ (en1k-bNN.json, ...) để review/merge lại
tools/build.py          ← build: data + examples + template → index.html
tools/gen_grammar_banks.py ← sinh 43 bank ngữ pháp còn lại (idempotent, validate capacity)
tools/gen_full_grammar.py ← sinh 40 bank nâng cao: động từ, câu phức, từ loại, IELTS
tools/gen_de_topics.py  ← trích 925 từ Đức A1 từ file Word → de_a1.json + de_topics.json
tools/audit.py          ← audit data: trùng lặp, format, bất thường → report/audit-report.md
tools/audit_examples.py ← audit ví dụ: đủ câu, có từ gốc, bản dịch, trùng → report/examples-audit.md
tools/apply_examples.py ← merge report/examples/*.json → src/data/ex/*.json
tools/gen_examples.py   ← sinh ví dụ hàng loạt qua DeepSeek API (resume theo batch, validate ngôn ngữ)
tools/cleanup_data.py   ← one-off chuẩn hóa type + sửa entry lỗi (không renumber)
tools/apply_fixes.py    ← merge report/fixes/*.json vào data (giữ cho lịch sử nghĩa)
tests/run-cdp.js + tests/page-tests.js ← test suite headless Chrome (CDP)
report/                 ← audit, changelog nghĩa, data cleanup, screenshot QA
```

## Quy trình update

1. Sửa data: `src/data/*.json` (mỗi dòng 1 entry `{"num":..,"word":..,"type":..,"phon":..,"meaning":..}`). **Không renumber `num`** — `num` là ID trong localStorage của user.
2. Thêm ví dụ: tạo batch `report/examples/<ds>-bNN.json` (format bên dưới) → `python tools/apply_examples.py` → `python tools/audit_examples.py`.
3. Rebuild: `python tools/build.py`.
4. Test: mở Chrome headless với `--remote-debugging-port=9222` rồi `node tests/run-cdp.js "file:///<đường-dẫn>/index.html"`. Sinh ví dụ tự động: `python tools/gen_examples.py --all` (đọc DeepSeek key từ config opencode, không log key).
5. Commit + push — GitHub Pages tự deploy sau ~1 phút.

Sửa UI/logic: sửa `src/template.html` → rebuild → test.

### Grammar bank

- `src/data/grammar.json` chứa `topics` (98 chuyên đề), `lexicon` (16 chủ ngữ, 24 động từ, 4 trạng từ, 12 cụm thời gian/thì, 86 pattern bank) và `bankPerTopic: 200000`.
- **12 topic `cat: "Thì"`** có `gen.tense`; mỗi topic expose **200.000 câu** qua `grammarItem(topicId, n)` — deterministic, cùng `n` luôn ra cùng câu và cùng thứ tự token. Tổ hợp đầy đủ là 294.912 câu/thì.
- **86 topic còn lại** có `gen.bank`, mỗi bank tối thiểu 200.000 câu. Ví dụ: `there-is-are` 221.184 · `passive-voice` 211.968 · `used-to` 294.912 · `articles` 3.686.400 · `comparatives` 4.608.000 · `verb-patterns` 384.000 · `sentence-types` 384.000 · `toeic-business` 230.400 · `ielts-linking` 384.000.
- Tổng cộng **70.192.896 câu** trên 98 bank, mỗi bank ≥ 200.000. Không lưu literal từng câu; index được giải mã theo mixed-radix (template + từng chiều dữ liệu).
- `grammarItem` trả `{ id, topic, level, title, en, tokens, answer, hint }`; `tokens` đã xáo trộn bằng `mulberry32` để dùng trực tiếp cho bài tập sắp xếp từ.
- Thêm chuyên đề mới: sửa `grammar.json` (id/cat/level/title/vi/formula/use/signals/examples/mistakes/exam). Dùng `gen.tense` khi đã có profile chia thì trong `TENSE_PROFILE`; dùng `gen.bank` + entry trong `lexicon.patterns` khi muốn bank câu theo mẫu riêng. Build sẽ validate placeholder, kiểu slot và capacity ≥ 200k.
- Sinh lại 43 bank cấu trúc/từ loại: `python tools/gen_grammar_banks.py all`. Sinh lại 40 bank nâng cao: `python tools/gen_full_grammar.py`.

### Format batch ví dụ

```json
{"file":"en1k","batch":"en1k-b01","items":[
  {"num":1,"ex":[{"s":"I need a pen.","t":"Tôi cần một cây bút."},
                  {"s":"She has a cat.","t":"Cô ấy có một con mèo."}]}
]}
```

- `apply_examples.py` merge tất cả batch theo `num`; batch sau được phép override batch trước (dùng để sửa).
- `audit_examples.py` báo tiến độ theo từ (0/1/2/3+ ví dụ) và lỗi cứng; **lỗi cứng → exit 1**.
- Đã đủ: **15.088 câu** (en1k 2.060 · en3k 6.958 · de3k 6.070), audit **0 lỗi cứng** — xem `report/examples-audit.md`. 569 cảnh báo heuristic là biến đổi/separable verb (đã spot-check).

## Test suite

`tests/page-tests.js` chạy trong trang (**213 assertions**): boot shell/nav/home, mở bài, 4 option unique, bỏ type chip, lưu từ sai + badge, thứ tự đáp án ổn định, giữ draft khi đổi tab, reveal tính sai + vào bank + ví dụ, màn Từ sai + practice + back, dictionary A-Z EN/DE, search không dấu, ẩn A-Z khi search, nhóm đồng nghĩa, **lọc loại từ EN/DE: động từ, cảm xúc, hành động, cụm từ + search giữ filter**, **tiếng Đức: 24 chủ đề, count khớp từ, phiên bài tập chỉ chứa từ trong chủ đề, chip chủ đề ở bài tập + từ điển, A-Z sorted theo locale de, umlaut gộp đúng, giữ mạo từ + số nhiều + dạng chia**, sheet chi tiết có 3 ví dụ, **grammar dictionary 98 chuyên đề + 7 nhóm + search + detail sheet + Enter**, **98 bank: capacity ≥ 200k, clamp, deterministic, token khớp câu, chia thì 3s/past đúng, there is/are hợp số, passive be + V3, used to + V, articles a/an, countable/uncountable, pronoun, comparative, verb patterns, sentence types, punctuation, TOEIC/IELTS frame**, đổi ngôn ngữ, liquid glass nav (pill index, 5 slot đều, pill khớp slot, icon glow, badge pulse, aria, không external asset), profile/avatar (theme-aware theo thiết bị, stats, tags, set/clear ảnh + nav/home sync), fintech home (hero, 4 quick actions, chart tuần/tháng, peak bar, recent + sheet, dataset cycle, bell), error banner (ẩn mặc định, chỉ hiện khi debug, lọc noise Firefox/Ethereum), data sanity, no JS error. `tests/run-cdp.js` kiểm tra thêm mobile viewport 390×844 (home + dictionary không tràn ngang), screenshot `report/mobile-dict.png`, và noscript banner.

## Data / audit

- `report/audit-report.md` — audit data tự động (còn 27 mục: 3 cặp đa nghĩa `senior/severe/share`, 19 type nhiều từ loại, 2 word dài BrE/NAmE, 1 num gap đã chấp nhận, `video` word=meaning).
- `report/examples-audit.md` — tiến độ + lỗi ví dụ (0 lỗi cứng; cảnh báo heuristic biến đổi/separable verb).
- `report/data-cleanup.md` — các fix data đã áp (chuẩn hóa type, xóa 2 entry trùng `3055`/`3256`, sửa phon `1122`/`3047`).
- `report/nghia-review.md` — changelog 600 fix nghĩa cũ (52 batch).
- `report/fixes/*.json` — fix gốc từng batch nghĩa (giữ để audit).
- `report/qa-home.png`, `qa-exercise.png`, `qa-dict-list.png`, `qa-dict-types.png`, `qa-dict-detail.png`, `qa-de-topics.png`, `qa-de-detail.png`, `qa-de-exercise.png`, `qa-de-mobile-dict.png`, `qa-de-mobile-exercise.png`, `qa-grammar-desktop.png`, `qa-grammar-mobile.png`, `qa-grammar-detail.png`, `qa-settings-dark.png`, `qa-settings-light.png`, `mobile-dict.png` — screenshot QA.

## Ghi chú

- `index.html` hiện ~3.95MB (đủ 15.088 câu ví dụ + 70,19M câu grammar addressable; gzip ~1MB) — load 4G ước 3-4s, sau đó browser cache.
- Banner lỗi JS **tắt mặc định** (tránh noise từ extension/browser như Firefox Reader, MetaMask). Bật để debug: mở `?debug=1` hoặc `localStorage.setItem('v4t:debug','1')`.
- en3k thiếu `num` 2247 (gap ID, không ảnh hưởng runtime; **không renumber**).
- 181 entry en3k thiếu `phon` — UI ẩn dòng phiên âm; không bịa IPA.
- Repo public (điều kiện dùng GitHub Pages miễn phí). Trong file không chứa key/credential — chỉ data từ vựng.
- Nguồn từ vựng: tổng hợp Oxford 3000 & danh sách tiếng Đức thông dụng; **925 từ Đức A1 trích từ `Tu-vung-tieng-Duc-A1-theo-chu-de.docx`** (mạo từ, số nhiều, dạng chia động từ, ví dụ giới từ) — regenerate bằng `python tools/gen_de_topics.py`; nghĩa tiếng Việt đã qua review 52 batch (600 chỉnh sửa) — xem changelog.
