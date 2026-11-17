import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import build  # noqa: E402


def main():
    topics = build.load_de_topics()
    a1 = build.load_de_a1({t['id'] for t in topics})
    words = build.load('de3k')
    ex = build.load_examples('de3k', words)
    for w in words:
        items = ex.get(w['num'])
        if items:
            w['ex'] = items
    merged = build.merge_de(words, a1)
    missing = [w for w in merged if not w.get('ex')]
    print('merged %d words, missing examples %d' % (len(merged), len(missing)))
    for w in missing[:10]:
        print('  ', w['num'], w['word'], '|', w['meaning'])
    out = os.path.join(ROOT, 'report', 'de-a1-missing-nums.txt')
    with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(','.join(str(w['num']) for w in missing) + '\n')
    print('wrote', out)


if __name__ == '__main__':
    main()
