# Học Từ Vựng Anh · Đức

App học từ vựng **1 file HTML duy nhất** — chạy offline, không server, không dependency.

**Mở online:** https://tonuy123.github.io/hoc-tu-vung/

> ⚠️ Trên iPhone: **đừng mở file bằng Files app / Quick Look preview** — Apple chặn JavaScript trong preview (từ iOS 13), câu hỏi sẽ không hiện. Mở bằng **Safari/Chrome** qua URL trên, hoặc cài app xem HTML hỗ trợ JS.

## Tính năng

- **7.516 từ**: 1.000 từ Anh cơ bản · 3.481 từ Anh thông dụng · 3.035 từ Đức (có mạo từ der/die/das, số nhiều)
- **4 dạng bài tập**: 1. Chọn nghĩa · 2. Viết nghĩa · 3. Viết từ · 4. Chọn từ
- **Mục "Từ sai"**: làm sai tự động lưu vào bank riêng theo ngôn ngữ; ôn lại làm đúng thì tự xóa khỏi danh sách (tối đa 1.000 từ)
- **2 tab danh sách từ** (tra cứu): render toàn bộ 1k/3k/Deutsch, tìm kiếm lọc **cả từ lẫn nghĩa**, **gõ không dấu vẫn ra**, nút nghe phát âm từng từ, badge ⚠️ đánh dấu từ đang trong mục ôn tập
- Tiến độ + từ sai + cài đặt tự lưu localStorage, khôi phục sau khi đóng trang
- Phát âm Web Speech API (nghe từ, tự động đọc tùy chọn)
- Toàn bộ data nhúng trong 1 file — copy đi đâu cũng chạy, mở `file://` trực tiếp trên desktop browser cũng chạy

## Cấu trúc repo

```
index.html          ← build output (GitHub Pages serve file này) — KHÔNG sửa tay
src/template.html   ← UI + logic app (sửa ở đây)
src/data/en1k.json  ← 1.000 từ Anh cơ bản (1 entry / dòng)
src/data/en3k.json  ← 3.481 từ Anh thông dụng
src/data/de3k.json  ← 3.035 từ Đức
tools/build.py      ← build: data + template → index.html
tools/audit.py      ← audit tự động: trùng lặp, format, bất thường → report/audit-report.md
tools/apply_fixes.py← merge report/fixes/*.json vào data + sinh changelog
tests/run-cdp.js + tests/page-tests.js ← test suite chạy headless Chrome (CDP)
report/             ← audit report, changelog review nghĩa, screenshot
```

## Quy trình update

1. Sửa data: `src/data/*.json` (mỗi dòng 1 entry `{"num":..,"word":..,"type":..,"phon":..,"meaning":..}`)
2. Rebuild: `python tools/build.py`
3. Test: mở Chrome headless với `--remote-debugging-port=9222` rồi `node tests/run-cdp.js "file:///<đường-dẫn>/index.html"`
4. Commit + push — GitHub Pages tự deploy sau ~1 phút

Sửa UI/logic: sửa `src/template.html` → rebuild → test.

## Review nghĩa

- `report/audit-report.md` — kết quả audit tự động
- `report/nghia-review.md` — changelog 600 fix nghĩa (52 batch: en1k 76 · en3k 494 · de3k 30 fix)
- `report/fixes/*.json` — fix gốc từng batch (giữ lại để audit)

## Test suite

`tests/page-tests.js` chạy trong trang (29 assertions: boot, MC/WRITE flow, bank từ sai, list 1k/3k/Deutsch, search không dấu, badge, đổi ngôn ngữ, no-JS error) + `tests/run-cdp.js` kiểm tra thêm mobile viewport 390×844 (không tràn ngang) và noscript banner.

## Ghi chú

- File `index.html` ~860KB — load lần đầu trên 4G khoảng 1-2s, sau đó browser cache.
- Repo public (điều kiện để dùng GitHub Pages miễn phí). Trong file không chứa key/credential — chỉ data từ vựng.
- Nguồn từ vựng: tổng hợp từ danh sách Oxford 3000 & danh sách từ tiếng Đức thông dụng; nghĩa tiếng Việt đã qua review 52 batch (600 chỉnh sửa) — xem changelog.
