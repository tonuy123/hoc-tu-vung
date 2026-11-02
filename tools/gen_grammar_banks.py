#!/usr/bin/env python
# gen_grammar_banks.py - generate data-driven banks for the remaining grammar topics.
# Usage:
#   python tools/gen_grammar_banks.py structures
#   python tools/gen_grammar_banks.py lexis
#   python tools/gen_grammar_banks.py exam
#   python tools/gen_grammar_banks.py all
#
# The script is idempotent: it replaces only the banks for the selected group.
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'src', 'data', 'grammar.json')

with io.open(PATH, encoding='utf-8') as f:
    G = json.load(f)
LEX = G['lexicon']
TOPICS = {t['id']: t for t in G['topics']}
VERBS = LEX['verbs']
SUBJ = LEX['subjects']

# ---------- shared subject fields ----------
EXTRA = {
    'I': dict(be='am', have='have', do='do', was='was', poss='my', poss_p='mine', obj='me', refl='myself', pro='I'),
    'you': dict(be='are', have='have', do='do', was='were', poss='your', poss_p='yours', obj='you', refl='yourself', pro='you'),
    'he': dict(be='is', have='has', do='does', was='was', poss='his', poss_p='his', obj='him', refl='himself', pro='he'),
    'she': dict(be='is', have='has', do='does', was='was', poss='her', poss_p='hers', obj='her', refl='herself', pro='she'),
    'it': dict(be='is', have='has', do='does', was='was', poss='its', poss_p='its', obj='it', refl='itself', pro='it'),
    'we': dict(be='are', have='have', do='do', was='were', poss='our', poss_p='ours', obj='us', refl='ourselves', pro='we'),
    'they': dict(be='are', have='have', do='do', was='were', poss='their', poss_p='theirs', obj='them', refl='themselves', pro='they'),
    'my brother': dict(be='is', have='has', do='does', was='was', poss='his', poss_p='his', obj='him', refl='himself', pro='he'),
    'the manager': dict(be='is', have='has', do='does', was='was', poss='his', poss_p='his', obj='him', refl='himself', pro='he'),
    'the students': dict(be='are', have='have', do='do', was='were', poss='their', poss_p='theirs', obj='them', refl='themselves', pro='they'),
    'our team': dict(be='is', have='has', do='does', was='was', poss='its', poss_p='its', obj='it', refl='itself', pro='it'),
    'Anna': dict(be='is', have='has', do='does', was='was', poss='her', poss_p='hers', obj='her', refl='herself', pro='she'),
    'Tom and I': dict(be='are', have='have', do='do', was='were', poss='our', poss_p='ours', obj='us', refl='ourselves', pro='we'),
    'the client': dict(be='is', have='has', do='does', was='was', poss='his', poss_p='his', obj='him', refl='himself', pro='he'),
    'my parents': dict(be='are', have='have', do='do', was='were', poss='their', poss_p='theirs', obj='them', refl='themselves', pro='they'),
    'the company': dict(be='is', have='has', do='does', was='was', poss='its', poss_p='its', obj='it', refl='itself', pro='it'),
}
for s in SUBJ:
    s.update(EXTRA[s['t']])

# ---------- shared dimensions ----------
TIMES = [
    'every day', 'on Mondays', 'at 9 a.m.', 'after lunch', 'in the morning',
    'twice a week', 'every week', 'before work', 'on weekends', 'once a month',
    'during the week', 'at noon',
]
PLACES = [
    'in the office', 'at the front desk', 'in the meeting room', 'on the second floor',
    'at the branch', 'in the lobby', 'at headquarters', 'near the entrance',
    'in the sales department', 'at the reception desk', 'in the building', 'on the top floor',
]
MANNER = ['carefully', 'quickly', 'regularly', 'efficiently']
FREQ = ['always', 'usually', 'often', 'sometimes', 'rarely', 'never', 'generally', 'normally']
DEGREE = ['very', 'extremely', 'quite', 'fairly', 'really', 'particularly', 'especially', 'rather']
COMMENT = ['in general', 'in practice', 'as expected', 'for now']
CTX = [
    'at work', 'during the meeting', 'in this case', 'before the deadline',
    'in the report', 'for the team', 'at the moment', 'these days',
    'in the past', 'in the future', 'on this project', 'under the current policy',
    'in most companies', 'for many employees', 'in the survey', 'according to the data',
    'in the long term', 'at first', 'as a result', 'in reality',
]
ADV = []
for i in range(50):
    ADV.append(dict(
        manner=MANNER[i % len(MANNER)],
        freq=FREQ[(i * 3) % len(FREQ)],
        degree=DEGREE[(i * 5) % len(DEGREE)],
    ))

ADJ = [
    dict(b='important', cmp='more important', sup='the most important'),
    dict(b='clear', cmp='clearer', sup='the clearest'),
    dict(b='quick', cmp='quicker', sup='the quickest'),
    dict(b='safe', cmp='safer', sup='the safest'),
    dict(b='useful', cmp='more useful', sup='the most useful'),
    dict(b='simple', cmp='simpler', sup='the simplest'),
    dict(b='effective', cmp='more effective', sup='the most effective'),
    dict(b='careful', cmp='more careful', sup='the most careful'),
    dict(b='efficient', cmp='more efficient', sup='the most efficient'),
    dict(b='reliable', cmp='more reliable', sup='the most reliable'),
    dict(b='flexible', cmp='more flexible', sup='the most flexible'),
    dict(b='practical', cmp='more practical', sup='the most practical'),
    dict(b='detailed', cmp='more detailed', sup='the most detailed'),
    dict(b='complete', cmp='more complete', sup='the most complete'),
    dict(b='accurate', cmp='more accurate', sup='the most accurate'),
    dict(b='affordable', cmp='more affordable', sup='the most affordable'),
    dict(b='modern', cmp='more modern', sup='the most modern'),
    dict(b='popular', cmp='more popular', sup='the most popular'),
    dict(b='difficult', cmp='more difficult', sup='the most difficult'),
    dict(b='expensive', cmp='more expensive', sup='the most expensive'),
]

NOUNS = [
    'report', 'email', 'contract', 'proposal', 'office', 'meeting room',
    'laptop', 'printer', 'system', 'software', 'website', 'invoice',
    'presentation', 'plan', 'schedule', 'budget', 'policy', 'process',
    'service', 'product', 'project', 'database', 'meeting', 'training session',
    'supplier', 'client', 'employee', 'manager', 'document', 'receipt',
    'ticket', 'room', 'building', 'vehicle', 'machine', 'account',
    'payment', 'shipment', 'folder', 'phone', 'desk', 'chair',
    'package', 'file', 'contractor', 'consultant', 'department', 'branch',
    'warehouse', 'factory',
]
PAIRS = []
for i, n in enumerate(NOUNS):
    if i % 2 == 0:
        PAIRS.append(dict(a='the new ' + n, b='the old ' + n))
    else:
        PAIRS.append(dict(a='this ' + n, b='that ' + n))

# 50 adjective-order noun phrases
OPINIONS = ['beautiful', 'excellent', 'comfortable', 'modern', 'spacious',
            'reliable', 'practical', 'elegant', 'quiet', 'bright']
SIZES = ['large', 'small', 'medium', 'huge', 'compact']
COLORS = ['blue', 'white', 'gray', 'black', 'green']
ORDER_NOUNS = ['office', 'meeting room', 'conference table', 'laptop bag', 'reception area',
               'desk', 'chair', 'building', 'showroom', 'workshop']
NP_ORDER = []
for i, op in enumerate(OPINIONS):
    for j in range(5):
        noun = ORDER_NOUNS[(i + j) % len(ORDER_NOUNS)]
        det = 'an' if op[0] in 'aeiou' else 'a'
        NP_ORDER.append(dict(det=det, op=op, size=SIZES[(i + j) % 5],
                             age=['new', 'recent', 'modern', 'old', 'brand-new'][(i + j) % 5],
                             color=COLORS[(i + j) % 5], noun=noun))

# 50 article entries: countable nouns use a/an/the; uncountable entries use a piece/item.
ART_NOUNS = [
    ('report', 'c'), ('email', 'c'), ('contract', 'c'), ('proposal', 'c'), ('meeting', 'c'),
    ('invoice', 'c'), ('laptop', 'c'), ('printer', 'c'), ('office', 'c'), ('desk', 'c'),
    ('chair', 'c'), ('phone', 'c'), ('file', 'c'), ('folder', 'c'), ('package', 'c'),
    ('shipment', 'c'), ('client', 'c'), ('supplier', 'c'), ('employee', 'c'), ('manager', 'c'),
    ('project', 'c'), ('budget', 'c'), ('schedule', 'c'), ('plan', 'c'), ('policy', 'c'),
    ('process', 'c'), ('service', 'c'), ('product', 'c'), ('website', 'c'), ('database', 'c'),
    ('presentation', 'c'), ('document', 'c'), ('receipt', 'c'), ('ticket', 'c'), ('room', 'c'),
    ('building', 'c'), ('vehicle', 'c'), ('machine', 'c'), ('account', 'c'), ('payment', 'c'),
    ('information', 'u'), ('equipment', 'u'), ('furniture', 'u'), ('software', 'u'),
    ('feedback', 'u'), ('advice', 'u'), ('research', 'u'), ('training', 'u'),
    ('luggage', 'u'), ('stationery', 'u'),
]
ART = []
for noun, kind in ART_NOUNS:
    if kind == 'c':
        det = 'an' if noun[0] in 'aeiou' else 'a'
        plural = noun + ('es' if noun.endswith(('s', 'x', 'ch', 'sh')) else 's')
        if noun.endswith('y'):
            plural = noun[:-1] + 'ies'
        ART.append(dict(a=det + ' ' + noun, an=det + ' ' + noun, the='the ' + noun,
                        pl='the ' + plural, pl_be='are', zero=plural))
    else:
        ART.append(dict(a='a piece of ' + noun, an='an item of ' + noun,
                        the='the ' + noun, pl='the ' + noun, pl_be='is', zero=noun))

# 50 countable/uncountable entries
C_NOUNS = ['reports', 'emails', 'contracts', 'proposals', 'meetings', 'invoices',
           'laptops', 'printers', 'offices', 'desks', 'chairs', 'phones',
           'files', 'folders', 'packages', 'shipments', 'clients', 'suppliers',
           'employees', 'managers', 'projects', 'budgets', 'schedules', 'plans', 'policies']
U_NOUNS = ['information', 'equipment', 'furniture', 'software', 'feedback', 'advice',
           'research', 'training', 'luggage', 'stationery', 'news', 'money',
           'work', 'traffic', 'progress', 'evidence', 'knowledge', 'experience',
           'support', 'access', 'data', 'time', 'space', 'water', 'paper']
C_QUANT = ['a few', 'several', 'many', 'a number of', 'some']
U_QUANT = ['a little', 'some', 'much', 'a great deal of', 'enough']
CNT = []
for i in range(50):
    c = C_NOUNS[i % len(C_NOUNS)]
    u = U_NOUNS[i % len(U_NOUNS)]
    CNT.append(dict(
        c=C_QUANT[i % len(C_QUANT)] + ' ' + c,
        u=U_QUANT[i % len(U_QUANT)] + ' ' + u,
        c_many='many ' + c, u_much='much ' + u,
        c_some='some ' + c, u_some='some ' + u,
        c_pl=c, u_unc=u,
    ))

def low1(x):
    if x.startswith('I ') or x == 'I':
        return x
    return x[:1].lower() + x[1:]


def cap1(x):
    return x[:1].upper() + x[1:]


def lower_fields(d, *keys):
    for k in keys:
        d[k + '_l'] = low1(d[k])


def third(v):
    if v.endswith(('s', 'x', 'z', 'ch', 'sh', 'o')):
        return v + 'es'
    if v.endswith('y') and len(v) > 1 and v[-2] not in 'aeiou':
        return v[:-1] + 'ies'
    return v + 's'


# 50 determiner phrases
DET = []
for n in [x for x in NOUNS if x != 'software']:
    plural = n + ('es' if n.endswith(('s', 'x', 'ch', 'sh')) else 's')
    if n.endswith('y'):
        plural = n[:-1] + 'ies'
    DET.append(dict(
        this='this ' + n, that='that ' + n, these='these ' + plural, those='those ' + plural,
        every='every ' + n, each='each ' + n, all='all the ' + plural,
        some='some ' + plural, any='any ' + plural,
    ))

# 50 reflexive/pronoun entries
REFL = []
for i, s in enumerate(SUBJ * 4):
    v = VERBS[(i * 5) % len(VERBS)]
    o = v['obj'][i % 2]
    REFL.append(dict(
        refl='%s %s %s %s' % (s['t'], v['past'], o, s['refl']),
        by='%s %s %s by %s' % (s['t'], v['past'], o, s['refl']),
        obj='The manager called %s' % s['obj'],
        each='%s and a colleague helped each other' % s['t'],
        q='Did the manager call %s?' % s['obj'],
    ))

# 50 possessive entries
POSS = []
for i, s in enumerate(SUBJ * 4):
    n = NOUNS[(i * 3) % len(NOUNS)]
    v = VERBS[(i * 7) % len(VERBS)]
    POSS.append(dict(
        poss='%s %s' % (s['poss'], n),
        poss_p=s['poss_p'],
        of='the manager\'s ' + n,
        full='%s checked %s %s' % (s['t'], s['poss'], n),
        q='Is this %s %s?' % (s['poss'], n),
        sent='%s sent %s %s to the client' % (s['t'], s['poss'], n),
    ))

# 50 pronoun entries
PRO = []
for i, s in enumerate(SUBJ * 4):
    v = VERBS[(i * 5) % len(VERBS)]
    n = NOUNS[(i * 3) % len(NOUNS)]
    PRO.append(dict(
        subj='%s %s the %s' % (s['t'], v['past'], n),
        refl='%s %s the %s %s' % (s['t'], v['past'], n, s['refl']),
        poss='%s checked %s email' % (s['t'], s['poss']),
        obj='The manager called %s' % s['obj'],
        poss_p='This report is %s' % s['poss_p'],
        q='Did the manager call %s?' % s['obj'],
    ))

# 50 subject-verb agreement entries
SVA = []
for i, c in enumerate(SUBJ * 4):
    v = VERBS[(i * 7) % len(VERBS)]
    o = v['obj'][i % 2]
    sg = next(x for x in SUBJ if x['p'] == '3s')
    pl = next(x for x in SUBJ if x['p'] == '3p')
    SVA.append(dict(
        sg='%s %s %s' % (sg['t'], v['s'], o),
        pl='%s %s %s' % (pl['t'], v['b'], o),
        sgn='%s does not %s %s' % (sg['t'], v['b'], o),
        pln='%s do not %s %s' % (pl['t'], v['b'], o),
        sgq='Does %s %s %s?' % (sg['t'], v['b'], o),
        plq='Do %s %s %s?' % (pl['t'], v['b'], o),
        there_sg='There is a report on the desk',
        there_pl='There are reports on the desk',
    ))

# 50 modal entries
MOD = []
for i, v in enumerate(VERBS * 2):
    o = v['obj'][i % 2]
    MOD.append(dict(
        can='can %s %s' % (v['b'], o),
        cannot='cannot %s %s' % (v['b'], o),
        must='must %s %s' % (v['b'], o),
        should='should %s %s' % (v['b'], o),
        may='may %s %s' % (v['b'], o),
        might='might %s %s' % (v['b'], o),
        could='could %s %s' % (v['b'], o),
        would='would %s %s' % (v['b'], o),
    ))

# 50 gerund/infinitive entries
GER = []
for i, s in enumerate(SUBJ * 4):
    v = VERBS[(i * 7) % len(VERBS)]
    o = v['obj'][i % 2]
    p3 = s['p'] == '3s'
    GER.append(dict(
        enjoy='%s %s %s %s' % (s['t'], 'enjoys' if p3 else 'enjoy', v['ing'], o),
        want='%s %s to %s %s' % (s['t'], 'wants' if p3 else 'want', v['b'], o),
        decide='%s decided to %s %s' % (s['t'], v['b'], o),
        avoid='%s %s making mistakes' % (s['t'], 'avoids' if p3 else 'avoid'),
        finish='%s finished %s %s' % (s['t'], v['ing'], o),
        suggest='%s suggested taking a break' % s['t'],
        mind='%s %s not mind working late' % (s['t'], 'does' if p3 else 'do'),
        forward='%s %s forward to meeting the client' % (s['t'], 'looks' if p3 else 'look'),
    ))

# 50 phrasal verb entries (base, past, pp, object)
PHRASALS = [
    ('follow up on', 'followed up on', 'followed up on', 'the client request', 'the invoice'),
    ('carry out', 'carried out', 'carried out', 'the inspection', 'the survey'),
    ('set up', 'set up', 'set up', 'the meeting', 'the new office'),
    ('turn down', 'turned down', 'turned down', 'the offer', 'the request'),
    ('put off', 'put off', 'put off', 'the meeting', 'the presentation'),
    ('call off', 'called off', 'called off', 'the event', 'the interview'),
    ('bring up', 'brought up', 'brought up', 'the issue', 'the problem'),
    ('look into', 'looked into', 'looked into', 'the complaint', 'the error'),
    ('deal with', 'dealt with', 'dealt with', 'the client', 'the problem'),
    ('find out', 'found out', 'found out', 'the reason', 'the details'),
    ('give up', 'gave up', 'given up', 'the plan', 'the project'),
    ('go over', 'went over', 'gone over', 'the report', 'the figures'),
    ('hand in', 'handed in', 'handed in', 'the report', 'the application'),
    ('keep up with', 'kept up with', 'kept up with', 'the schedule', 'the changes'),
    ('look after', 'looked after', 'looked after', 'the equipment', 'the office'),
    ('make up', 'made up', 'made up', 'the missing data', 'the story'),
    ('pick up', 'picked up', 'picked up', 'the package', 'the client'),
    ('point out', 'pointed out', 'pointed out', 'the error', 'the risk'),
    ('run out of', 'ran out of', 'run out of', 'time', 'supplies'),
    ('take over', 'took over', 'taken over', 'the project', 'the team'),
    ('try out', 'tried out', 'tried out', 'the new system', 'the software'),
    ('work out', 'worked out', 'worked out', 'the budget', 'the schedule'),
    ('write down', 'wrote down', 'written down', 'the details', 'the address'),
    ('back up', 'backed up', 'backed up', 'the data', 'the files'),
    ('sort out', 'sorted out', 'sorted out', 'the problem', 'the invoice'),
]
PHRASAL = []
for base, past, pp, o1, o2 in PHRASALS:
    for o in (o1, o2):
        PHRASAL.append(dict(
            aff='She %s %s' % (past, o),
            neg='She did not %s %s' % (base, o),
            q='Did she %s %s?' % (base, o),
            pp='She has %s %s' % (pp, o),
            past='She %s %s' % (past, o),
            base='%s %s' % (base, o),
        ))

# 50 preposition entries (verb/adjective + preposition + object)
PREP_VERBS = [
    ('depend', 'depended', 'on the supplier'), ('apologize', 'apologized', 'for the delay'),
    ('apply', 'applied', 'for the position'), ('arrive', 'arrived', 'at the office'),
    ('ask', 'asked', 'for help'), ('believe', 'believed', 'in the plan'),
    ('belong', 'belonged', 'to the company'), ('care', 'cared', 'about the details'),
    ('complain', 'complained', 'about the noise'), ('concentrate', 'concentrated', 'on the task'),
    ('deal', 'dealt', 'with the problem'), ('differ', 'differed', 'from the old model'),
    ('focus', 'focused', 'on the report'), ('hear', 'heard', 'about the change'),
    ('insist', 'insisted', 'on the deadline'), ('listen', 'listened', 'to the client'),
    ('object', 'objected', 'to the proposal'), ('pay', 'paid', 'for the service'),
    ('prepare', 'prepared', 'for the interview'), ('refer', 'referred', 'to the report'),
    ('rely', 'relied', 'on the data'), ('respond', 'responded', 'to the email'),
    ('search', 'searched', 'for the file'), ('succeed', 'succeeded', 'in the project'),
    ('wait', 'waited', 'for the confirmation'),
]
PREP_ADJ = [
    ('responsible', 'for the budget'), ('interested', 'in the offer'),
    ('good', 'at solving problems'), ('worried', 'about the deadline'),
    ('satisfied', 'with the result'), ('famous', 'for its service'),
    ('ready', 'for the meeting'), ('afraid', 'of making mistakes'),
    ('proud', 'of the team'), ('disappointed', 'with the service'),
    ('aware', 'of the risk'), ('capable', 'of handling the task'),
    ('dependent', 'on the supplier'), ('familiar', 'with the system'),
    ('keen', 'on the idea'), ('similar', 'to the old model'),
    ('suitable', 'for the role'), ('thankful', 'for the support'),
    ('used', 'to the new system'), ('wrong', 'about the date'),
    ('serious', 'about the plan'), ('confident', 'in the team'),
    ('responsible', 'for the report'), ('happy', 'with the result'),
    ('late', 'for the meeting'),
]
PREP = []
for i, (v, past, rest) in enumerate(PREP_VERBS):
    s = SUBJ[i % len(SUBJ)]
    p3 = s['p'] == '3s'
    PREP.append(dict(
        aff='%s %s %s' % (s['t'], third(v) if p3 else v, rest),
        neg='%s %s not %s %s' % (s['t'], 'does' if p3 else 'do', v, rest),
        q='%s %s %s %s?' % ('Does' if p3 else 'Do', s['t'], v, rest),
        past='%s %s %s' % (s['t'], past, rest),
        pastneg='%s did not %s %s' % (s['t'], v, rest),
        pastq='Did %s %s %s?' % (s['t'], v, rest),
    ))
for i, (adj, rest) in enumerate(PREP_ADJ):
    s = SUBJ[(i + 5) % len(SUBJ)]
    PREP.append(dict(
        aff='%s %s %s %s' % (s['t'], s['be'], adj, rest),
        neg='%s %s not %s %s' % (s['t'], s['be'], adj, rest),
        q='%s %s %s %s?' % (s['be'].capitalize(), s['t'], adj, rest),
        past='%s %s %s %s' % (s['t'], s['was'], adj, rest),
        pastneg='%s %s not %s %s' % (s['t'], s['was'], adj, rest),
        pastq='%s %s %s %s?' % (s['was'].capitalize(), s['t'], adj, rest),
    ))

# 50 conjunction entries
CONJ = []
for i, s in enumerate(SUBJ * 4):
    v = VERBS[(i * 5) % len(VERBS)]
    o = v['obj'][i % 2]
    CONJ.append(dict(
        and_='%s %s %s, and %s sent it to the client' % (s['t'], v['past'], o, s['t']),
        but='%s %s %s, but %s did not send it' % (s['t'], v['past'], o, s['t']),
        because='%s sent %s because the client asked' % (s['t'], o),
        although='Although %s %s busy, %s %s %s' % (s['t'], s['was'], s['t'], v['past'], o),
        so='The client asked, so %s %s %s' % (s['t'], v['past'], o),
        or_='You can call the client or send %s' % o,
    ))


def add_bank(topic_id, dims, templates, slots):
    total = len(templates)
    for d in dims:
        vals = slots[d]
        assert vals, (topic_id, d)
        total *= len(vals)
    assert total >= 200000, (topic_id, total)
    LEX.setdefault('patterns', {})[topic_id] = dict(dims=dims, templates=templates, slots=slots)
    TOPICS[topic_id]['gen'] = {'bank': topic_id}
    return total


def only(c, fields):
    return {k: c[k] for k in fields}


# ---------- structures ----------
def build_structures():
    PAT = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        PAT.append(dict(
            sv='%s %s' % (s['t'], v['past']),
            svo='%s %s %s' % (s['t'], v['past'], o),
            svoo='%s sent the client a copy of %s' % (s['t'], o),
            svoc='%s made %s clear' % (s['t'], o),
            svbc='%s %s busy' % (s['t'], s['be']),
        ))
    add_bank('sentence-structures', ['PAT', 'TIME', 'PLACE', 'COMMENT'], [
        '{PAT_SV} {TIME}.',
        '{PAT_SVO} {PLACE} {TIME}.',
        '{PAT_SVOO} {TIME}.',
        '{PAT_SVOC} {TIME}.',
        '{PAT_SVBC} {TIME}.',
        'I know that {PAT_SV} {TIME}.',
        '{PAT_SVO}, and {PAT_SV}.',
        '{COMMENT}, {PAT_SVO} {PLACE}.',
    ], dict(PAT=PAT, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    Q = [only(c, ['aff', 'q', 'qneg', 'wh', 'wh_embed', 'tag_aff', 'tag_neg']) for c in BASE]
    add_bank('questions', ['Q', 'TIME', 'PLACE', 'COMMENT'], [
        '{Q_Q} {TIME}?',
        '{Q_QNEG} {TIME}?',
        '{Q_WH} {TIME}?',
        'Do you know {Q_WH_EMBED} {TIME}?',
        'Could you tell me {Q_WH_EMBED} {TIME}?',
        '{Q_AFF}, {Q_TAG_AFF}?',
        'Why {Q_Q} {TIME}?',
        'How often {Q_Q} {TIME}?',
    ], dict(Q=Q, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    NEG = [only(c, ['aff', 'neg', 'pastneg', 'ppneg', 'contneg']) for c in BASE]
    add_bank('negation', ['NEG', 'TIME', 'PLACE', 'COMMENT'], [
        '{NEG_NEG} {TIME}.',
        '{NEG_PASTNEG} {TIME}.',
        '{NEG_PPNEG} {TIME}.',
        '{NEG_CONTNEG} {TIME}.',
        '{NEG_NEG} {PLACE} {TIME}.',
        '{NEG_PASTNEG} {PLACE} {TIME}.',
        'It is not true that {NEG_AFF} {TIME}.',
        '{NEG_AFF}, but {NEG_NEG} {TIME}.',
    ], dict(NEG=NEG, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    REL = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        REL.append(dict(
            which='the report which %s %s' % (s['t'], v['past']),
            who='the manager who %s %s' % (v['past'], o),
            where='the office where %s %s' % (s['t'], 'works' if s['p'] == '3s' else 'work'),
            whose='the manager whose team %s %s' % (v['past'], o),
        ))
    add_bank('relative-clauses', ['REL', 'ADJ', 'TIME', 'PLACE', 'COMMENT'], [
        '{REL_WHICH} is {ADJ_B} {TIME}.',
        '{REL_WHO} works {PLACE} {TIME}.',
        '{REL_WHERE} is {ADJ_B} {TIME}.',
        '{REL_WHOSE} is {PLACE} {TIME}.',
        'I met {REL_WHO} {PLACE} {TIME}.',
        'This is {REL_WHICH} from the client.',
        '{REL_WHICH} was {ADJ_B} {TIME}.',
        'Do you know {REL_WHO} {PLACE}?',
    ], dict(REL=REL, ADJ=ADJ, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    COND = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        p3 = s['p'] == '3s'
        vs = v['s'] if p3 else v['b']
        do = 'does' if p3 else 'do'
        COND.append(dict(
            if1='If %s %s %s, %s will %s %s' % (s['t'], vs, o, s['t'], v['b'], o),
            if1neg='If %s %s not %s %s, %s will not %s %s' % (s['t'], do, v['b'], o, s['t'], v['b'], o),
            if2='If %s %s %s, %s would %s %s' % (s['t'], v['past'], o, s['t'], v['b'], o),
            if3='If %s had %s %s, %s would have %s %s' % (s['t'], v['pp'], o, s['t'], v['pp'], o),
            unless='Unless %s %s %s, %s will not %s %s' % (s['t'], vs, o, s['t'], v['b'], o),
            q='Will %s %s %s if %s %s %s?' % (s['t'], v['b'], o, s['t'], vs, o),
            q_embed='whether %s will %s %s if %s %s %s' % (s['t'], v['b'], o, s['t'], vs, o),
            if1_l=low1('If %s %s %s, %s will %s %s' % (s['t'], vs, o, s['t'], v['b'], o)),
            if1neg_l=low1('If %s %s not %s %s, %s will not %s %s' % (s['t'], do, v['b'], o, s['t'], v['b'], o)),
            if2_l=low1('If %s %s %s, %s would %s %s' % (s['t'], v['past'], o, s['t'], v['b'], o)),
        ))
    add_bank('conditionals', ['COND', 'CTX', 'TIME', 'COMMENT'], [
        '{COND_IF1} {CTX} {TIME}.',
        '{COND_IF1NEG} {CTX} {TIME}.',
        '{COND_IF2} {CTX} {TIME}.',
        '{COND_IF3} {CTX} {TIME}.',
        '{COND_UNLESS} {CTX} {TIME}.',
        'I wonder {COND_Q_EMBED} {CTX} {TIME}.',
        '{COND_IF1}, and {COND_IF1NEG_L}.',
        '{COMMENT}, {COND_IF1_L} {CTX}.',
    ], dict(COND=COND, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    REP = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        REP.append(dict(
            said='The manager said that %s would %s %s' % (s['t'], v['b'], o),
            told='The manager told the team that %s would %s %s' % (s['t'], v['b'], o),
            ask='The manager asked if %s would %s %s' % (s['t'], v['b'], o),
            askwh='The manager asked when %s would %s %s' % (s['t'], v['b'], o),
            deny='The manager denied that %s had %s %s' % (s['t'], v['pp'], o),
        ))
    for e in REP:
        lower_fields(e, 'said', 'told')
    add_bank('reported-speech', ['REP', 'CTX', 'TIME', 'COMMENT'], [
        '{REP_SAID} {CTX} {TIME}.',
        '{REP_TOLD} {CTX} {TIME}.',
        '{REP_ASK} {CTX} {TIME}.',
        '{REP_ASKWH} {CTX} {TIME}.',
        '{REP_DENY} {CTX} {TIME}.',
        'I heard that {REP_SAID_L} {CTX} {TIME}.',
        'Did you know that {REP_SAID_L} {CTX}?',
        '{COMMENT}, {REP_TOLD_L} {CTX}.',
    ], dict(REP=REP, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    WISH = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        WISH.append(dict(
            present='I wish I had more time to %s %s' % (v['b'], o),
            past='I wish I had %s %s' % (v['pp'], o),
            future='I wish %s would %s %s' % (s['t'], v['b'], o),
            only='If only I had %s %s' % (v['pp'], o),
            regret='I regret not %s %s' % (v['ing'], o),
        ))
    add_bank('wish-clauses', ['WISH', 'CTX', 'TIME', 'COMMENT'], [
        '{WISH_PRESENT} {CTX} {TIME}.',
        '{WISH_PAST} {CTX} {TIME}.',
        '{WISH_FUTURE} {CTX} {TIME}.',
        '{WISH_ONLY} {CTX} {TIME}.',
        '{WISH_REGRET} {CTX} {TIME}.',
        '{WISH_PRESENT} {CTX} {TIME}.',
        '{WISH_PAST} {CTX} {TIME}.',
        '{COMMENT}, {WISH_PRESENT} {CTX}.',
    ], dict(WISH=WISH, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    CAUS = []
    for c in BASE:
        v, o = c['v'], c['o']
        CAUS.append(dict(obj=o, pp=v['pp'], base=v['b'], agent='the team'))
    add_bank('causative', ['S', 'CAUS', 'TIME', 'PLACE'], [
        '{S_T} had {CAUS_OBJ} {CAUS_PP} {TIME}.',
        '{S_T} got {CAUS_OBJ} {CAUS_PP} {TIME}.',
        '{S_T} made {CAUS_AGENT} {CAUS_BASE} {CAUS_OBJ} {TIME}.',
        '{S_T} let {CAUS_AGENT} {CAUS_BASE} {CAUS_OBJ} {TIME}.',
        '{S_T} helped {CAUS_AGENT} {CAUS_BASE} {CAUS_OBJ} {TIME}.',
        '{S_T} did not have {CAUS_OBJ} {CAUS_PP} {TIME}.',
        'Did {S_T} get {CAUS_OBJ} {CAUS_PP} {TIME}?',
        '{S_T} had {CAUS_OBJ} {CAUS_PP} {PLACE} {TIME}.',
    ], dict(S=SUBJ, CAUS=CAUS, TIME=TIMES, PLACE=PLACES))

    INV = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        INV.append(dict(
            never='Never %s %s %s %s' % (s['have'], s['t'], v['pp'], o),
            rarely='Rarely %s %s %s %s' % (s['do'], s['t'], v['b'], o),
            hardly='Hardly had %s %s %s when the meeting started' % (s['t'], v['pp'], o),
            notonly='Not only did %s %s %s, but %s also %s it' % (s['t'], v['b'], o, s['t'], v['past']),
            had='Had %s %s %s, %s would have called' % (s['t'], v['pp'], o, s['t']),
            so='So detailed was the report that we approved it',
            only='Only then did %s %s %s' % (s['t'], v['b'], o),
            nowhere='Nowhere else can you find %s' % o,
        ))
    add_bank('inversion', ['INV', 'CTX', 'TIME', 'COMMENT'], [
        '{INV_NEVER} {CTX} {TIME}.',
        '{INV_RARELY} {CTX} {TIME}.',
        '{INV_HARDLY} {CTX} {TIME}.',
        '{INV_NOTONLY} {CTX} {TIME}.',
        '{INV_HAD} {CTX} {TIME}.',
        '{INV_SO} {CTX} {TIME}.',
        '{INV_ONLY} {CTX} {TIME}.',
        '{INV_NOWHERE} {CTX} {TIME}.',
    ], dict(INV=INV, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    CLEFT = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        CLEFT.append(dict(
            it='It was %s who %s %s' % (s['t'], v['past'], o),
            what='What %s %s is a clear plan' % (s['t'], 'needs' if s['p'] == '3s' else 'need'),
            all='All %s %s is %s' % (s['t'], 'wants' if s['p'] == '3s' else 'want', o),
            there='There is a report that needs checking',
            itplace='It was at the office that %s %s %s' % (s['t'], v['past'], o),
        ))
    for e in CLEFT:
        lower_fields(e, 'it', 'all')
    add_bank('cleft-sentences', ['CLEFT', 'TIME', 'PLACE', 'COMMENT'], [
        '{CLEFT_IT} {TIME}.',
        '{CLEFT_WHAT} {TIME}.',
        '{CLEFT_ALL} {TIME}.',
        '{CLEFT_THERE} {TIME}.',
        '{CLEFT_ITPLACE} {TIME}.',
        'I think {CLEFT_IT_L} {TIME}.',
        '{CLEFT_WHAT}, and {CLEFT_ALL_L}.',
        '{COMMENT}, {CLEFT_IT_L} {PLACE} {TIME}.',
    ], dict(CLEFT=CLEFT, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    PART = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        PART.append(dict(
            ing='%s %s, %s noticed a problem' % (v['ing'].capitalize(), o, s['t']),
            ed='%s in 2020, the report is outdated' % v['pp'].capitalize(),
            having='Having %s %s, %s went home' % (v['pp'], o, s['t']),
            not_='Not %s %s, %s asked for help' % (v['ing'], o, s['t']),
            being='Being a new employee, %s asked many questions' % s['t'],
            compared='Compared with last year, %s has improved' % o,
            ing_after='%s %s' % (v['ing'], o),
        ))
    for e in PART:
        lower_fields(e, 'having')
    add_bank('participle-clauses', ['PART', 'CTX', 'TIME', 'COMMENT'], [
        '{PART_ING} {CTX} {TIME}.',
        '{PART_ED} {CTX} {TIME}.',
        '{PART_HAVING} {CTX} {TIME}.',
        '{PART_NOT_} {CTX} {TIME}.',
        '{PART_BEING} {CTX} {TIME}.',
        '{PART_COMPARED} {CTX} {TIME}.',
        'I noticed a problem while {PART_ING_AFTER} {CTX}.',
        '{COMMENT}, {PART_HAVING_L} {CTX}.',
    ], dict(PART=PART, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    NC = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        NC.append(dict(
            that='I believe that %s will %s %s' % (s['t'], v['b'], o),
            whether='She asked whether %s would %s %s' % (s['t'], v['b'], o),
            what='We discussed what %s %s' % (s['t'], 'needs' if s['p'] == '3s' else 'need'),
            if_='I wonder if %s will %s %s' % (s['t'], v['b'], o),
            how='She explained how %s %s %s' % (s['t'], v['s'] if s['p'] == '3s' else v['b'], o),
            fact='The fact that %s %s %s surprised us' % (s['t'], v['past'], o),
        ))
    for e in NC:
        lower_fields(e, 'that', 'fact')
    add_bank('noun-clauses', ['NC', 'CTX', 'TIME', 'COMMENT'], [
        '{NC_THAT} {CTX} {TIME}.',
        '{NC_WHETHER} {CTX} {TIME}.',
        '{NC_WHAT} {CTX} {TIME}.',
        '{NC_IF_} {CTX} {TIME}.',
        '{NC_HOW} {CTX} {TIME}.',
        '{NC_FACT} {CTX} {TIME}.',
        'I know that {NC_THAT_L} {CTX}.',
        '{COMMENT}, {NC_FACT_L} {CTX}.',
    ], dict(NC=NC, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    ADVCL = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        ADVCL.append(dict(
            time='When the meeting ended, %s %s %s' % (s['t'], v['past'], o),
            reason='Because %s %s %s, we changed the plan' % (s['t'], v['past'], o),
            condition='If %s %s %s, we will approve it' % (s['t'], v['s'] if s['p'] == '3s' else v['b'], o),
            concession='Although %s %s %s, we continued' % (s['t'], v['past'], o),
            purpose='%s left early so that %s could %s %s' % (cap1(s['t']), s['t'], v['b'], o),
            result='The report was so important that we discussed it',
        ))
    for e in ADVCL:
        lower_fields(e, 'time', 'reason')
    add_bank('adverb-clauses', ['ADVCL', 'CTX', 'TIME', 'COMMENT'], [
        '{ADVCL_TIME} {CTX} {TIME}.',
        '{ADVCL_REASON} {CTX} {TIME}.',
        '{ADVCL_CONDITION} {CTX} {TIME}.',
        '{ADVCL_CONCESSION} {CTX} {TIME}.',
        '{ADVCL_PURPOSE} {CTX} {TIME}.',
        '{ADVCL_RESULT} {CTX} {TIME}.',
        'I know that {ADVCL_TIME_L} {CTX}.',
        '{COMMENT}, {ADVCL_REASON_L} {CTX}.',
    ], dict(ADVCL=ADVCL, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    TAG = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        p3 = s['p'] == '3s'
        tag_be = 'am I' if s['pro'] == 'I' else ('is %s' % s['pro'] if p3 else 'are %s' % s['pro'])
        TAG.append(dict(
            aff='%s %s %s, %s?' % (s['t'], v['s'] if p3 else v['b'], o, c['tag_aff']),
            neg='%s %s not %s %s, %s?' % (s['t'], 'does' if p3 else 'do', v['b'], o, c['tag_neg']),
            past='%s %s %s, didn\'t %s?' % (s['t'], v['past'], o, s['pro']),
            modal='%s can %s %s, can\'t %s?' % (s['t'], v['b'], o, s['pro']),
            be='%s %s ready, %s?' % (s['t'], s['be'], 'isn\'t %s' % s['pro'] if p3 else 'aren\'t %s' % s['pro']),
            lets='Let\'s %s %s, shall we?' % (v['b'], o),
            imperative='Please %s %s, will you?' % (v['b'], o),
            not_='%s %s not ready, %s?' % (s['t'], s['be'], tag_be),
        ))
    for e in TAG:
        lower_fields(e, 'lets', 'imperative')
    add_bank('question-tags', ['TAG', 'CTX', 'TIME', 'COMMENT'], [
        '{TIME}, {TAG_AFF}',
        '{CTX}, {TAG_NEG}',
        '{TIME}, {TAG_PAST}',
        '{CTX}, {TAG_MODAL}',
        '{TIME}, {TAG_BE}',
        '{CTX}, {TAG_LETS_L}',
        '{TIME}, {TAG_IMPERATIVE_L}',
        '{COMMENT}, {TAG_NOT_}',
    ], dict(TAG=TAG, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    SO = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        SO.append(dict(
            so='The report was so detailed that we approved it',
            such='It was such a long meeting that everyone felt tired',
            so_many='There were so many clients that we opened another desk',
            so_much='There was so much work that we stayed late',
            such_a='She is such a reliable manager that everyone trusts her',
        ))
    for e in SO:
        lower_fields(e, 'so', 'such')
    add_bank('so-such', ['SO', 'CTX', 'TIME', 'COMMENT'], [
        '{SO_SO} {CTX} {TIME}.',
        '{SO_SUCH} {CTX} {TIME}.',
        '{SO_SO_MANY} {CTX} {TIME}.',
        '{SO_SO_MUCH} {CTX} {TIME}.',
        '{SO_SUCH_A} {CTX} {TIME}.',
        'I did not expect that {SO_SO_L} {CTX}.',
        'Did you know that {SO_SUCH_L} {CTX}?',
        '{COMMENT}, {SO_SO_L} {CTX}.',
    ], dict(SO=SO, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    TOO = []
    for c in BASE:
        o = c['o']
        TOO.append(dict(
            too='The report was too large to send by email',
            enough='She is experienced enough to lead the project',
            not_enough='The room was not big enough for the meeting',
            too_many='There were too many applicants to interview in one day',
            too_much='There was too much noise to concentrate',
        ))
    for e in TOO:
        lower_fields(e, 'too', 'enough', 'not_enough')
    add_bank('too-enough', ['TOO', 'CTX', 'TIME', 'COMMENT'], [
        '{TOO_TOO} {CTX} {TIME}.',
        '{TOO_ENOUGH} {CTX} {TIME}.',
        '{TOO_NOT_ENOUGH} {CTX} {TIME}.',
        '{TOO_TOO_MANY} {CTX} {TIME}.',
        '{TOO_TOO_MUCH} {CTX} {TIME}.',
        'I think that {TOO_TOO_L} {CTX}.',
        'Do you think {TOO_ENOUGH_L} {CTX}?',
        '{COMMENT}, {TOO_NOT_ENOUGH_L} {CTX}.',
    ], dict(TOO=TOO, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    CONC = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        CONC.append(dict(
            although='Although %s %s busy, %s %s %s' % (s['t'], s['was'], s['t'], v['past'], o),
            even='Even though %s %s %s, we finished the report' % (s['t'], v['past'], o),
            though='Though %s %s tired, %s stayed late' % (s['t'], s['was'], s['t']),
            despite='Despite working late, %s %s %s' % (s['t'], v['past'], o),
            in_spite='In spite of the rain, we visited the site',
        ))
    for e in CONC:
        lower_fields(e, 'although', 'even', 'despite')
    add_bank('concession-clauses', ['CONC', 'CTX', 'TIME', 'COMMENT'], [
        '{CONC_ALTHOUGH} {CTX} {TIME}.',
        '{CONC_EVEN} {CTX} {TIME}.',
        '{CONC_THOUGH} {CTX} {TIME}.',
        '{CONC_DESPITE} {CTX} {TIME}.',
        '{CONC_IN_SPITE} {CTX} {TIME}.',
        'I know that {CONC_ALTHOUGH_L} {CTX}.',
        'Did you notice that {CONC_EVEN_L} {CTX}?',
        '{COMMENT}, {CONC_DESPITE_L} {CTX}.',
    ], dict(CONC=CONC, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    PURP = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        PURP.append(dict(
            so_that='%s sent the file early so that the team could review it' % s['t'].capitalize(),
            in_order_that='She called in order that everyone could prepare',
            to='She called to confirm the meeting',
            in_order_to='We left early in order to catch the train',
            so_as_to='He spoke slowly so as to be understood',
        ))
    for e in PURP:
        lower_fields(e, 'to', 'in_order_to')
    add_bank('purpose-clauses', ['PURP', 'CTX', 'TIME', 'COMMENT'], [
        '{PURP_SO_THAT} {CTX} {TIME}.',
        '{PURP_IN_ORDER_THAT} {CTX} {TIME}.',
        '{PURP_TO} {CTX} {TIME}.',
        '{PURP_IN_ORDER_TO} {CTX} {TIME}.',
        '{PURP_SO_AS_TO} {CTX} {TIME}.',
        'I think that {PURP_SO_THAT} {CTX}.',
        'Do you know why {PURP_TO_L} {CTX}?',
        '{COMMENT}, {PURP_IN_ORDER_TO_L} {CTX}.',
    ], dict(PURP=PURP, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    PMOD = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        PMOD.append(dict(
            can='%s can be %s' % (o.capitalize(), v['pp']),
            must='%s must be %s' % (o.capitalize(), v['pp']),
            should='%s should be %s' % (o.capitalize(), v['pp']),
            might='%s might be %s' % (o.capitalize(), v['pp']),
            might_have='%s might have been %s' % (o.capitalize(), v['pp']),
            cannot='%s cannot be %s' % (o.capitalize(), v['pp']),
        ))
    for e in PMOD:
        lower_fields(e, 'must', 'should')
    add_bank('passive-modals', ['PMOD', 'CTX', 'TIME', 'COMMENT'], [
        '{PMOD_CAN} {CTX} {TIME}.',
        '{PMOD_MUST} {CTX} {TIME}.',
        '{PMOD_SHOULD} {CTX} {TIME}.',
        '{PMOD_MIGHT} {CTX} {TIME}.',
        '{PMOD_MIGHT_HAVE} {CTX} {TIME}.',
        '{PMOD_CANNOT} {CTX} {TIME}.',
        'I think that {PMOD_MUST_L} {CTX}.',
        '{COMMENT}, {PMOD_SHOULD_L} {CTX}.',
    ], dict(PMOD=PMOD, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    MIX = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        MIX.append(dict(
            past_present='If %s had %s %s, %s would work in banking now' % (s['t'], v['pp'], o, s['t']),
            present_past='If %s were more careful, %s would not have made that mistake' % (s['t'], s['t']),
            past_present_neg='If %s had not %s %s, %s would not be late now' % (s['t'], v['pp'], o, s['t']),
            present_past_neg='If %s were taller, %s would have joined the team' % (s['t'], s['t']),
        ))
    for e in MIX:
        lower_fields(e, 'past_present', 'present_past')
    add_bank('mixed-conditionals', ['MIX', 'CTX', 'TIME', 'COMMENT'], [
        '{MIX_PAST_PRESENT} {CTX} {TIME}.',
        '{MIX_PRESENT_PAST} {CTX} {TIME}.',
        '{MIX_PAST_PRESENT_NEG} {CTX} {TIME}.',
        '{MIX_PRESENT_PAST_NEG} {CTX} {TIME}.',
        'Consider this: {MIX_PAST_PRESENT} {CTX}.',
        'Do you think that {MIX_PRESENT_PAST_L} {CTX}?',
        'She said that {MIX_PAST_PRESENT_L} {CTX}.',
        '{COMMENT}, {MIX_PAST_PRESENT_L} {CTX}.',
    ], dict(MIX=MIX, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    FIP = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        FIP.append(dict(
            would='%s said %s would %s %s the next day' % (s['t'], s['t'], v['b'], o),
            going='We were going to %s %s' % (v['b'], o),
            about='They were about to %s %s when the client called' % (v['b'], o),
            would_neg='He said he would not %s %s' % (v['b'], o),
            would_q='She asked if I would %s %s' % (v['b'], o),
        ))
    for e in FIP:
        lower_fields(e, 'going', 'about')
    add_bank('future-in-the-past', ['FIP', 'CTX', 'TIME', 'COMMENT'], [
        '{FIP_WOULD} {CTX} {TIME}.',
        '{FIP_GOING} {CTX} {TIME}.',
        '{FIP_ABOUT} {CTX} {TIME}.',
        '{FIP_WOULD_NEG} {CTX} {TIME}.',
        '{FIP_WOULD_Q} {CTX} {TIME}.',
        'I knew that {FIP_GOING_L} {CTX}.',
        'Did you know that {FIP_GOING_L} {CTX}?',
        '{COMMENT}, {FIP_ABOUT_L} {CTX}.',
    ], dict(FIP=FIP, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))


# ---------- lexis ----------
def build_lexis():
    add_bank('articles', ['S', 'ART', 'TIME', 'PLACE', 'COMMENT'], [
        '{S_T} needed {ART_A} {TIME}.',
        '{S_T} sent {ART_THE} {PLACE} {TIME}.',
        '{ART_PL} {ART_PL_BE} available {PLACE} {TIME}.',
        'This is {ART_AN} from the client.',
        'We discussed {ART_ZERO} {TIME}.',
        '{S_T} found {ART_A} {PLACE} {TIME}.',
        'Is {ART_THE} on the desk?',
        '{COMMENT}, {S_T} reviewed {ART_THE} {TIME}.',
    ], dict(S=SUBJ, ART=ART, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    add_bank('countable-uncountable', ['S', 'CNT', 'TIME', 'PLACE', 'COMMENT'], [
        '{S_T} needed {CNT_C} {TIME}.',
        '{S_T} needed {CNT_U} {TIME}.',
        'There are {CNT_C} {PLACE}.',
        'There is {CNT_U} {PLACE}.',
        '{S_T} reviewed {CNT_C} {TIME}.',
        '{S_T} reviewed {CNT_U} {TIME}.',
        'How many {CNT_C_PL} are there?',
        '{COMMENT}, how much {CNT_U_UNC} do we need?',
    ], dict(S=SUBJ, CNT=CNT, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    add_bank('quantifiers', ['S', 'CNT', 'TIME', 'PLACE', 'COMMENT'], [
        '{S_T} reviewed {CNT_C_SOME} {TIME}.',
        '{S_T} reviewed {CNT_U_SOME} {TIME}.',
        'There are {CNT_C_MANY} {PLACE}.',
        'There is {CNT_U_MUCH} {PLACE}.',
        '{CNT_C_SOME} were sent {PLACE} {TIME}.',
        '{CNT_U_SOME} was sent {PLACE} {TIME}.',
        'Did {S_T} review {CNT_C} {TIME}?',
        '{COMMENT}, did {S_T} review {CNT_U} {TIME}?',
    ], dict(S=SUBJ, CNT=CNT, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    for e in PRO:
        lower_fields(e, 'refl')
    for e in PRO:
        lower_fields(e, 'obj', 'q')
    add_bank('pronouns', ['PRO', 'TIME', 'PLACE', 'COMMENT'], [
        '{PRO_SUBJ} {TIME}.',
        '{PRO_REFL} {TIME}.',
        '{PRO_POSS} {TIME}.',
        '{PRO_OBJ} {TIME}.',
        '{PRO_POSS_P} {TIME}.',
        '{TIME}, {PRO_Q_L}',
        '{PRO_SUBJ}, and {PRO_OBJ_L} {TIME}.',
        '{COMMENT}, {PRO_REFL_L} {PLACE}.',
    ], dict(PRO=PRO, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    for e in POSS:
        lower_fields(e, 'full', 'q')
    add_bank('possessives', ['POSS', 'TIME', 'PLACE', 'COMMENT'], [
        '{POSS_POSS} is on the desk.',
        '{POSS_FULL} {TIME}.',
        '{POSS_SENT} {TIME}.',
        'This is {POSS_POSS_P}.',
        '{TIME}, {POSS_Q_L}',
        'The manager checked {POSS_OF} {TIME}.',
        '{POSS_POSS} was sent {PLACE} {TIME}.',
        '{COMMENT}, {POSS_FULL_L} {PLACE}.',
    ], dict(POSS=POSS, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    add_bank('determiners', ['S', 'DET', 'TIME', 'PLACE', 'COMMENT'], [
        '{S_T} reviewed {DET_THIS} {TIME}.',
        '{S_T} reviewed {DET_THESE} {TIME}.',
        '{DET_EVERY} receives a badge.',
        '{DET_ALL} were sent {PLACE}.',
        'Do you have {DET_ANY}?',
        '{S_T} needed {DET_SOME} {TIME}.',
        '{DET_THAT} is on the desk.',
        '{COMMENT}, {DET_THOSE} are {PLACE}.',
    ], dict(S=SUBJ, DET=DET, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    for e in REFL:
        lower_fields(e, 'by', 'q')
    add_bank('reflexive-pronouns', ['REFL', 'TIME', 'PLACE', 'COMMENT'], [
        '{REFL_REFL} {TIME}.',
        '{REFL_BY} {TIME}.',
        '{REFL_OBJ} {TIME}.',
        '{REFL_EACH} {TIME}.',
        '{TIME}, {REFL_Q_L}',
        'I think {REFL_REFL} {TIME}.',
        '{REFL_REFL}, and {REFL_EACH}.',
        '{COMMENT}, {REFL_BY_L} {PLACE}.',
    ], dict(REFL=REFL, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    add_bank('comparatives', ['PAIR', 'ADJ', 'TIME', 'PLACE', 'COMMENT'], [
        '{PAIR_A} is {ADJ_CMP} than {PAIR_B}.',
        '{PAIR_A} is not {ADJ_CMP} than {PAIR_B}.',
        'Is {PAIR_A} {ADJ_CMP} than {PAIR_B}?',
        '{PAIR_A} seems {ADJ_CMP} than {PAIR_B} {TIME}.',
        '{PAIR_A} is much {ADJ_CMP} than {PAIR_B}.',
        'We need {PAIR_A} because it is {ADJ_CMP}.',
        '{PAIR_A} is {ADJ_CMP} than {PAIR_B} {PLACE}.',
        '{COMMENT}, compared with {PAIR_B}, {PAIR_A} is {ADJ_CMP}.',
    ], dict(PAIR=PAIRS, ADJ=ADJ, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    add_bank('superlatives', ['PAIR', 'ADJ', 'TIME', 'PLACE', 'COMMENT'], [
        '{PAIR_A} is {ADJ_SUP} in the department.',
        '{PAIR_A} is one of {ADJ_SUP} reports in the department.',
        'This is {ADJ_SUP} report I have read.',
        '{PAIR_A} has {ADJ_SUP} design in the department.',
        'Is {PAIR_A} {ADJ_SUP} in the department?',
        '{PAIR_A} was {ADJ_SUP} {TIME}.',
        'We chose {PAIR_A} because it is {ADJ_SUP}.',
        '{COMMENT}, {PAIR_A} is {ADJ_SUP} {PLACE}.',
    ], dict(PAIR=PAIRS, ADJ=ADJ, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    add_bank('adjective-order', ['S', 'NP', 'TIME', 'PLACE', 'COMMENT'], [
        '{S_T} visited {NP_DET} {NP_OP} {NP_SIZE} {NP_AGE} {NP_COLOR} {NP_NOUN} {TIME}.',
        'They bought {NP_DET} {NP_OP} {NP_SIZE} {NP_AGE} {NP_COLOR} {NP_NOUN}.',
        'This is {NP_DET} {NP_OP} {NP_SIZE} {NP_AGE} {NP_COLOR} {NP_NOUN}.',
        'We need {NP_DET} {NP_OP} {NP_SIZE} {NP_AGE} {NP_COLOR} {NP_NOUN} for the team.',
        'Is it {NP_DET} {NP_OP} {NP_SIZE} {NP_AGE} {NP_COLOR} {NP_NOUN}?',
        'She described {NP_DET} {NP_OP} {NP_SIZE} {NP_AGE} {NP_COLOR} {NP_NOUN}.',
        '{NP_DET} {NP_OP} {NP_SIZE} {NP_AGE} {NP_COLOR} {NP_NOUN} was delivered {TIME}.',
        '{COMMENT}, I saw {NP_DET} {NP_OP} {NP_SIZE} {NP_AGE} {NP_COLOR} {NP_NOUN} {PLACE}.',
    ], dict(S=SUBJ, NP=NP_ORDER, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    add_bank('adverbs', ['S', 'ADV', 'TIME', 'PLACE', 'COMMENT'], [
        '{S_T} reviewed the report {ADV_MANNER} {TIME}.',
        '{S_T} would {ADV_FREQ} review the report {TIME}.',
        '{S_T} {S_BE} {ADV_DEGREE} careful {TIME}.',
        '{S_T} worked {ADV_MANNER} {PLACE}.',
        '{S_T} will review the report {ADV_MANNER} {TIME}.',
        '{S_T} checked the figures {ADV_MANNER} {TIME}.',
        '{S_T} would {ADV_FREQ} check the figures {TIME}.',
        '{COMMENT}, {S_T} finished the report {ADV_MANNER}.',
    ], dict(S=SUBJ, ADV=ADV, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    add_bank('adverb-order', ['S', 'VO', 'MANNER', 'PLACE', 'TIME'], [
        '{S_T} {VO_PAST} {MANNER} {PLACE} {TIME}.',
        '{S_T} {VO_PAST} {MANNER} {TIME}.',
        '{S_T} {VO_PAST} {PLACE} {TIME}.',
        '{S_T} {VO_PAST} {TIME}.',
        '{MANNER}, {S_T} {VO_PAST} {PLACE} {TIME}.',
        '{TIME}, {S_T} {VO_PAST} {MANNER} {PLACE}.',
        'Did {S_T} {VO_BASE} {MANNER} {PLACE} {TIME}?',
        '{S_T} did not {VO_BASE} {MANNER} {PLACE} {TIME}.',
    ], dict(S=SUBJ, VO=[dict(past='%s %s' % (v['past'], v['obj'][i % 2]),
                             base='%s %s' % (v['b'], v['obj'][i % 2]), obj=v['obj'][i % 2])
                         for i, v in enumerate(VERBS * 2)][:50],
            MANNER=MANNER, PLACE=PLACES, TIME=TIMES))

    for e in PREP:
        lower_fields(e, 'aff', 'q', 'pastq')
    add_bank('prepositions', ['PREP', 'TIME', 'PLACE', 'COMMENT'], [
        '{PREP_AFF} {TIME}.',
        '{PREP_NEG} {TIME}.',
        '{TIME}, {PREP_Q_L}',
        '{PREP_PAST} {PLACE} {TIME}.',
        '{PREP_PASTNEG} {TIME}.',
        '{TIME}, {PREP_PASTQ_L}',
        'I know that {PREP_AFF_L} {PLACE}.',
        '{COMMENT}, {PREP_AFF_L} {TIME}.',
    ], dict(PREP=PREP, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    for e in CONJ:
        lower_fields(e, 'but', 'because')
    add_bank('conjunctions', ['CONJ', 'CTX', 'TIME', 'COMMENT'], [
        '{CONJ_AND_} {CTX} {TIME}.',
        '{CONJ_BUT} {CTX} {TIME}.',
        '{CONJ_BECAUSE} {CTX} {TIME}.',
        '{CONJ_ALTHOUGH} {CTX} {TIME}.',
        '{CONJ_SO} {CTX} {TIME}.',
        '{CONJ_OR_} {CTX} {TIME}.',
        'I think that {CONJ_BUT_L} {CTX}.',
        '{COMMENT}, {CONJ_BECAUSE_L} {CTX}.',
    ], dict(CONJ=CONJ, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    for e in SVA:
        lower_fields(e, 'there_pl', 'sgq', 'plq')
    add_bank('subject-verb-agreement', ['SVA', 'TIME', 'PLACE', 'COMMENT'], [
        '{SVA_SG} {TIME}.',
        '{SVA_PL} {TIME}.',
        '{SVA_SGN} {TIME}.',
        '{SVA_PLN} {TIME}.',
        '{TIME}, {SVA_SGQ_L}',
        '{TIME}, {SVA_PLQ_L}',
        '{SVA_THERE_SG} {TIME}.',
        '{COMMENT}, {SVA_THERE_PL_L} {PLACE}.',
    ], dict(SVA=SVA, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    add_bank('modal-verbs', ['S', 'MOD', 'TIME', 'PLACE'], [
        '{S_T} {MOD_CAN} {TIME}.',
        '{S_T} {MOD_CANNOT} {TIME}.',
        '{S_T} {MOD_MUST} {TIME}.',
        '{S_T} {MOD_SHOULD} {TIME}.',
        '{S_T} {MOD_MAY} {TIME}.',
        '{S_T} {MOD_MIGHT} {TIME}.',
        '{S_T} {MOD_COULD} {TIME}.',
        '{S_T} {MOD_WOULD} {PLACE} {TIME}.',
    ], dict(S=SUBJ, MOD=MOD, TIME=TIMES, PLACE=PLACES))

    for e in GER:
        lower_fields(e, 'forward')
    add_bank('gerund-infinitive', ['GER', 'TIME', 'PLACE', 'COMMENT'], [
        '{GER_ENJOY} {TIME}.',
        '{GER_WANT} {TIME}.',
        '{GER_DECIDE} {TIME}.',
        '{GER_AVOID} {TIME}.',
        '{GER_FINISH} {TIME}.',
        '{GER_SUGGEST} {TIME}.',
        '{GER_MIND} {TIME}.',
        '{COMMENT}, {GER_FORWARD_L} {PLACE}.',
    ], dict(GER=GER, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    for e in PHRASAL:
        lower_fields(e, 'aff', 'q')
    add_bank('phrasal-verbs', ['PHRASAL', 'TIME', 'PLACE', 'COMMENT'], [
        '{PHRASAL_AFF} {TIME}.',
        '{PHRASAL_NEG} {TIME}.',
        '{TIME}, {PHRASAL_Q_L}',
        '{PHRASAL_PP} {TIME}.',
        '{PHRASAL_PAST} {PLACE} {TIME}.',
        'I think {PHRASAL_AFF_L} {TIME}.',
        'Please {PHRASAL_BASE} {TIME}.',
        '{COMMENT}, {PHRASAL_AFF_L} {PLACE}.',
    ], dict(PHRASAL=PHRASAL, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))


# ---------- exam ----------
def build_exam():
    TOEIC_ACTIONS = [
        'submit the expense report', 'confirm the booking', 'notify the client about the change',
        'attach the signed contract', 'review the proposal',
        'schedule the interview', 'contact the supplier immediately',
        'update the project timeline', 'prepare the quarterly report',
        'check the flight schedule', 'send the updated price list',
        'book a conference room', 'order office supplies', 'pay the monthly invoice',
        'renew the service contract', 'register for the training session',
        'confirm the delivery date', 'print the meeting materials',
        'reserve a hotel room', 'arrange a conference call', 'file the tax documents',
        'approve the travel request', 'send the invitation', 'update the client database',
        'prepare the sales presentation', 'review the budget proposal',
        'contact the IT support team', 'check the inventory', 'process the refund',
        'issue a receipt', 'schedule a site visit', 'confirm the shipment',
        'prepare the onboarding plan', 'review the safety policy', 'send the meeting minutes',
        'update the employee handbook', 'organize the team meeting', 'book the flight',
        'reserve the training room', 'order new equipment', 'review the supplier contract',
        'confirm the payment', 'prepare the financial statement',
        'submit the application', 'arrange the interview panel', 'send the welcome email',
        'update the marketing plan', 'check the customer feedback',
        'prepare the annual report', 'schedule the maintenance visit',
    ]
    TOEIC = [dict(action=a) for a in TOEIC_ACTIONS]
    add_bank('toeic-business', ['TOEIC', 'TIME', 'PLACE', 'COMMENT'], [
        'Please {TOEIC_ACTION} {TIME}.',
        'Could you {TOEIC_ACTION} {TIME}?',
        'We need you to {TOEIC_ACTION} {TIME}.',
        'The manager asked us to {TOEIC_ACTION} {TIME}.',
        'Before the deadline, please {TOEIC_ACTION}.',
        'If possible, {TOEIC_ACTION} {PLACE} {TIME}.',
        'Your task is to {TOEIC_ACTION} {TIME}.',
        '{COMMENT}, I would like you to {TOEIC_ACTION} {TIME}.',
    ], dict(TOEIC=TOEIC, TIME=TIMES, PLACE=PLACES, COMMENT=COMMENT))

    LINK_LINES = [
        'The plan is expensive; however, it may be effective',
        'The data is clear; therefore, we should act',
        'Although the plan is expensive, it may be effective',
        'We should act because the data is clear',
        'The plan is effective; moreover, it is affordable',
        'Many companies invest in training; for example, our firm runs weekly workshops',
        'The initial cost is high; in addition, the rollout takes time',
        'Sales increased last quarter; as a result, we hired more staff',
        'The policy is popular; nevertheless, it needs revision',
        'Remote work saves time; on the other hand, it can weaken teamwork',
        'The report is detailed; in contrast, the summary is very short',
        'The team worked late; consequently, the project was finished on time',
        'Training improves performance; furthermore, it increases retention',
        'The supplier was late; however, the quality was excellent',
        'We reduced costs; therefore, profits improved',
        'Although the market is competitive, the product sells well',
        'The survey sample was small; therefore, the results are uncertain',
        'The new system is faster; in addition, it is easier to use',
        'The office is small; however, it is well located',
        'The deadline is tight; nevertheless, we can finish the report',
        'The client complained; as a result, we changed the process',
        'The training was useful; for example, staff learned new tools',
        'The budget was cut; consequently, we postponed the launch',
        'The proposal is practical; moreover, it is affordable',
        'The data is incomplete; however, the trend is clear',
        'The team is experienced; in contrast, the new hires need training',
        'The product is reliable; furthermore, it has a long warranty',
        'The meeting was long; nevertheless, we made a decision',
        'The branch is profitable; therefore, we will expand it',
        'The policy was unclear; as a result, employees asked questions',
        'The report was accurate; however, it lacked a conclusion',
        'The service is fast; in addition, the staff are friendly',
        'The project is risky; nevertheless, the potential return is high',
        'The client agreed; consequently, we signed the contract',
        'The software is expensive; on the other hand, it saves time',
        'The survey was anonymous; therefore, responses were honest',
        'The office is modern; for example, it has smart lighting',
        'The team communicated well; as a result, the launch was smooth',
        'The supplier offers credit; however, the delivery is slow',
        'The plan was approved; in addition, the budget was increased',
        'The market is growing; therefore, demand is likely to rise',
        'The report was long; nevertheless, it was easy to read',
        'The staff received training; consequently, errors decreased',
        'The product is popular; moreover, it is affordable',
        'The deadline was extended; however, the scope did not change',
        'The data supports the theory; in contrast, earlier studies disagreed',
        'The process is simple; therefore, new employees learn it quickly',
        'The client is satisfied; furthermore, they renewed the contract',
        'The office moved; as a result, commuting time increased',
        'The team is small; nevertheless, it delivers high-quality work',
    ]
    LINK = [dict(line=x) for x in LINK_LINES]
    for e in LINK:
        lower_fields(e, 'line')
    add_bank('ielts-linking', ['LINK', 'CTX', 'TIME', 'COMMENT'], [
        '{LINK_LINE} {CTX} {TIME}.',
        '{COMMENT}, {LINK_LINE_L} {CTX}.',
        '{LINK_LINE} {TIME}.',
        'The manager said that {LINK_LINE_L} {CTX}.',
        'It is clear that {LINK_LINE_L} {CTX}.',
        'In the report, {LINK_LINE_L} {CTX}.',
        '{LINK_LINE}, which is important {CTX}.',
        'We agree that {LINK_LINE_L} {CTX}.',
    ], dict(LINK=LINK, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    COMPLEX_LINES = [
        'While remote work reduces commuting time, it can weaken team cohesion',
        'The policy, which was introduced last year, has reduced costs',
        'Despite the initial cost, the system saves time',
        'Not only does the policy reduce costs, but it also improves morale',
        'If companies invest in training, productivity may increase',
        'Although the sample was small, the findings are consistent',
        'The report suggests that the market is becoming more competitive',
        'Because the data was incomplete, the conclusion remains uncertain',
        'The new process, which was tested in two branches, reduced errors',
        'Even though the budget was limited, the team completed the project',
        'The study argues that flexible working arrangements improve retention',
        'While the initial results were positive, further research is needed',
        'The company expanded rapidly, which increased demand for training',
        'Unless the policy is revised, costs are likely to rise',
        'The survey found that employees value clear communication',
        'Despite facing strong competition, the firm increased its market share',
        'The system allows staff to work remotely, which improves work-life balance',
        'Not only did the training improve skills, but it also boosted confidence',
        'If the trend continues, demand will exceed supply',
        'Although the report is detailed, it lacks a clear recommendation',
        'The evidence suggests that early intervention is more effective',
        'The project, which began in 2020, has created hundreds of jobs',
        'While some employees prefer remote work, others value office interaction',
        'The policy was introduced to reduce costs and improve efficiency',
        'The data indicates that customer satisfaction has improved',
        'Even if the budget is cut, the core service will continue',
        'The findings highlight the importance of regular training',
        'The company invested in automation, which reduced processing time',
        'Although the market is uncertain, the long-term outlook is positive',
        'The report concludes that further investment is justified',
        'While the initial cost is high, the system pays for itself over time',
        'The new policy, which applies to all staff, will start next month',
        'Because the supplier missed the deadline, the launch was delayed',
        'The study shows that diverse teams make better decisions',
        'Despite the challenges, the project was completed on schedule',
        'If the company expands, it will need more qualified staff',
        'The survey indicates that most customers prefer online service',
        'Not only does the plan reduce waste, but it also lowers costs',
        'Although the evidence is limited, the hypothesis is plausible',
        'The system was designed to improve accuracy and speed',
        'While the results are encouraging, they should be interpreted carefully',
        'The company introduced flexible hours, which improved morale',
        'Even though the task was difficult, the team met the deadline',
        'The report argues that investment in education is essential',
        'If the policy is implemented, it may reduce inequality',
        'The data reveals a clear link between training and performance',
        'Despite the lack of funding, the project moved forward',
        'The new approach, which combines online and offline methods, is effective',
        'Although the sample was limited, the findings are informative',
        'The study recommends that companies invest in employee well-being',
    ]
    COMPLEX = [dict(line=x) for x in COMPLEX_LINES]
    for e in COMPLEX:
        lower_fields(e, 'line')
    add_bank('ielts-complex', ['COMPLEX', 'CTX', 'TIME', 'COMMENT'], [
        '{COMPLEX_LINE} {CTX} {TIME}.',
        '{COMMENT}, {COMPLEX_LINE_L} {CTX}.',
        '{COMPLEX_LINE} {TIME}.',
        'The report argues that {COMPLEX_LINE_L} {CTX}.',
        'It is important to note that {COMPLEX_LINE_L} {CTX}.',
        'In many cases, {COMPLEX_LINE_L} {CTX}.',
        '{COMPLEX_LINE}, which deserves attention {CTX}.',
        'We can conclude that {COMPLEX_LINE_L} {CTX}.',
    ], dict(COMPLEX=COMPLEX, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))

    HEDGE_LINES = [
        'The results may suggest that the policy is effective',
        'The findings might be explained by the sample size',
        'The data appears to support this conclusion',
        'The trend is likely to continue',
        'It is possible that the policy will reduce costs',
        'These results suggest that further research is needed',
        'The evidence seems to indicate a positive effect',
        'The outcome could be influenced by external factors',
        'It is unlikely that the change will have an immediate impact',
        'The study tends to support the earlier findings',
        'The data may not be representative of the whole population',
        'The results should be interpreted with caution',
        'The findings are broadly consistent with previous research',
        'The policy might lead to a gradual improvement',
        'It can be argued that the benefits outweigh the costs',
        'The evidence is not sufficient to draw a firm conclusion',
        'The trend appears to be stable over time',
        'The results could be explained by differences in sample size',
        'The study offers preliminary evidence for the theory',
        'The data suggest that the effect is modest',
        'The findings may have important implications for practice',
        'The relationship is likely to be complex',
        'The results are consistent with a small but significant effect',
        'The evidence does not appear to support the stronger claim',
        'The policy may have unintended consequences',
        'The data are limited to a single region',
        'The findings should be replicated in a larger sample',
        'The results indicate a possible association',
        'The study provides tentative support for the hypothesis',
        'The effect might be stronger in the long term',
        'The evidence suggests that the policy is broadly effective',
        'The results are difficult to generalize',
        'The data may reflect seasonal variation',
        'The findings are consistent with earlier observations',
        'The policy is likely to require further adjustment',
        'The study does not establish a causal relationship',
        'The results appear to be robust across models',
        'The evidence is mixed and requires careful interpretation',
        'The trend may continue in the coming years',
        'The findings highlight the need for further investigation',
        'The data suggest a modest improvement in performance',
        'The results could be affected by measurement error',
        'The study offers a useful starting point for future research',
        'The policy might not achieve its intended objectives',
        'The evidence indicates that the effect varies by context',
        'The findings are preliminary and should be treated with caution',
        'The data appear to be consistent with the hypothesis',
        'The results may have been influenced by the sample selection',
        'The study suggests that the relationship is not straightforward',
        'The evidence supports a cautious interpretation',
    ]
    HEDGE = [dict(line=x) for x in HEDGE_LINES]
    for e in HEDGE:
        lower_fields(e, 'line')
    add_bank('academic-hedging', ['HEDGE', 'CTX', 'TIME', 'COMMENT'], [
        '{HEDGE_LINE} {CTX} {TIME}.',
        '{COMMENT}, {HEDGE_LINE_L} {CTX}.',
        '{HEDGE_LINE} {TIME}.',
        'The report notes that {HEDGE_LINE_L} {CTX}.',
        'It is important to note that {HEDGE_LINE_L} {CTX}.',
        'In the literature, {HEDGE_LINE_L} {CTX}.',
        '{HEDGE_LINE}, which warrants further study {CTX}.',
        'We can conclude that {HEDGE_LINE_L} {CTX}.',
    ], dict(HEDGE=HEDGE, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))


# ---------- base clauses ----------
def build_base(n=50):
    out = []
    for i in range(n):
        s = SUBJ[i % len(SUBJ)]
        v = VERBS[(i * 7) % len(VERBS)]
        o = v['obj'][i % 2]
        p3 = s['p'] == '3s'
        vs = v['s'] if p3 else v['b']
        do = 'does' if p3 else 'do'
        have = 'has' if p3 else 'have'
        c = dict(
            subj=s, v=v, o=o,
            aff='%s %s %s' % (s['t'], vs, o),
            neg='%s %s not %s %s' % (s['t'], do, v['b'], o),
            q='%s %s %s %s' % (do, s['t'], v['b'], o),
            qneg='%s\'t %s %s %s' % ('Doesn' if p3 else 'Don', s['t'], v['b'], o),
            wh='what %s %s %s' % (do, s['t'], v['b']),
            wh_embed='what %s %s' % (s['t'], vs),
            tag_aff='%s\'t %s' % ('doesn' if p3 else 'don', s['pro']),
            tag_neg='%s %s' % (do, s['pro']),
            past='%s %s %s' % (s['t'], v['past'], o),
            pastneg='%s did not %s %s' % (s['t'], v['b'], o),
            pastq='did %s %s %s' % (s['t'], v['b'], o),
            pp='%s %s %s %s' % (s['t'], have, v['pp'], o),
            ppneg='%s %s not %s %s' % (s['t'], have, v['pp'], o),
            ppq='%s %s %s %s' % (have, s['t'], v['pp'], o),
            cont='%s %s %s %s' % (s['t'], s['be'], v['ing'], o),
            contneg='%s %s not %s %s' % (s['t'], s['be'], v['ing'], o),
            contq='%s %s %s %s' % (s['be'], s['t'], v['ing'], o),
            pv='%s is %s by %s' % (o, v['pp'], s['obj']),
            pvneg='%s is not %s by %s' % (o, v['pp'], s['obj']),
            pvq='is %s %s by %s' % (o, v['pp'], s['obj']),
            subj_name=s['t'], obj_name=o, verb_base=v['b'], vpp=v['pp'], ving=v['ing'],
            poss=s['poss'], poss_p=s['poss_p'], objp=s['obj'], refl=s['refl'],
            be=s['be'], have_field=have, do=do, was=s['was'], pro=s['pro'],
        )
        out.append(c)
    return out


BASE = build_base()


def main():
    group = sys.argv[1] if len(sys.argv) > 1 else 'all'
    groups = {
        'structures': ['sentence-structures', 'questions', 'negation', 'relative-clauses',
                       'conditionals', 'reported-speech', 'wish-clauses', 'causative',
                       'inversion', 'cleft-sentences', 'participle-clauses', 'noun-clauses',
                       'adverb-clauses', 'question-tags', 'so-such', 'too-enough',
                       'concession-clauses', 'purpose-clauses', 'passive-modals',
                       'mixed-conditionals', 'future-in-the-past'],
        'lexis': ['articles', 'countable-uncountable', 'quantifiers', 'pronouns',
                  'possessives', 'determiners', 'reflexive-pronouns', 'comparatives',
                  'superlatives', 'adjective-order', 'adverbs', 'adverb-order',
                  'prepositions', 'conjunctions', 'subject-verb-agreement',
                  'modal-verbs', 'gerund-infinitive', 'phrasal-verbs'],
        'exam': ['toeic-business', 'ielts-linking', 'ielts-complex', 'academic-hedging'],
    }
    if group not in groups and group != 'all':
        raise SystemExit('unknown group: ' + group)
    todo = []
    if group in ('structures', 'all'):
        todo += groups['structures']
    if group in ('lexis', 'all'):
        todo += groups['lexis']
    if group in ('exam', 'all'):
        todo += groups['exam']
    for tid in todo:
        if tid not in TOPICS:
            raise SystemExit('missing topic: ' + tid)
        if TOPICS[tid].get('gen', {}).get('bank') == tid:
            del TOPICS[tid]['gen']

    if group in ('structures', 'all'):
        build_structures()
    if group in ('lexis', 'all'):
        build_lexis()
    if group in ('exam', 'all'):
        build_exam()

    with io.open(PATH, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(G, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print('group', group)
    print('topics', len(G['topics']))
    print('banks', sum(1 for t in G['topics'] if t.get('gen')))
    print('pattern banks', len(G['lexicon']['patterns']))
    total = 0
    for t in G['topics']:
        gen = t.get('gen') or {}
        if not gen:
            continue
        if gen.get('bank'):
            p = G['lexicon']['patterns'][gen['bank']]
            n = len(p['templates'])
            for d in p['dims']:
                n *= len(p['slots'][d])
            total += n
            print('%-30s %9d' % (t['id'], n))
        else:
            total += int(G['bankPerTopic'])
    print('TOTAL', total)


if __name__ == '__main__':
    main()
