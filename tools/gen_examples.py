# gen_examples.py - generate example sentences via the DeepSeek API (OpenAI-compatible)
# Usage:
#   python tools/gen_examples.py --dataset en1k --limit 10 --count 3 --batch 10
#   python tools/gen_examples.py --dataset en1k
#   python tools/gen_examples.py --all
# Writes report/examples/<ds>-auto-bNNN.json batches. Does NOT modify src/data.
# The API key is read from the local opencode config; it is never printed.
import argparse
import glob
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'src', 'data')
EXDIR = os.path.join(DATA, 'ex')
BATCHDIR = os.path.join(ROOT, 'report', 'examples')
CFG = os.path.join(os.path.expanduser('~'), '.config', 'opencode', 'opencode.jsonc')
LOG = os.path.join(ROOT, 'report', 'examples-gen.log')

DATASETS = {
    'en1k': {'lang': 'English', 'count': 3},
    'en3k': {'lang': 'English', 'count': 2},
    'de3k': {'lang': 'German', 'count': 2},
}

DE_MARKERS = set('der die das den dem des ein eine einen einem einer und ist sind war nicht mit auf für von zu im am ich du er sie es wir ihr sich mein dein sein ihre hat habe haben wird werden kann können muss sehr auch aber oder wenn dass wie was wo kein keine zum zur vom beim'.split())
EN_MARKERS = set('the and is are was were a an to of in on at for with this that these those i you he she it we they my your his her its our their have has had do does did not but or if when where what who how can will would should could may might must'.split())


def marker_score(s, markers):
    ws = re.findall(r"[A-Za-zÀ-ÿß']+", s.lower())
    return sum(1 for w in ws if w in markers)


def language_ok(s, lang):
    de = marker_score(s, DE_MARKERS)
    en = marker_score(s, EN_MARKERS)
    if lang == 'English':
        if de >= 3 and de > en:
            return False
        if re.search(r'[äöüßÄÖÜ]', s) and de >= 1 and de >= en:
            return False
        return True
    if lang == 'German':
        if en >= 4 and en > de + 1:
            return False
        return True
    return True


def parse_nums(spec):
    out = set()
    for part in spec.split(','):
        part = part.strip()
        if not part:
            continue
        if '-' in part:
            a, b = part.split('-', 1)
            out.update(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    return out


def read_json(fp):
    with io.open(fp, encoding='utf-8') as f:
        return json.load(f)


def load_key():
    with io.open(CFG, encoding='utf-8-sig') as f:
        cfg = json.load(f)
    key = cfg.get('provider', {}).get('deepseek', {}).get('options', {}).get('apiKey')
    if not key:
        raise SystemExit('No DeepSeek API key in opencode config')
    return key


def log(msg):
    line = time.strftime('%Y-%m-%d %H:%M:%S') + '  ' + msg
    print(line)
    try:
        with io.open(LOG, 'a', encoding='utf-8', newline='\n') as f:
            f.write(line + '\n')
    except Exception:
        pass


def covered_nums(ds):
    nums = set()
    ex_path = os.path.join(EXDIR, ds + '.json')
    if os.path.exists(ex_path):
        try:
            nums |= {int(k) for k in read_json(ex_path).keys()}
        except Exception:
            pass
    for fp in glob.glob(os.path.join(BATCHDIR, ds + '-*.json')):
        try:
            rec = read_json(fp)
            for it in rec.get('items', []):
                try:
                    nums.add(int(it.get('num')))
                except (TypeError, ValueError):
                    pass
        except Exception:
            pass
    return nums


def build_prompt(words, lang, count):
    lines = []
    for w in words:
        lines.append('%s | %s | %s | %s' % (w['num'], w['word'], w.get('type', ''), w['meaning']))
    return (
        'You write example sentences for a Vietnamese learner vocabulary app.\n'
        'Language of the sentences: %s. Translation language: Vietnamese.\n'
        'CRITICAL: every "s" value MUST be written in %s only. Never write a sentence in another language. '
        'A sentence in another language is invalid and will be rejected.\n'
        'For EACH word below, write exactly %d example sentences. Each sentence must contain the target word '
        '(or a natural inflected form). Then translate the sentence accurately into Vietnamese.\n'
        'Rules:\n'
        '- Sentences: natural, 6-18 words, A2-B1 level, varied contexts.\n'
        '- One sentence per common sense where possible; no duplicates.\n'
        '- German nouns: use the article in the sentence. German separable verbs may split naturally.\n'
        '- Do not add numbering inside s. Do not add explanations.\n'
        '- Return JSON only, exactly this shape: {"items":[{"num":1,"ex":[{"s":"...","t":"..."}]}]}\n'
        'Words (num | word | type | meaning):\n' + '\n'.join(lines)
    )


def call_api(key, prompt, max_tokens, temp, lang):
    body = {
        'model': 'deepseek-chat',
        'messages': [
            {'role': 'system', 'content': 'You are a careful bilingual lexicographer. Output valid JSON only. Every example sentence must be written in ' + lang + ', never in another language.'},
            {'role': 'user', 'content': prompt},
        ],
        'temperature': temp,
        'max_tokens': max_tokens,
        'response_format': {'type': 'json_object'},
    }
    req = urllib.request.Request(
        'https://api.deepseek.com/chat/completions',
        data=json.dumps(body).encode('utf-8'),
        headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json'},
        method='POST',
    )
    with urllib.request.urlopen(req, timeout=240) as r:
        raw = r.read().decode('utf-8', 'replace')
    rec = json.loads(raw)
    choice = rec['choices'][0]
    content = choice.get('message', {}).get('content') or ''
    return content, choice.get('finish_reason'), rec.get('usage', {})


def parse_items(content):
    text = content.strip()
    text = re.sub(r'^```(?:json)?\s*', '', text)
    text = re.sub(r'\s*```$', '', text)
    start = text.find('{')
    end = text.rfind('}')
    if start < 0 or end < 0 or end <= start:
        raise ValueError('no JSON object in response')
    obj = json.loads(text[start:end + 1])
    items = obj.get('items')
    if not isinstance(items, list):
        raise ValueError('missing items')
    return items


def validate(words, items, count, lang):
    want = {w['num']: w for w in words}
    good = {}
    errors = []
    for it in items:
        try:
            num = int(it.get('num'))
        except (TypeError, ValueError):
            errors.append('bad num')
            continue
        if num not in want:
            errors.append('unknown num %s' % num)
            continue
        ex = it.get('ex')
        if not isinstance(ex, list):
            errors.append('%s: ex not list' % num)
            continue
        clean = []
        seen = set()
        for x in ex:
            if not isinstance(x, dict):
                continue
            s = str(x.get('s', '')).strip()
            t = str(x.get('t', '')).strip()
            if not s or not t or len(s) < 6 or len(t) < 3:
                continue
            if s in seen:
                continue
            if '</script' in (s + t).lower() or '\n' in s or '\n' in t:
                continue
            if not language_ok(s, lang):
                continue
            seen.add(s)
            clean.append({'s': s, 't': t})
        if len(clean) < count:
            errors.append('%s: only %d/%d valid examples' % (num, len(clean), count))
            continue
        good[num] = clean[:count]
    missing = [n for n in want if n not in good]
    return good, missing, errors


def gen_batch(key, ds, words, count, max_tokens, temp, tries=3):
    prompt = build_prompt(words, DATASETS[ds]['lang'], count)
    last = ''
    for attempt in range(1, tries + 1):
        try:
            content, finish, usage = call_api(key, prompt, max_tokens, temp, DATASETS[ds]['lang'])
            items = parse_items(content)
            good, missing, errors = validate(words, items, count, DATASETS[ds]['lang'])
            if not missing:
                return good, usage
            last = 'missing=%s errors=%s' % (missing[:8], errors[:5])
            log('  attempt %d: %s' % (attempt, last))
        except Exception as e:
            last = str(e)
            log('  attempt %d error: %s' % (attempt, last))
        time.sleep(2 * attempt)
    return {}, {'error': last}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dataset', choices=list(DATASETS.keys()))
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--limit', type=int, default=0, help='max words this run (0 = all missing)')
    ap.add_argument('--batch', type=int, default=30)
    ap.add_argument('--count', type=int, default=0, help='examples per word (default per dataset)')
    ap.add_argument('--max-tokens', type=int, default=8000)
    ap.add_argument('--nums', help='force regeneration for num ranges, e.g. 641-680,900')
    ap.add_argument('--temp', type=float, default=0.65)
    args = ap.parse_args()
    if not args.all and not args.dataset:
        raise SystemExit('Need --dataset or --all')
    key = load_key()
    os.makedirs(BATCHDIR, exist_ok=True)
    ds_list = list(DATASETS.keys()) if args.all else [args.dataset]
    for ds in ds_list:
        count = args.count or DATASETS[ds]['count']
        words = read_json(os.path.join(DATA, ds + '.json'))
        done = covered_nums(ds)
        force = parse_nums(args.nums) if args.nums else None
        if force is not None:
            todo = [w for w in words if int(w['num']) in force]
            prefix = 'fix'
        else:
            todo = [w for w in words if int(w['num']) not in done]
            prefix = 'auto'
        if args.limit:
            todo = todo[:args.limit]
        log('%s: %d words, %d already covered, %d to generate (count=%d, temp=%s)' % (ds, len(words), len(done), len(todo), count, args.temp))
        start = 0
        while start < len(todo):
            chunk = todo[start:start + args.batch]
            start += len(chunk)
            tag = '%s-%s-%04d-%04d' % (ds, prefix, int(chunk[0]['num']), int(chunk[-1]['num']))
            out = os.path.join(BATCHDIR, tag + '.json')
            if os.path.exists(out):
                log('  skip existing %s' % os.path.basename(out))
                continue
            t0 = time.time()
            good, usage = gen_batch(key, ds, chunk, count, args.max_tokens, args.temp)
            if len(good) < len(chunk):
                fail = [w for w in chunk if int(w['num']) not in good]
                log('  partial batch %s: %d/%d, retrying missing in smaller chunks' % (tag, len(good), len(chunk)))
                if good:
                    write_batch(ds, tag + '-part', good)
                half = (len(fail) + 1) // 2
                for j, sub in enumerate((fail[:half], fail[half:])):
                    if not sub:
                        continue
                    sub_tag = '%s-fix%d-%04d-%04d' % (tag, j + 1, int(sub[0]['num']), int(sub[-1]['num']))
                    sub_good, sub_usage = gen_batch(key, ds, sub, count, args.max_tokens, args.temp)
                    if sub_good:
                        write_batch(ds, sub_tag, sub_good)
                    log('  %s: %d/%d' % (sub_tag, len(sub_good), len(sub)))
                    time.sleep(0.6)
            else:
                write_batch(ds, tag, good)
            log('  wrote %s (%d words) in %.1fs %s' % (tag, len(good), time.time() - t0, usage.get('total_tokens', '')))
            time.sleep(0.6)


def write_batch(ds, tag, good):
    items = [{'num': n, 'ex': good[n]} for n in sorted(good)]
    rec = {'file': ds, 'batch': tag, 'items': items}
    out = os.path.join(BATCHDIR, tag + '.json')
    with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(rec, ensure_ascii=False, separators=(',', ':')) + '\n')


if __name__ == '__main__':
    main()
