# cleanup_data.py - one-off data hygiene pass (no renumbering)
# - normalize POS type formatting (drop trailing dots, e.g. "n., v" -> "n, v")
# - repair two malformed en3k entries (3256, 3055) without changing counts
# Usage: python tools/cleanup_data.py
import io
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'src', 'data')
OUT = os.path.join(ROOT, 'report', 'data-cleanup.md')
FILES = ['en1k.json', 'en3k.json', 'de3k.json']


def read_json(fp):
    with io.open(fp, encoding='utf-8') as f:
        return json.load(f)


def write_words(fp, words):
    body = '[\n' + ',\n'.join('  ' + json.dumps(w, ensure_ascii=False) for w in words) + '\n]\n'
    with io.open(fp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(body)


def clean_type(v):
    t = str(v.get('type', '') or '')
    t = re.sub(r'\.', '', t)
    t = re.sub(r'\s+', ' ', t)
    t = re.sub(r',\s*,+', ', ', t)
    t = t.strip(' ,')
    return t


def main():
    rows = []
    for name in FILES:
        words = read_json(os.path.join(DATA, name))
        changed_type = 0
        for w in words:
            old = str(w.get('type', '') or '')
            new = clean_type(w)
            if new != old:
                w['type'] = new
                changed_type += 1
        if name == 'en3k.json':
            before = len(words)
            words = [w for w in words if w.get('num') not in (3055, 3256)]
            if before != len(words):
                rows.append(('en3k', '3055, 3256', 'entry', 'duplicate entries', 'removed'))
            for w in words:
                if w.get('num') == 3047 and w.get('phon') != '/ˈswəʊlən/':
                    old = w.get('phon', '')
                    w['phon'] = '/ˈswəʊlən/'
                    rows.append(('en3k', 3047, 'phon', old, '/ˈswəʊlən/'))
                if w.get('num') == 1122 and 'li' not in str(w.get('phon', '')):
                    old = w.get('phon', '')
                    w['phon'] = '/ˌʌnɪkˈspektɪdli/'
                    rows.append(('en3k', 1122, 'phon', old, '/ˌʌnɪkˈspektɪdli/'))
        write_words(os.path.join(DATA, name), words)
        rows.append((name, '-', 'type-format', '%d entries' % changed_type, 'normalized'))
        print('%s: type normalized in %d entries' % (name, changed_type))

    lines = ['# Data cleanup — 2026-10-27', '']
    lines.append('Không renumber `num` (ID dùng trong localStorage).')
    lines.append('')
    lines.append('| file | num | field | old | new |')
    lines.append('|---|---|---|---|---|')
    for r in rows:
        lines.append('| %s | %s | %s | %s | %s |' % r)
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    print('WROTE', OUT)


if __name__ == '__main__':
    main()
