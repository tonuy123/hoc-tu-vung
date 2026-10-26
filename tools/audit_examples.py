# audit_examples.py - validate example sentences for the vocab app
# Usage: python tools/audit_examples.py
# Hard errors make the command exit 1. Missing examples are reported (progress mode).
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'src', 'data')
EXDIR = os.path.join(DATA, 'ex')
OUT = os.path.join(ROOT, 'report', 'examples-audit.md')
FILES = ['en1k', 'en3k', 'de3k']
LANG = {'en1k': 'English', 'en3k': 'English', 'de3k': 'German'}
DE_MARKERS = set('der die das den dem des ein eine einen einem einer und ist sind war nicht mit auf für von zu im am ich du er sie es wir ihr sich mein dein sein ihre hat habe haben wird werden kann können muss sehr auch aber oder wenn dass wie was wo kein keine zum zur vom beim'.split())
EN_MARKERS = set('the and is are was were a an to of in on at for with this that these those i you he she it we they my your his her its our their have has had do does did not but or if when where what who how can will would should could may might must'.split())


def marker_score(s, markers):
    ws = re.findall(r"[A-Za-zÀ-ÿß']+", s.lower())
    return sum(1 for w in ws if w in markers)


def wrong_language(s, lang):
    de = marker_score(s, DE_MARKERS)
    en = marker_score(s, EN_MARKERS)
    if lang == 'English':
        if de >= 3 and de > en:
            return True
        if re.search(r'[äöüßÄÖÜ]', s) and de >= 1 and de >= en:
            return True
        return False
    if lang == 'German':
        return en >= 4 and en > de + 1
    return False


def read_json(fp):
    with io.open(fp, encoding='utf-8') as f:
        return json.load(f)


def has_word(sentence, word):
    s = sentence.lower()
    w = re.sub(r'\([^)]*\)', ' ', word).lower()
    w = re.sub(r'^(der|die|das|ein|eine|einen|einem|einer)\s+', '', w).strip()
    toks = [t for t in re.findall(r"[a-zà-ÿäöüß']+", w) if len(t) >= 3]
    if not toks:
        return True
    if any(t in s for t in toks):
        return True
    for t in toks:
        if len(t) >= 5 and t[:-1] in s:
            return True
        if t.endswith('e') and t[:-1] + 'ing' in s:
            return True
        if t.endswith('y') and t[:-1] + 'ies' in s:
            return True
    return False


def main():
    lines = ['# Examples audit — vocabulary app', '']
    hard = 0
    warns = 0
    summary = []
    for name in FILES:
        words = read_json(os.path.join(DATA, name + '.json'))
        ex_path = os.path.join(EXDIR, name + '.json')
        ex = read_json(ex_path) if os.path.exists(ex_path) else {}
        word_map = {str(w['num']): w for w in words}
        dist = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
        n_sent = 0
        errs = []
        wns = []
        for k, w in word_map.items():
            items = ex.get(k, [])
            if not isinstance(items, list):
                errs.append('num %s: ex is not a list' % k)
                continue
            dist[min(len(items), 4)] = dist.get(min(len(items), 4), 0) + 1
            seen = set()
            for idx, it in enumerate(items):
                if not isinstance(it, dict):
                    errs.append('num %s item %d: not an object' % (k, idx))
                    continue
                s = str(it.get('s', '')).strip()
                t = str(it.get('t', '')).strip()
                if not s or not t:
                    errs.append('num %s item %d: empty s/t' % (k, idx))
                    continue
                if s in seen:
                    errs.append('num %s item %d: duplicate sentence' % (k, idx))
                seen.add(s)
                n_sent += 1
                if len(s) < 8 or len(s) > 220:
                    errs.append('num %s item %d: s length %d' % (k, idx, len(s)))
                if len(t) < 4 or len(t) > 200:
                    errs.append('num %s item %d: t length %d' % (k, idx, len(t)))
                if '\n' in s or '\n' in t:
                    errs.append('num %s item %d: newline' % (k, idx))
                if '</script' in (s + t).lower():
                    errs.append('num %s item %d: unsafe </script' % (k, idx))
                if wrong_language(s, LANG[name]):
                    errs.append('num %s item %d: wrong language (%s): %s' % (k, idx, LANG[name], s[:70]))
                if not has_word(s, w['word']):
                    wns.append('num %s (%s): %s' % (k, w['word'], s[:80]))
        hard += len(errs)
        warns += len(wns)
        summary.append((name, len(words), dist.get(0, 0), dist.get(1, 0), dist.get(2, 0), dist.get(3, 0) + dist.get(4, 0), n_sent))
        lines.append('## %s' % name)
        lines.append('')
        lines.append('- Từ: %d · có 3+ ví dụ: %d · 2: %d · 1: %d · 0: %d · tổng câu: %d' % (
            len(words), dist.get(3, 0) + dist.get(4, 0), dist.get(2, 0), dist.get(1, 0), dist.get(0, 0), n_sent))
        if errs:
            lines.append('- **Lỗi (%d)**' % len(errs))
            for e in errs[:20]:
                lines.append('  - %s' % e)
        if wns:
            lines.append('- **Cảnh báo heuristic từ gốc (%d — có thể báo nhầm với biến đổi/separable verb)**' % len(wns))
            for e in wns[:20]:
                lines.append('  - %s' % e)
        if not errs and not wns:
            lines.append('- Không có lỗi.')
        lines.append('')
    lines.append('## Tổng')
    lines.append('')
    for s in summary:
        lines.append('- %s: %d từ · 0 ví dụ: %d · 1: %d · 2: %d · 3+: %d · %d câu' % (s[0], s[1], s[2], s[3], s[4], s[5], s[6]))
    lines.append('')
    lines.append('- Lỗi cứng: **%d** · cảnh báo: **%d**' % (hard, warns))
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    print('SENTENCES:', sum(s[6] for s in summary))
    print('HARD_ERRORS:', hard)
    print('WARNINGS:', warns)
    print('WROTE', OUT)
    if hard:
        sys.exit(1)


if __name__ == '__main__':
    main()
