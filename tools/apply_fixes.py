# apply_fixes.py - merge report/fixes/*.json into src/data/*.json
# Usage: python tools/apply_fixes.py
# - applies fixes by num, verifying old_meaning matches (safety)
# - rewrites data files in same format (1 entry per line)
# - writes report/nghia-review.md changelog
import io
import json
import os
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'src', 'data')
FIXDIR = os.path.join(ROOT, 'report', 'fixes')
OUT = os.path.join(ROOT, 'report', 'nghia-review.md')

FILES = ['en1k.json', 'en3k.json', 'de3k.json']


def read_json(fp):
    with io.open(fp, encoding='utf-8') as f:
        return json.load(f)


def write_words(fp, words):
    body = '[\n' + ',\n'.join('  ' + json.dumps(w, ensure_ascii=False) for w in words) + '\n]\n'
    with io.open(fp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(body)


def main():
    data = {}
    for name in FILES:
        data[name] = read_json(os.path.join(DATA, name))
    index = {name: {w['num']: w for w in data[name]} for name in FILES}

    applied = []
    skipped = []
    fix_files = sorted(glob.glob(os.path.join(FIXDIR, '*.json')))
    if not fix_files:
        print('No fix files found.')
        return

    for fp in fix_files:
        batch = os.path.basename(fp).replace('.json', '')
        rec = read_json(fp)
        name = rec.get('file')
        if name not in index:
            skipped.append('%s: unknown file %r' % (batch, name))
            continue
        for fix in rec.get('fixes', []):
            num = fix.get('num')
            entry = index[name].get(num)
            old = fix.get('old_meaning')
            relocated_from = None
            if entry is not None and old is not None and entry.get('meaning') != old:
                entry = None
            if entry is None:
                # relocation: find unique entry matching word + old_meaning (agents sometimes mislabel num)
                wfix = str(fix.get('word', '')).strip().lower()
                cands = [w for w in data[name]
                         if str(w.get('word', '')).strip().lower() == wfix and old is not None and w.get('meaning') == old]
                if len(cands) == 1:
                    entry = cands[0]
                    relocated_from = num
                    num = entry['num']
                else:
                    if old is None:
                        skipped.append('%s: num %s not found in %s' % (batch, num, name))
                    else:
                        skipped.append('%s: num %s (%s) old_meaning mismatch, relocation failed (cands=%d)\n    file entry has: %r\n    fix wants old: %r'
                                       % (batch, num, fix.get('word'), len(cands),
                                          index[name].get(fix.get('num'), {}).get('meaning'), old))
                    continue
            changed = []
            for src_key, dst_key in (('new_word', 'word'), ('new_type', 'type'),
                                     ('new_phon', 'phon'), ('new_meaning', 'meaning')):
                if src_key in fix and fix[src_key] is not None:
                    new_val = str(fix[src_key]).strip()
                    if new_val and entry.get(dst_key, '') != new_val:
                        changed.append((dst_key, entry.get(dst_key, ''), new_val))
                        entry[dst_key] = new_val
            if not changed:
                skipped.append('%s: num %s (%s) no effective change' % (batch, num, entry.get('word')))
                continue
            applied.append({
                'batch': batch, 'file': name, 'num': num, 'word': entry.get('word'),
                'reason': fix.get('reason', ''), 'relocated_from': relocated_from,
                'changed': changed,
            })

    for name in FILES:
        write_words(os.path.join(DATA, name), data[name])

    lines = ['# Review nghĩa từ vựng — changelog', '']
    lines.append('Applied: **%d** fixes · Skipped: **%d** · Batches processed: **%d**' % (len(applied), len(skipped), len(fix_files)))
    lines.append('')
    for name in FILES:
        rows = [a for a in applied if a['file'] == name]
        lines.append('## %s — %d fixes' % (name, len(rows)))
        lines.append('')
        if not rows:
            lines.append('_(no changes)_')
            lines.append('')
            continue
        lines.append('| num | word | field | old | new | reason | batch |')
        lines.append('|---|---|---|---|---|---|---|')
        for a in rows:
            for field, old_v, new_v in a['changed']:
                esc = lambda s: str(s).replace('|', '\\|').replace('\n', ' ')
                lines.append('| %s | %s | %s | %s | %s | %s | %s |' % (
                    a['num'], esc(a['word']), field, esc(old_v), esc(new_v), esc(a['reason']), a['batch']))
        lines.append('')

    if skipped:
        lines.append('## Skipped')
        lines.append('')
        for s in skipped:
            lines.append('- %s' % s.replace('\n', '\n  '))
        lines.append('')

    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')

    print('APPLIED:', len(applied))
    print('SKIPPED:', len(skipped))
    for s in skipped[:15]:
        print('  SKIP:', s)
    print('WROTE', OUT)


if __name__ == '__main__':
    main()
