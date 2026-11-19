# -*- coding: utf-8 -*-
"""Build src/data/de_grammar.json from the Python drill banks.

Usage:
    python tools/gen_de_grammar.py            # validate + write JSON
    python tools/gen_de_grammar.py --sample   # print sample sentences only
"""
import io
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "de_grammar"))

import banks_a1
import banks_a2
import banks_b1
import banks_b2
from topics import TOPICS

OUT = os.path.join(ROOT, "src", "data", "de_grammar.json")
MIN_CAPACITY = 200000

BANKS = {}
for _mod in (banks_a1, banks_a2, banks_b1, banks_b2):
    for _k, _v in _mod.BANKS.items():
        if _k in BANKS:
            raise SystemExit("duplicate bank id: " + _k)
        BANKS[_k] = _v

DIM_RE = re.compile(r"\{(\w+)\}")


def capacity(bank):
    total = len(bank["templates"])
    for d in bank["dims"]:
        total *= len(bank["slots"][d])
    return total


def used_dims(bank):
    hit = set()
    tpl = " ".join(bank["templates"])
    for d in bank["dims"]:
        if re.search(r"\{" + d + r"(_\w+)?\}", tpl):
            hit.add(d)
    return hit


def render(bank, idx):
    dims = bank["dims"]
    slots = bank["slots"]
    total = capacity(bank)
    idx = max(0, min(total - 1, idx))
    x = idx
    pi = x % len(bank["templates"])
    x //= len(bank["templates"])
    mapping = {}
    for d in dims:
        vals = slots[d]
        val = vals[x % len(vals)]
        x //= len(vals)
        if isinstance(val, dict):
            for k, v in val.items():
                mapping[d + "_" + k.upper()] = v
        else:
            mapping[d] = val
    out = bank["templates"][pi]
    for k in DIM_RE.findall(out):
        val = mapping.get(k)
        if val is None:
            raise ValueError("unknown placeholder {%s} in %s" % (k, out))
        out = out.replace("{" + k + "}", val)
    out = re.sub(r"\s+", " ", out)
    out = re.sub(r"\s+([?!.,])", r"\1", out)
    out = out.strip()
    return out[0].upper() + out[1:] if out else out


def validate():
    errors = []
    ids = set()
    if not TOPICS:
        errors.append("no topics")
    for t in TOPICS:
        if t["id"] in ids:
            errors.append("duplicate topic id " + t["id"])
        ids.add(t["id"])
        bank = BANKS.get(t["gen"]["bank"])
        if not bank:
            errors.append("missing bank for " + t["id"])
            continue
        cap = capacity(bank)
        if cap < MIN_CAPACITY:
            errors.append("%s capacity %d < %d" % (t["id"], cap, MIN_CAPACITY))
        missing = set(bank["dims"]) - used_dims(bank)
        if missing:
            errors.append("%s dims unused in templates: %s"
                          % (t["id"], ", ".join(sorted(missing))))
        for tpl in bank["templates"]:
            for d in bank["dims"]:
                if not re.search(r"\{" + d + r"(_\w+)?\}", tpl):
                    errors.append("%s template misses dim %s: %s"
                                  % (t["id"], d, tpl))
        for i in range(0, 40):
            s = render(bank, i * max(1, cap // 40))
            if "{" in s or "}" in s:
                errors.append("%s unresolved placeholder: %s" % (t["id"], s))
            if "  " in s or " ." in s or " ," in s:
                errors.append("%s spacing: %s" % (t["id"], s))
        if not t.get("examples") or not t.get("mistakes"):
            errors.append("%s missing examples/mistakes" % t["id"])
        for ex in t["examples"]:
            if not ex.get("de") or not ex.get("vi"):
                errors.append("%s example incomplete" % t["id"])
        drill = t.get("drill") or []
        if len(drill) != 20:
            errors.append("%s drill must have 20 sentences (got %d)" % (t["id"], len(drill)))
        for row in drill:
            if not row.get("de") or not row.get("vi"):
                errors.append("%s drill row incomplete" % t["id"])
    for bank_id in BANKS:
        if bank_id not in ids:
            errors.append("bank without topic: " + bank_id)
    for lv in ("A1", "A2", "B1", "B2"):
        n = len([t for t in TOPICS if t["level"] == lv])
        if not n:
            errors.append("no topics for level " + lv)
    return errors


def build():
    patterns = {}
    for t in TOPICS:
        bank = BANKS[t["gen"]["bank"]]
        patterns[t["gen"]["bank"]] = {
            "dims": list(bank["dims"]),
            "templates": list(bank["templates"]),
            "slots": bank["slots"],
        }
    return {
        "version": 1,
        "lang": "de",
        "bankPerTopic": MIN_CAPACITY,
        "lexicon": {"patterns": patterns},
        "topics": TOPICS,
    }


def main():
    sample = "--sample" in sys.argv
    errors = validate()
    if errors:
        for e in errors:
            print("ERROR", e)
        raise SystemExit(1)
    if sample:
        random.seed(7)
        for t in TOPICS:
            bank = BANKS[t["gen"]["bank"]]
            cap = capacity(bank)
            idxs = [0, cap // 3, cap - 1]
            print("== %s [%s] %s" % (t["id"], t["level"], t["title"]))
            for i in idxs:
                print("   " + render(bank, i))
        print("\n%d topics, %d banks, total %s sentences"
              % (len(TOPICS), len(BANKS), sum(capacity(BANKS[t["gen"]["bank"]]) for t in TOPICS)))
        return
    data = build()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    size = os.path.getsize(OUT)
    print("wrote %s (%.2f MB) · %d topics · %d banks · %s sentences"
          % (OUT, size / 1048576.0, len(TOPICS), len(BANKS),
             "{:,}".format(sum(capacity(BANKS[t["gen"]["bank"]]) for t in TOPICS))))


if __name__ == "__main__":
    main()
