# build.py - Build single-file vocab web app
# Usage: python tools/build.py
# Reads src/data/*.json + src/template.html -> writes index.html at repo root
import io
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src')
TEMPLATE = os.path.join(SRC, 'template.html')
OUT = os.path.join(ROOT, 'index.html')
EXDIR = os.path.join(SRC, 'data', 'ex')

DATASETS = [
    ('en1k', 'en'),
    ('en3k', 'en'),
    ('de3k', 'de'),
]
GRAMMAR_PATH = os.path.join(SRC, 'data', 'grammar.json')
DE_A1_PATH = os.path.join(SRC, 'data', 'de_a1.json')
DE_TOPICS_PATH = os.path.join(SRC, 'data', 'de_topics.json')


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


def load_examples(name, words):
    path = os.path.join(EXDIR, name + '.json')
    if not os.path.exists(path):
        return {}
    with io.open(path, encoding='utf-8') as f:
        raw = json.load(f)
    if not isinstance(raw, dict):
        raise SystemExit('EX BAD ROOT in %s' % name)
    by_num = {w['num']: w for w in words}
    out = {}
    for k, items in raw.items():
        try:
            num = int(k)
        except (TypeError, ValueError):
            raise SystemExit('EX BAD NUM in %s: %r' % (name, k))
        if num not in by_num:
            raise SystemExit('EX UNKNOWN NUM in %s: %s' % (name, num))
        if not isinstance(items, list) or not items:
            continue
        clean = []
        for it in items:
            if not isinstance(it, dict):
                raise SystemExit('EX BAD ITEM in %s num %s' % (name, num))
            s = str(it.get('s', '')).strip()
            t = str(it.get('t', '')).strip()
            if not s or not t:
                raise SystemExit('EX EMPTY in %s num %s' % (name, num))
            clean.append({'s': s, 't': t})
        out[num] = clean
    return out


def load_de_topics():
    with io.open(DE_TOPICS_PATH, encoding='utf-8') as f:
        topics = json.load(f)
    if not isinstance(topics, list) or not topics:
        raise SystemExit('DE TOPICS: empty')
    ids = []
    for t in topics:
        for k in ('id', 'name', 'short'):
            if not str(t.get(k, '')).strip():
                raise SystemExit('DE TOPICS: missing %s' % k)
        ids.append(t['id'])
    if len(ids) != len(set(ids)):
        raise SystemExit('DE TOPICS: duplicate ids')
    return topics


def load_de_a1(topic_ids):
    with io.open(DE_A1_PATH, encoding='utf-8') as f:
        words = json.load(f)
    if not isinstance(words, list) or not words:
        raise SystemExit('DE A1: empty')
    seen = set()
    for w in words:
        for k in ('num', 'word', 'meaning', 'type'):
            if not str(w.get(k, '')).strip():
                raise SystemExit('DE A1: missing %s in %s' % (k, json.dumps(w, ensure_ascii=False)))
        w['num'] = int(w['num'])
        if w['num'] in seen:
            raise SystemExit('DE A1: dup num %s' % w['num'])
        seen.add(w['num'])
        topics = w.get('topics')
        if not isinstance(topics, list) or not topics:
            raise SystemExit('DE A1: no topics in %s' % w['word'])
        for t in topics:
            if t not in topic_ids:
                raise SystemExit('DE A1: bad topic %s in %s' % (t, w['word']))
        w['topics'] = list(dict.fromkeys(topics))
        w.setdefault('phon', '')
    return words


def meaning_parts(text):
    clean = re.sub(r'\([^)]*\)', ' ', str(text or ''))
    parts = [p.strip().lower() for p in re.split(r'[;,/|]', clean)]
    return [p for p in parts if p]


def meanings_overlap(a, b):
    pa, pb = meaning_parts(a), meaning_parts(b)
    for x in pa:
        for y in pb:
            if x == y:
                return True
            if len(x) >= 2 and len(y) >= 2 and (x in y or y in x):
                return True
    return False


def merge_de(words, a1):
    """Merge the A1 topic list into the German dataset.

    Same word + same POS is folded into one entry (topics and meanings merged);
    a word with a different POS stays a separate entry, as in the English sets.
    """
    index = {}
    used = set()
    for w in words:
        index.setdefault(norm_word(w['word']), []).append(w)
        used.add(w['num'])
    for rec in a1:
        key = norm_word(rec['word'])
        target = None
        for cand in index.get(key, []):
            if cand.get('type', '') == rec['type']:
                target = cand
                break
        if target:
            for t in rec['topics']:
                target.setdefault('topics', [])
                if t not in target['topics']:
                    target['topics'].append(t)
            if rec.get('extra'):
                if not target.get('extra'):
                    target['extra'] = rec['extra']
                target['meaning'] = re.sub(r'\s*\(Pl[^)]*\)', '', target['meaning']).strip()
            if not meanings_overlap(target['meaning'], rec['meaning']):
                target['meaning'] = target['meaning'] + ' · ' + rec['meaning']
            if rec.get('ex'):
                ex = target.setdefault('ex', [])
                for x in rec['ex']:
                    if not any(y.get('s') == x.get('s') for y in ex):
                        ex.append(x)
        else:
            new = {
                'num': rec['num'],
                'word': rec['word'],
                'meaning': rec['meaning'],
                'type': rec['type'],
                'phon': '',
                'topics': list(rec['topics']),
            }
            if rec.get('extra'):
                new['extra'] = rec['extra']
            if rec.get('ex'):
                new['ex'] = list(rec['ex'])
            if rec['num'] in used:
                raise SystemExit('DE MERGE: num collision %s' % rec['num'])
            used.add(rec['num'])
            words.append(new)
            index.setdefault(key, []).append(new)
    for w in words:
        w.setdefault('topics', [])
    return words


def norm_word(s):
    return re.sub(r'\s+', ' ', str(s or '')).strip().lower()


def load_grammar():
    with io.open(GRAMMAR_PATH, encoding='utf-8') as f:
        g = json.load(f)
    topics = g.get('topics')
    if not isinstance(topics, list) or not topics:
        raise SystemExit('GRAMMAR: no topics')
    ids = [t.get('id') for t in topics]
    if len(ids) != len(set(ids)):
        raise SystemExit('GRAMMAR: duplicate ids')
    lex = g.get('lexicon') or {}
    times = lex.get('times') or {}
    patterns = lex.get('patterns') or {}
    bank = int(g.get('bankPerTopic') or 0)
    if bank <= 0:
        raise SystemExit('GRAMMAR: bad bankPerTopic')

    for bank_id, p in patterns.items():
        if not isinstance(p, dict):
            raise SystemExit('GRAMMAR: bad pattern %s' % bank_id)
        tpls = p.get('templates')
        dims = p.get('dims')
        slots = p.get('slots')
        if not isinstance(tpls, list) or not tpls or not all(isinstance(x, str) and x.strip() for x in tpls):
            raise SystemExit('GRAMMAR: bad templates in %s' % bank_id)
        if not isinstance(dims, list) or not dims or len(dims) != len(set(dims)):
            raise SystemExit('GRAMMAR: bad dims in %s' % bank_id)
        if not isinstance(slots, dict):
            raise SystemExit('GRAMMAR: bad slots in %s' % bank_id)
        fields = set()
        total = len(tpls)
        for dim in dims:
            vals = slots.get(dim)
            if not isinstance(vals, list) or not vals:
                raise SystemExit('GRAMMAR: empty dim %r in %s' % (dim, bank_id))
            total *= len(vals)
            first = vals[0]
            if isinstance(first, dict):
                if not first or not all(isinstance(k, str) and isinstance(v, str) and v.strip() for k, v in first.items()):
                    raise SystemExit('GRAMMAR: bad object slot %r in %s' % (dim, bank_id))
                for v in vals:
                    if not isinstance(v, dict) or set(v) != set(first):
                        raise SystemExit('GRAMMAR: inconsistent slot %r in %s' % (dim, bank_id))
                    if not all(isinstance(x, str) and x.strip() for x in v.values()):
                        raise SystemExit('GRAMMAR: bad value %r in %s' % (dim, bank_id))
                fields.update(dim + '_' + k.upper() for k in first)
            elif isinstance(first, str):
                if not first.strip() or not all(isinstance(v, str) and v.strip() for v in vals):
                    raise SystemExit('GRAMMAR: bad scalar slot %r in %s' % (dim, bank_id))
                fields.add(dim)
            else:
                raise SystemExit('GRAMMAR: bad slot type %r in %s' % (dim, bank_id))
        if total < bank:
            raise SystemExit('GRAMMAR: pattern %s only %d < %d' % (bank_id, total, bank))
        for tpl in tpls:
            for key in set(re.findall(r'\{(\w+)\}', tpl)):
                if key not in fields:
                    raise SystemExit('GRAMMAR: unknown placeholder %r in %s' % (key, bank_id))

    for t in topics:
        for k in ('id', 'cat', 'level', 'title', 'vi', 'formula', 'use'):
            if not str(t.get(k, '')).strip():
                raise SystemExit('GRAMMAR: missing %s in %s' % (k, t.get('id')))
        if not t.get('examples') or not t.get('mistakes'):
            raise SystemExit('GRAMMAR: examples/mistakes missing in %s' % t['id'])
        gen = t.get('gen')
        if gen:
            if gen.get('bank'):
                if gen['bank'] not in patterns:
                    raise SystemExit('GRAMMAR: bad gen bank %r in %s' % (gen['bank'], t['id']))
            else:
                tense = gen.get('tense')
                if tense not in times:
                    raise SystemExit('GRAMMAR: bad gen tense %r in %s' % (tense, t['id']))
    return g


def grammar_capacity(g, topic):
    gen = topic.get('gen') or {}
    if not gen:
        return 0
    if gen.get('bank'):
        p = g['lexicon']['patterns'][gen['bank']]
        n = len(p['templates'])
        for dim in p['dims']:
            n *= len(p['slots'][dim])
        return n
    return int(g.get('bankPerTopic') or 0)


def main():
    data = {}
    counts = []
    ex_stats = []
    de_topics = load_de_topics()
    de_a1 = load_de_a1({t['id'] for t in de_topics})
    de_a1_ex = load_examples('de_a1', de_a1)
    for w in de_a1:
        items = de_a1_ex.get(w['num'])
        if items:
            w['ex'] = items
    for name, lang in DATASETS:
        words = load(name)
        ex = load_examples(name, words)
        for w in words:
            items = ex.get(w['num'])
            if items:
                w['ex'] = items
        if name == 'de3k':
            words = merge_de(words, de_a1)
        else:
            for w in words:
                w.setdefault('topics', [])
        ex_stats.append((name,
                         sum(1 for w in words if w.get('ex')),
                         sum(len(w.get('ex') or []) for w in words)))
        data[name] = {'lang': lang, 'words': words}
        counts.append((name, len(words)))

    used = {}
    for w in data['de3k']['words']:
        for t in w['topics']:
            used[t] = used.get(t, 0) + 1
    for t in de_topics:
        t['count'] = used.get(t['id'], 0)
        if not t['count']:
            raise SystemExit('DE TOPICS: no words for %s' % t['id'])
    data['de3k']['topics'] = de_topics
    if len(data['de3k']['words']) != len({w['num'] for w in data['de3k']['words']}):
        raise SystemExit('DE MERGE: duplicate nums')
    blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    if '</script' in blob.lower():
        raise SystemExit('UNSAFE: </script found in data blob')
    grammar = load_grammar()
    gblob = json.dumps(grammar, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    if '</script' in gblob.lower():
        raise SystemExit('UNSAFE: </script found in grammar blob')
    with io.open(TEMPLATE, encoding='utf-8') as f:
        tpl = f.read()
    if '__DATA_JSON__' not in tpl:
        raise SystemExit('TEMPLATE PLACEHOLDER MISSING')
    if '__GRAMMAR_JSON__' not in tpl:
        raise SystemExit('TEMPLATE GRAMMAR PLACEHOLDER MISSING')
    html = tpl.replace('__DATA_JSON__', blob).replace('__GRAMMAR_JSON__', gblob)
    assert '__DATA_JSON__' not in html
    assert '__GRAMMAR_JSON__' not in html
    with io.open(OUT, 'w', encoding='utf-8', newline='\n') as f:
        f.write(html)
    for name, n in counts:
        print('%-6s %5d words' % (name, n))
    for name, nw, ne in ex_stats:
        print('%-6s %5d words with examples, %d sentences' % (name, nw, ne))
    print('grammar %d topics, %d with bank, %d sentences' % (
        len(grammar['topics']),
        sum(1 for t in grammar['topics'] if t.get('gen')),
        sum(grammar_capacity(grammar, t) for t in grammar['topics'])))
    print('WROTE %s (%d bytes)' % (OUT, os.path.getsize(OUT)))


if __name__ == '__main__':
    main()
