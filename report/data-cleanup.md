# Data cleanup — 2026-10-27

Không renumber `num` — `num` là ID dùng trong localStorage của user.

| file | phạm vi | field | old | new |
|---|---|---|---|---|
| en3k | 679 entry | type | `n., v` (có dấu chấm) | `n, v` |
| en3k | 3055, 3256 | entry | entry trùng (`swollen`, `unexpected`) | đã xóa |
| en3k | 1122 | phon | `/ˈʌniksˈpektid/` | `/ˌʌnɪkˈspektɪdli/` |
| en3k | 3047 | phon | `/ˈswoulən/` | `/ˈswəʊlən/` |

Kết quả: en1k 1.000 · en3k 3.479 · de3k 3.035 = **7.514 từ**.

Ghi chú:
- `num` 2247 (en3k) vẫn thiếu — gap ID đã chấp nhận, không renumber.
- 181 entry en3k thiếu `phon` — không bịa IPA.
- 3 cặp đa nghĩa giữ nguyên: `senior`, `severe`, `share`.
