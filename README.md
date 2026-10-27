# Học Từ Vựng Anh · Đức

App học từ vựng **1 file HTML duy nhất** — chạy offline, không server, không dependency.

**Mở online:** https://tonuy123.github.io/hoc-tu-vung/

> Trên iPhone: **đừng mở file bằng Files app / Quick Look preview** — Apple chặn JavaScript trong preview (từ iOS 13), câu hỏi sẽ không hiện. Mở bằng **Safari/Chrome** qua URL trên, hoặc cài app xem HTML hỗ trợ JS.

## Tính năng

- **7.514 từ**: 1.000 từ Anh cơ bản · 3.479 từ Anh thông dụng · 3.035 từ Đức (có mạo từ der/die/das, số nhiều)
- **Bottom navigation 5 mục đúng bản gốc**: Home · Play · Heart (Từ sai) · Search (Từ điển) · Avatar (Hồ sơ) — liquid glass (blur 10px, saturate 180%), pill trượt 20% với glow, active icon glow, badge đỏ pulse, bar 68px/380px đặt cách đáy 34px.
- **Hồ sơ (avatar)**: hero light-glass, avatar tròn **đổi ảnh từ máy** (resize 256px, lưu localStorage, nav avatar sync ngay), stats, tags bộ từ, ngôn ngữ EN/DE, số câu/phiên, xóa tiến độ.
- **Home dashboard (fintech style)**: top bar avatar + lời chào + chuông từ sai; hero tổng câu/độ chính xác + đổi bộ từ; 4 quick action bài tập; chart tuần/tháng theo hoạt động ngày; danh sách hoạt động gần đây + sheet xem tất cả. Avatar đồng bộ từ Hồ sơ.
- **4 dạng bài tập**: Chọn nghĩa · Viết nghĩa · Viết từ · Chọn từ.
- **Mục "Từ sai"**: màn danh sách riêng (search, phát âm) + nút Ôn tập; làm sai tự lưu theo ngôn ngữ, ôn lại làm đúng thì tự xóa (tối đa 1.000 từ).
- **Từ điển A-Z**: EN (merge 1k + 3k) và DE; lọc theo chữ cái A-Z; tìm kiếm **cả từ lẫn nghĩa**, **gõ không dấu vẫn ra**; gom nhóm **cùng nghĩa tiếng Việt**; tap từ mở chi tiết có phon, từ loại, nghĩa, **2-3 câu ví dụ + bản dịch** (tổng 15.088 câu), nút nghe.
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
src/data/de3k.json      ← 3.035 từ Đức
src/data/ex/en1k.json   ← ví dụ đã merge (num → [{s,t}]) — build tự nhúng vào app
src/data/ex/en3k.json
src/data/ex/de3k.json
report/examples/        ← batch gốc ví dụ (en1k-bNN.json, ...) để review/merge lại
tools/build.py          ← build: data + examples + template → index.html
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

`tests/page-tests.js` chạy trong trang (**133 assertions**): boot shell/nav/home, mở bài, 4 option unique, bỏ type chip, lưu từ sai + badge, thứ tự đáp án ổn định, giữ draft khi đổi tab, reveal tính sai + vào bank + ví dụ, màn Từ sai + practice + back, dictionary A-Z EN/DE, search không dấu, ẩn A-Z khi search, nhóm đồng nghĩa, sheet chi tiết có 3 ví dụ, đổi ngôn ngữ, liquid glass nav (pill index, 5 slot đều, pill khớp slot, icon glow, badge pulse, aria, không external asset), profile/avatar (light mode, stats, tags, set/clear ảnh + nav/home sync), fintech home (hero, 4 quick actions, chart tuần/tháng, peak bar, recent + sheet, dataset cycle, bell), data sanity, no JS error. `tests/run-cdp.js` kiểm tra thêm mobile viewport 390×844 (home + dictionary không tràn ngang), screenshot `report/mobile-dict.png`, và noscript banner.

## Data / audit

- `report/audit-report.md` — audit data tự động (còn 27 mục: 3 cặp đa nghĩa `senior/severe/share`, 19 type nhiều từ loại, 2 word dài BrE/NAmE, 1 num gap đã chấp nhận, `video` word=meaning).
- `report/examples-audit.md` — tiến độ + lỗi ví dụ (0 lỗi cứng; cảnh báo heuristic biến đổi/separable verb).
- `report/data-cleanup.md` — các fix data đã áp (chuẩn hóa type, xóa 2 entry trùng `3055`/`3256`, sửa phon `1122`/`3047`).
- `report/nghia-review.md` — changelog 600 fix nghĩa cũ (52 batch).
- `report/fixes/*.json` — fix gốc từng batch nghĩa (giữ để audit).
- `report/qa-home.png`, `qa-exercise.png`, `qa-dict-list.png`, `qa-dict-detail.png`, `qa-settings.png`, `mobile-dict.png` — screenshot QA.

## Ghi chú

- `index.html` hiện ~2.69MB (đủ 15.088 câu ví dụ; gzip ~700KB) — load 4G ước 2-3s, sau đó browser cache.
- en3k thiếu `num` 2247 (gap ID, không ảnh hưởng runtime; **không renumber**).
- 181 entry en3k thiếu `phon` — UI ẩn dòng phiên âm; không bịa IPA.
- Repo public (điều kiện dùng GitHub Pages miễn phí). Trong file không chứa key/credential — chỉ data từ vựng.
- Nguồn từ vựng: tổng hợp Oxford 3000 & danh sách tiếng Đức thông dụng; nghĩa tiếng Việt đã qua review 52 batch (600 chỉnh sửa) — xem changelog.
