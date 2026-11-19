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
- **Từ điển A-Z**: EN (merge 1k + 3k) và DE; lọc theo chữ cái A-Z (tiếng Đức gộp Ä→A, Ö→O, Ü→U, ß→S nên không sót từ); **tiếng Đức lọc thêm 24 chủ đề** (kết hợp được với lọc loại từ); **lọc loại từ** (danh từ, động từ, tính từ, trạng từ, tính từ cảm xúc, động từ hành động, cụm từ, khác); tìm kiếm **cả từ lẫn nghĩa**, **gõ không dấu vẫn ra**; gom nhóm **cùng nghĩa tiếng Việt**; tap từ mở chi tiết có phon, từ loại, nghĩa, **số nhiều / dạng chia động từ / chủ đề**, **2-3 câu ví dụ + bản dịch** (tổng 15.522 câu), nút nghe.
- **Từ điển ngữ pháp**: tab `Từ vựng | Ngữ pháp` ngay trong màn Từ điển, có công tắc **English | Deutsch** — **98 chuyên đề tiếng Anh** (12 thì, 12 động từ, 32 cấu trúc câu, 8 câu nâng cao, 28 từ loại, 6 TOEIC & IELTS) và **52 chuyên đề tiếng Đức A1→B2**, lọc theo nhóm, search cả công thức/ví dụ/lỗi thường gặp, sheet chi tiết có công thức, cách dùng, dấu hiệu, ví dụ, lỗi sai và ghi chú thi cử.
- **Ngữ pháp Đức chia theo level**: chip `Tất cả | A1 | A2 | B1 | B2` — chọn A1 chỉ hiện đúng 14 chuyên đề A1, không lẫn level khác (bộ lọc level chạy trước lọc nhóm và search).
- **Ngân hàng câu luyện tập**: **98 bank tiếng Anh, mỗi bank tối thiểu 200.000 câu, tổng 70.192.896 câu** + **52 bank tiếng Đức, tổng 337.188.664 câu** — địa chỉ hóa được, sinh bằng generator seed cố định, không nhồi hàng trăm MB text vào file HTML; mỗi câu có sẵn token đã xáo trộn cho bài tập sắp xếp từ.
- **Chống mẹo trắc nghiệm**: distractor random từ toàn bộ pool ngôn ngữ (EN 1k+3k), không lộ từ loại, tối đa 2 option cùng POS, thứ tự đáp án ổn định theo seed.
- Tiến độ + từ sai + cài đặt tự lưu localStorage, khôi phục sau khi đóng trang.
- Phát âm Web Speech API bằng nút 🔊 thủ công (đã bỏ tự động đọc).
- Toàn bộ data nhúng trong 1 file — copy đi đâu cũng chạy, mở `file://` trực tiếp trên desktop browser cũng chạy.
- **Tab "Sắp xếp câu" (tab thứ 5 trong Bài tập)**: chọn level `A1–B2` + chuyên đề, mỗi chuyên đề có **20 câu thật viết tay** bám đúng ngữ pháp của chuyên đề đó — **đề bài là câu tiếng Việt** (“Anh ấy làm việc ở văn phòng.”), dưới là các từ tiếng Đức xáo trộn để ghép. Kiểm tra ngay, xem đáp án, sang câu tiếp; có thể vào nhanh từ nút ▶ ở danh sách ngữ pháp hoặc từ sheet chi tiết.
- **Chi tiết ngữ pháp**: sheet mở ra có công thức, cách dùng từng bước (3 bước), dấu hiệu nhận biết, 4 ví dụ có dịch, 3 lỗi **Sai / Đúng** kèm giải thích, mục **Lưu ý** và ghi chú thi cử.
- **Từ điển và bài tập độc lập**: đổi ngôn ngữ/chủ đề trong Từ điển **không** làm reset phiên bài tập và ngược lại — hai màn giữ state riêng (`dictLang`/`dictTopic` vs `lang`/`dtopic`).
- **Số nhiều trong bài tập**: danh từ Đức có số nhiều thì hiện `Pl.: die …` **ngay cạnh từ** ở phần từ điển/chi tiết; ở bài trắc nghiệm chỉ hiện đáp án sạch, không còn ghi chú trong ngoặc.

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
src/data/de_grammar.json ← 52 chuyên đề ngữ pháp Đức A1→B2 + 52 pattern bank (sinh từ tools/de_grammar/)
tools/de_grammar/       ← nguồn Python của ngữ pháp Đức (lexicon + 4 file bank + topics)
tools/gen_de_grammar.py ← sinh src/data/de_grammar.json, validate capacity/placeholder/word order
src/data/ex/en1k.json   ← ví dụ đã merge (num → [{s,t}]) — build tự nhúng vào app
src/data/ex/en3k.json
src/data/ex/de3k.json
src/data/ex/de_a1.json   ← 434 ví dụ cho 217 từ Đức A1 mới (DeepSeek)
report/examples/        ← batch gốc ví dụ (en1k-bNN.json, ...) để review/merge lại
tools/build.py          ← build: data + examples + template → index.html
tools/gen_grammar_banks.py ← sinh 43 bank ngữ pháp còn lại (idempotent, validate capacity)
tools/gen_full_grammar.py ← sinh 40 bank nâng cao: động từ, câu phức, từ loại, IELTS
tools/gen_de_topics.py  ← trích 925 từ Đức A1 từ file Word → de_a1.json + de_topics.json
tools/missing_de_examples.py ← liệt kê num từ Đức A1 mới chưa có ví dụ
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

### Ngữ pháp Đức (A1→B2)

- Nguồn nằm trong `tools/de_grammar/`: `lexicon.py` (động từ + bảng chia + pool danh từ/tính từ/giới từ + helper ghép câu), `banks_a1/a2/b1/b2.py` (52 bank), `topics.py` (metadata 52 chuyên đề: id/level/cat/title/vi/formula/use/signals/examples/mistakes/exam), `topics_extra.py` (bổ sung `howto` = cách dùng từng bước, `notes` = lưu ý, thêm ví dụ và lỗi sai cho cả 52 chuyên đề), `drill_a1/a2/b1/b2.py` (20 câu sắp xếp cho mỗi chuyên đề, kèm câu tiếng Việt làm đề bài).
- Sinh lại: `python tools/gen_de_grammar.py` → ghi `src/data/de_grammar.json` (~1,6 MB). Xem thử câu mẫu: `python tools/gen_de_grammar.py --sample`.
- **Hợp đồng với engine**: mỗi bank khai báo `dims` + `templates`, và **mọi template phải dùng đủ mọi dim** — nếu thiếu, hai index khác nhau sẽ render ra cùng một câu. `shapes_main`/`shapes_yfrage`/`shapes_sub`/`shapes_pair` trong `lexicon.py` sinh sẵn bộ template thoả điều kiện này và giữ trật tự từ hợp lệ.
- **Quy tắc chất lượng câu** (generator không tự bắt được, phải giữ khi thêm bank):
  - mỗi động từ mang bổ ngữ riêng (`("fahren", "nach Berlin")`) — không cross động từ với object rời, tránh “Ich fahre den Text”;
  - trạng từ thời gian đứng ngay sau động từ chia, trạng từ thể cách đứng sau thời gian, không bao giờ bỏ lửng cuối câu;
  - tiền tố động từ tách rời / phân từ / động từ nguyên thể luôn nằm trong `comp` và là thành phần cuối;
  - slot không phải danh từ viết **chữ thường** (renderer chỉ viết hoa ký tự đầu câu);
  - bank thì quá khứ dùng `TIME_PAST`, bank hiện tại dùng `TIME_BASE`.
- Capacity: mỗi chuyên đề ≥ 200.000 câu; tổng 52 bank = 337.188.664 câu. `build.py` validate lại toàn bộ (placeholder, kiểu slot, capacity ≥ 200k) trước khi nhúng.

### Format batch ví dụ

```json
{"file":"en1k","batch":"en1k-b01","items":[
  {"num":1,"ex":[{"s":"I need a pen.","t":"Tôi cần một cây bút."},
                  {"s":"She has a cat.","t":"Cô ấy có một con mèo."}]}
]}
```

- `apply_examples.py` merge tất cả batch theo `num`; batch sau được phép override batch trước (dùng để sửa).
- `audit_examples.py` báo tiến độ theo từ (0/1/2/3+ ví dụ) và lỗi cứng; **lỗi cứng → exit 1**.
- Đã đủ: **15.522 câu** (en1k 2.060 · en3k 6.958 · de3k 6.504), audit **0 lỗi cứng** — xem `report/examples-audit.md`. 577 cảnh báo heuristic là biến đổi/separable verb (đã spot-check). 434 câu của 217 từ Đức A1 mới được sinh bằng DeepSeek `deepseek-v4-flash`.

## Test suite

`tests/page-tests.js` chạy trong trang (**264 assertions**): boot shell/nav/home, mở bài, 4 option unique, bỏ type chip, lưu từ sai + badge, thứ tự đáp án ổn định, giữ draft khi đổi tab, reveal tính sai + vào bank + ví dụ, màn Từ sai + practice + back, dictionary A-Z EN/DE, search không dấu, ẩn A-Z khi search, nhóm đồng nghĩa, **lọc loại từ EN/DE: động từ, cảm xúc, hành động, cụm từ + search giữ filter**, **tiếng Đức: 24 chủ đề, count khớp từ, phiên bài tập chỉ chứa từ trong chủ đề, chip chủ đề ở bài tập + từ điển, A-Z sorted theo locale de, umlaut gộp đúng, giữ mạo từ + số nhiều + dạng chia**, sheet chi tiết có 3 ví dụ, **grammar dictionary 98 chuyên đề + 7 nhóm + search + detail sheet + Enter**, **98 bank: capacity ≥ 200k, clamp, deterministic, token khớp câu, chia thì 3s/past đúng, there is/are hợp số, passive be + V3, used to + V, articles a/an, countable/uncountable, pronoun, comparative, verb patterns, sentence types, punctuation, TOEIC/IELTS frame**, **ôn Từ sai: session không bị tráo giữa phiên (2 câu liên tiếp vẫn đúng), tách state từ điển/bài tập (đổi chủ đề từ điển không reset phiên), đáp án trắc nghiệm sạch không ngoặc, Viết từ hiện nghĩa ở trên và gõ từ ở dưới, màn Sắp xếp câu (mở được, token đủ, ghép đúng, sang câu tiếp), sheet ngữ pháp có Cách dùng + Lưu ý + 4 ví dụ + 3 lỗi Sai/Đúng, profile không còn khối Bộ từ**, **ngữ pháp Đức: 52 chuyên đề, công tắc English/Deutsch, label “Deutsch”, chip level 5 nút, chọn A1/A2/B1/B2 chỉ ra đúng số chuyên đề của level đó và không lẫn level (id + badge đều khớp), 52 bank ≥ 200k render sạch (không placeholder, không double space), tokens khớp câu, clamp index**, đổi ngôn ngữ, liquid glass nav (pill index, 5 slot đều, pill khớp slot, icon glow, badge pulse, aria, không external asset), profile/avatar (theme-aware theo thiết bị, stats, tags, set/clear ảnh + nav/home sync), fintech home (hero, 4 quick actions, chart tuần/tháng, peak bar, recent + sheet, dataset cycle, bell), error banner (ẩn mặc định, chỉ hiện khi debug, lọc noise Firefox/Ethereum), data sanity, no JS error. `tests/run-cdp.js` kiểm tra thêm mobile viewport 390×844 (home + dictionary không tràn ngang), screenshot `report/mobile-dict.png`, và noscript banner.

## Data / audit

- `report/audit-report.md` — audit data tự động (còn 27 mục: 3 cặp đa nghĩa `senior/severe/share`, 19 type nhiều từ loại, 2 word dài BrE/NAmE, 1 num gap đã chấp nhận, `video` word=meaning).
- `report/examples-audit.md` — tiến độ + lỗi ví dụ (0 lỗi cứng; cảnh báo heuristic biến đổi/separable verb).
- `report/data-cleanup.md` — các fix data đã áp (chuẩn hóa type, xóa 2 entry trùng `3055`/`3256`, sửa phon `1122`/`3047`).
- `report/nghia-review.md` — changelog 600 fix nghĩa cũ (52 batch).
- `report/fixes/*.json` — fix gốc từng batch nghĩa (giữ để audit).
- `report/qa-home.png`, `qa-exercise.png`, `qa-dict-list.png`, `qa-dict-types.png`, `qa-dict-detail.png`, `qa-de-topics.png`, `qa-de-detail.png`, `qa-de-mobile-detail.png`, `qa-de-exercise.png`, `qa-de-mobile-dict.png`, `qa-de-mobile-exercise.png`, `qa-grammar-desktop.png`, `qa-grammar-mobile.png`, `qa-grammar-detail.png`, `qa-settings-dark.png`, `qa-settings-light.png`, `mobile-dict.png`, `grammar-de-a1.png` (ngữ pháp Đức lọc A1 trên mobile 390px), `grammar-de-detail.png` (sheet chi tiết: cách dùng, ví dụ, lỗi sai, lưu ý), `grammar-de-drill.png` (màn sắp xếp câu), `order-tab.png` (tab thứ 5: đề bài câu Việt + từ Đức xáo trộn), `write-vn.png` (Viết từ: nghĩa ở trên, gõ từ ở dưới), `quiz-clean.png` (đáp án trắc nghiệm không còn ghi chú trong ngoặc), `profile.png` (đã bỏ khối Bộ từ), `quiz-plural.png` — screenshot QA.

## Ghi chú

- `index.html` hiện ~5,7MB (đủ 15.522 câu ví dụ + 70,19M câu grammar EN + 337,19M câu grammar DE addressable; gzip ~1,2MB) — load 4G ước 3-4s, sau đó browser cache.
- Banner lỗi JS **tắt mặc định** (tránh noise từ extension/browser như Firefox Reader, MetaMask). Bật để debug: mở `?debug=1` hoặc `localStorage.setItem('v4t:debug','1')`.
- en3k thiếu `num` 2247 (gap ID, không ảnh hưởng runtime; **không renumber**).
- 181 entry en3k thiếu `phon` — UI ẩn dòng phiên âm; không bịa IPA.
- Repo public (điều kiện dùng GitHub Pages miễn phí). Trong file không chứa key/credential — chỉ data từ vựng.
- Nguồn từ vựng: tổng hợp Oxford 3000 & danh sách tiếng Đức thông dụng; **925 từ Đức A1 trích từ `Tu-vung-tieng-Duc-A1-theo-chu-de.docx`** (mạo từ, số nhiều, dạng chia động từ, ví dụ giới từ) — regenerate bằng `python tools/gen_de_topics.py`; 217 từ mới có thêm 2 ví dụ Đức–Việt sinh bằng DeepSeek (`de_a1`); nghĩa tiếng Việt đã qua review 52 batch (600 chỉnh sửa) — xem changelog.
