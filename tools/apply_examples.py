# apply_examples.py - merge report/examples/*.json batches into src/data/ex/*.json
# Batch format:
#   {"file":"en1k","batch":"b01","items":[{"num":1,"ex":[{"s":"...","t":"..."}]}, ...]}
# Later batches override an identical num (use for corrections); conflicts are reported.
# Usage: python tools/apply_examples.py
import glob
import io
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'src', 'data')
EXDIR = os.path.join(DATA, 'ex')
BATCHDIR = os.path.join(ROOT, 'report', 'examples')
FILES = ['en1k', 'en3k', 'de3k']


def read_json(fp):
    with io.open(fp, encoding='utf-8') as f:
        return json.load(f)


def word_nums(name):
    words = read_json(os.path.join(DATA, name + '.json'))
    return {int(w['num']) for w in words}


def validate_items(name, num, items):
    if not isinstance(items, list) or not items:
        raise SystemExit('%s num %s: ex must be a non-empty list' % (name, num))
    out = []
    for it in items:
        if not isinstance(it, dict):
            raise SystemExit('%s num %s: bad item' % (name, num))
        s = str(it.get('s', '')).strip()
        t = str(it.get('t', '')).strip()
        if not s or not t:
            raise SystemExit('%s num %s: empty s/t' % (name, num))
        if '</script' in (s + t).lower():
            raise SystemExit('%s num %s: unsafe </script' % (name, num))
        out.append({'s': s, 't': t})
    return out


def main():
    os.makedirs(EXDIR, exist_ok=True)
    nums = {name: word_nums(name) for name in FILES}
    merged = {name: {} for name in FILES}
    origin = {name: {} for name in FILES}
    conflicts = []
    files = sorted(glob.glob(os.path.join(BATCHDIR, '*.json')))
    if not files:
        print('No example batches found.')
    for fp in files:
        rec = read_json(fp)
        name = rec.get('file')
        if name not in FILES:
            raise SystemExit('%s: unknown file %r' % (os.path.basename(fp), name))
        batch = rec.get('batch') or os.path.basename(fp)
        for item in rec.get('items', []):
            try:
                num = int(item.get('num'))
            except (TypeError, ValueError):
                raise SystemExit('%s: bad num %r' % (batch, item.get('num')))
            if num not in nums[name]:
                raise SystemExit('%s: num %s not in %s' % (batch, num, name))
            items = validate_items(name, num, item.get('ex'))
            if num in merged[name] and merged[name][num] != items:
                conflicts.append('%s: num %s overridden by %s (was %s)' % (name, num, batch, origin[name].get(num)))
            merged[name][num] = items
            origin[name][num] = batch
    for name in FILES:
        data = merged[name]
        body = '{\n' + ',\n'.join(
            '  %s: %s' % (json.dumps(str(k)), json.dumps(data[k], ensure_ascii=False))
            for k in sorted(data)
        ) + '\n}\n' if data else '{}\n'
        out = os.path.join(EXDIR, name + '.json')
        with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
            f.write(body)
        n_sent = sum(len(v) for v in data.values())
        print('%-6s %5d words, %6d sentences -> %s' % (name, len(data), n_sent, out))
    if conflicts:
        print('CONFLICTS: %d' % len(conflicts))
        for c in conflicts[:20]:
            print('  ' + c)


if __name__ == '__main__':
    main()
