# audit.py - automatic anomaly audit for vocab data
# Usage: python tools/audit.py
# Reads src/data/*.json, writes report/audit-report.md
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'src', 'data')
OUT = os.path.join(ROOT, 'report', 'audit-report.md')

FILES = ['en1k.json', 'en3k.json', 'de3k.json']


def load(name):
    with io.open(os.path.join(DATA, name), encoding='utf-8') as f:
        return json.load(f)


def main():
    lines = ['# Audit report — vocab data', '']
    total_issues = 0
    for name in FILES:
        words = load(name)
        issues = {}

        def add(cat, msg):
            issues.setdefault(cat, []).append(msg)

        nums = [w.get('num') for w in words]
        if nums != list(range(1, len(words) + 1)):
            bad = []
            for i, n in enumerate(nums):
                if n != i + 1:
                    bad.append('idx %d has num %s' % (i, n))
                    if len(bad) >= 10:
                        break
            add('num-sequence', '; '.join(bad))

        seen_key = {}
        seen_word = {}
        for w in words:
            key = (str(w.get('word', '')).strip().lower() + '|' + str(w.get('meaning', '')).strip().lower())
            if key in seen_key:
                add('dup-word+meaning', 'num %s dup with num %s (%s)' % (w.get('num'), seen_key[key], w.get('word')))
            else:
                seen_key[key] = w.get('num')
            wd = str(w.get('word', '')).strip().lower()
            seen_word.setdefault(wd, []).append(w.get('num'))

        for wd, ns in seen_word.items():
            if len(ns) > 1:
                add('dup-word', '%s at nums %s' % (wd, ns[:6]))

        for w in words:
            num = w.get('num')
            word = str(w.get('word', '')).strip()
            meaning = str(w.get('meaning', '')).strip()
            phon = str(w.get('phon', '')).strip()
            typ = str(w.get('type', '')).strip()
            if not word:
                add('empty-word', 'num %s' % num)
            if not meaning:
                add('empty-meaning', 'num %s (%s)' % (num, word))
            elif len(meaning) < 2:
                add('short-meaning', 'num %s (%s) = %r' % (num, word, meaning))
            if word.lower() == meaning.lower():
                add('word-eq-meaning', 'num %s (%s)' % (num, word))
            if meaning != w.get('meaning', ''):
                add('meaning-whitespace', 'num %s (%s)' % (num, word))
            if len(meaning) > 110:
                add('long-meaning', 'num %s (%s) len=%d' % (num, word, len(meaning)))
            if len(word) > 45:
                add('long-word', 'num %s len=%d' % (num, len(word)))
            if re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', word + meaning):
                add('control-chars', 'num %s (%s)' % (num, word))
            if phon and not (phon.startswith('/') and phon.endswith('/')):
                add('phon-format', 'num %s (%s) phon=%r' % (num, word, phon))
            if typ and (len(typ) > 15 or re.search(r'\d', typ)):
                add('type-format', 'num %s (%s) type=%r' % (num, word, typ))

        lines.append('## %s — %d entries' % (name, len(words)))
        lines.append('')
        if not issues:
            lines.append('No issues found.')
        for cat in sorted(issues):
            items = issues[cat]
            total_issues += len(items)
            lines.append('- **%s** (%d):' % (cat, len(items)))
            for it in items[:15]:
                lines.append('  - %s' % it)
            if len(items) > 15:
                lines.append('  - … and %d more' % (len(items) - 15))
        lines.append('')

    total_batches = 0
    lines.append('## Review batches (size 150)')
    lines.append('')
    for name in FILES:
        n = len(load(name))
        nb = (n + 149) // 150
        total_batches += nb
        lines.append('- %s: %d entries → %d batches' % (name, n, nb))
    lines.append('- TOTAL: %d batches' % total_batches)

    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    print('ISSUES:', total_issues)
    print('BATCHES:', total_batches)
    print('WROTE', OUT)


if __name__ == '__main__':
    main()
