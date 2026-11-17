# gen_de_topics.py - extract German A1 vocabulary from the Word handbook
# into src/data/de_a1.json (words with topic tags) + src/data/de_topics.json
# Usage: python tools/gen_de_topics.py
import io
import json
import os
import re
import sys

try:
    import docx
except ImportError:
    sys.exit('need python-docx (pip install python-docx)')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCX = os.path.join(os.path.expanduser('~'), 'Downloads', 'Tu-vung-tieng-Duc-A1-theo-chu-de.docx')
OUT_WORDS = os.path.join(ROOT, 'src', 'data', 'de_a1.json')
OUT_TOPICS = os.path.join(ROOT, 'src', 'data', 'de_topics.json')

TOPICS = [
    ('01', 'Chào hỏi và thông tin cá nhân', 'Chào hỏi'),
    ('02', 'Gia đình và quan hệ', 'Gia đình'),
    ('03', 'Nhà cửa và đồ dùng', 'Nhà cửa'),
    ('04', 'Đồ ăn và thức uống', 'Đồ ăn'),
    ('05', 'Quán ăn và gọi món', 'Quán ăn'),
    ('06', 'Mua sắm, tiền bạc và quần áo', 'Mua sắm'),
    ('07', 'Thành phố và địa điểm', 'Thành phố'),
    ('08', 'Phương tiện và du lịch', 'Du lịch'),
    ('09', 'Sinh hoạt hằng ngày', 'Hằng ngày'),
    ('10', 'Trường học và công việc', 'Học & làm'),
    ('11', 'Sở thích và thể thao', 'Sở thích'),
    ('12', 'Thời tiết và thiên nhiên', 'Thời tiết'),
    ('13', 'Cơ thể và sức khỏe', 'Sức khỏe'),
    ('14', 'Cảm xúc và trạng thái', 'Cảm xúc'),
    ('15', 'Quốc gia, quốc tịch và ngôn ngữ', 'Quốc gia'),
    ('16', 'Lịch và thời gian', 'Lịch'),
    ('17', 'Động từ thiết yếu', 'Động từ'),
    ('18', 'Tính từ và trạng từ', 'Tính từ'),
    ('19', 'Màu sắc', 'Màu sắc'),
    ('20', 'Từ để hỏi, đại từ và từ chỉ định', 'Đại từ'),
    ('21', 'Giới từ, liên từ và từ phủ định', 'Giới từ'),
    ('22', 'Cụm giao tiếp thường dùng', 'Giao tiếp'),
    ('23', 'Số đếm tham khảo', 'Số đếm'),
    ('24', 'Nói giờ và mốc thời gian', 'Nói giờ'),
]
TOPIC_NAME = {t[0]: t[1] for t in TOPICS}

# table index -> (topic id, kind)
TABLE_MAP = {
    3: ('01', 'noun'), 4: ('02', 'noun'), 5: ('03', 'noun'), 6: ('04', 'noun'),
    7: ('05', 'noun'), 8: ('06', 'noun'), 9: ('07', 'noun'), 10: ('08', 'noun'),
    11: ('09', 'noun'), 12: ('10', 'noun'), 13: ('11', 'noun'), 14: ('12', 'noun'),
    15: ('13', 'noun'), 16: ('14', 'noun'),
    17: ('15', 'noun'), 18: ('15', 'country'), 19: ('15', 'language'), 20: ('15', 'people'),
    21: ('16', 'noun'),
    22: ('17', 'verb'),
    23: ('18', 'adjadv'),
    24: ('19', 'color'),
    25: ('20', 'pron'),
    26: ('21', 'function'),
    27: ('22', 'phrase'),
    28: ('23', 'num'), 29: ('23', 'ordinal'),
    30: ('24', 'time'),
}

ADVERBS = set('''
sehr ziemlich auch nur noch schon erst wieder immer oft manchmal selten nie
heute gestern morgen jetzt später hier dort links rechts geradeaus oben unten
drinnen draußen vielleicht leider wirklich genau ungefähr zusammen allein
gern(e) lieber am liebsten ein bisschen
'''.split())

PRONOUNS = set('''
wer was welcher welche welches ich du er sie es wir ihr Sie mich mir dich dir
mein meine dein deine sein seine ihr ihre unser unsere euer eure Ihr Ihre
dieser diese dieses alle man jemand niemand etwas nichts
'''.split())

PREPS = set('''
in an auf unter über vor hinter neben zwischen bei mit nach zu aus von für ohne
um bis ab gegen durch seit
'''.split())

CONJS = set('und oder aber denn weil dass wenn'.split())


def clean(s):
    return re.sub(r'\s+', ' ', str(s).replace('\u00a0', ' ')).strip()


def empty(s):
    return not s or s in ('—', '-', '–')


def cell(row, i):
    return clean(row[i]) if i < len(row) else ''


def split_pair(raw):
    left, _, right = raw.partition('·')
    return clean(left), clean(right)


def add(bucket, word, meaning, typ, topic, extra=''):
    word = clean(word)
    meaning = clean(meaning)
    if not word or not meaning:
        return
    key = (word.lower(), meaning.lower())
    if key in bucket:
        rec = bucket[key]
        if topic not in rec['topics']:
            rec['topics'].append(topic)
        if extra and not rec.get('extra'):
            rec['extra'] = extra
        return
    rec = {'word': word, 'meaning': meaning, 'type': typ, 'topics': [topic]}
    if extra:
        rec['extra'] = extra
    bucket[key] = rec


def parse_noun(bucket, row, topic, typ='n'):
    left, plural = split_pair(cell(row, 0))
    meaning = cell(row, 1)
    extra = '' if empty(plural) else 'Pl.: ' + plural
    add(bucket, left, meaning, typ, topic, extra)


def main():
    if not os.path.exists(DOCX):
        sys.exit('DOCX not found: ' + DOCX)
    doc = docx.Document(DOCX)
    bucket = {}

    for idx, (topic, kind) in sorted(TABLE_MAP.items()):
        table = doc.tables[idx]
        rows = [[clean(c.text) for c in r.cells] for r in table.rows]
        for row in rows[1:]:
            if not any(row):
                continue
            if kind in ('noun', 'country'):
                parse_noun(bucket, row, topic)
            elif kind == 'language':
                name, meaning, adj = cell(row, 0), cell(row, 1), cell(row, 2)
                add(bucket, name, meaning, 'n', topic)
                if adj:
                    add(bucket, adj, meaning + ' (tính từ)', 'adj', topic)
            elif kind == 'people':
                forms, plural, meaning = cell(row, 0), cell(row, 1), cell(row, 2)
                parts = [p.strip() for p in forms.split('/') if p.strip()]
                genders = ['nam', 'nữ']
                for i, part in enumerate(parts[:2]):
                    add(bucket, part, meaning + ' (' + genders[i] + ')', 'n', topic,
                        'Pl.: ' + plural if plural and not empty(plural) else '')
            elif kind == 'verb':
                word, forms, meaning, note = cell(row, 0), cell(row, 1), cell(row, 2), cell(row, 3)
                extra = []
                if not empty(forms):
                    extra.append(forms)
                if not empty(note):
                    extra.append(note)
                add(bucket, word, meaning, 'v', topic, ' · '.join(extra))
            elif kind == 'adjadv':
                word, meaning = cell(row, 0), cell(row, 1)
                add(bucket, word, meaning, 'adv' if word in ADVERBS else 'adj', topic)
            elif kind == 'color':
                add(bucket, cell(row, 0), cell(row, 1), 'adj', topic)
            elif kind == 'pron':
                word, meaning = cell(row, 0), cell(row, 1)
                add(bucket, word, meaning, 'pron' if word in PRONOUNS else 'adv', topic)
            elif kind == 'function':
                word, meaning, example = cell(row, 0), cell(row, 1), cell(row, 2)
                if word in PREPS:
                    typ = 'prep'
                elif word in CONJS:
                    typ = 'conj'
                elif word in ('nicht', 'kein / keine', 'ja', 'nein', 'doch', 'bitte', 'danke'):
                    typ = 'part'
                else:
                    typ = 'adv'
                add(bucket, word, meaning, typ, topic, '' if empty(example) else example)
            elif kind == 'phrase':
                add(bucket, cell(row, 0), cell(row, 1), 'phrase', topic)
            elif kind in ('num', 'ordinal'):
                add(bucket, cell(row, 0), cell(row, 1), 'num', topic)
            elif kind == 'time':
                word, meaning = cell(row, 0), cell(row, 1)
                typ = 'phrase' if (' ' in word or word.endswith(('?', '.'))) else 'adv'
                add(bucket, word, meaning, typ, topic)
            else:
                sys.exit('unknown kind ' + kind)

    words = []
    for i, rec in enumerate(bucket.values()):
        rec['num'] = 100001 + i
        rec['topics'] = sorted(rec['topics'])
        words.append(rec)

    counts = {}
    for w in words:
        for t in w['topics']:
            counts[t] = counts.get(t, 0) + 1

    topics_out = [
        {'id': tid, 'name': name, 'short': short, 'count': counts.get(tid, 0)}
        for tid, name, short in TOPICS
    ]

    missing = [t['id'] for t in topics_out if not t['count']]
    if missing:
        sys.exit('empty topics: ' + ', '.join(missing))

    with io.open(OUT_WORDS, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(words, f, ensure_ascii=False, indent=0)
        f.write('\n')
    with io.open(OUT_TOPICS, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(topics_out, f, ensure_ascii=False, indent=0)
        f.write('\n')

    print('de_a1  %d words, %d topics' % (len(words), len(topics_out)))
    for t in topics_out:
        print('  %s %-38s %3d words' % (t['id'], t['short'], t['count']))


if __name__ == '__main__':
    main()
