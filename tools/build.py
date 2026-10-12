# build.py - Build single-file vocab web app
# Usage: python tools/build.py
# Reads src/data/*.json + src/template.html -> writes index.html at repo root
import io
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src')
TEMPLATE = os.path.join(SRC, 'template.html')
OUT = os.path.join(ROOT, 'index.html')

DATASETS = [
    ('en1k', 'en'),
    ('en3k', 'en'),
    ('de3k', 'de'),
]


def load(name):
    path = os.path.join(SRC, 'data', name + '.json')
    with io.open(path, encoding='utf-8') as f:
        words = json.load(f)
    for w in words:
        for k in ('num', 'word', 'meaning'):
            if k not in w or not str(w[k]).strip():
                raise SystemExit('BAD ENTRY in %s: %s' % (name, json.dumps(w, ensure_ascii=False)))
        w['num'] = int(w['num'])
        w.setdefault('type', '')
        w.setdefault('phon', '')
    nums = [w['num'] for w in words]
    if len(nums) != len(set(nums)):
        seen, dup = set(), []
        for n in nums:
            if n in seen and n not in dup:
                dup.append(n)
            seen.add(n)
        raise SystemExit('DUP NUMS in %s: %s' % (name, dup[:10]))
    return words


def main():
    data = {}
    counts = []
    for name, lang in DATASETS:
        words = load(name)
        data[name] = {'lang': lang, 'words': words}
        counts.append((name, len(words)))
    blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    if '</script' in blob.lower():
        raise SystemExit('UNSAFE: </script found in data blob')
    with io.open(TEMPLATE, encoding='utf-8') as f:
        tpl = f.read()
    if '__DATA_JSON__' not in tpl:
        raise SystemExit('TEMPLATE PLACEHOLDER MISSING')
    html = tpl.replace('__DATA_JSON__', blob)
    assert '__DATA_JSON__' not in html
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write(html)
    for name, n in counts:
        print('%-6s %5d words' % (name, n))
    print('WROTE %s (%d bytes)' % (OUT, os.path.getsize(OUT)))


if __name__ == '__main__':
    main()
