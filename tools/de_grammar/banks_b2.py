# -*- coding: utf-8 -*-
"""B2 German grammar drill banks."""
from lexicon import (VERBS, PERSONS, TIME_BASE, TIME_PAST, PLACE_ROOM, PLACE_CITY,
                     modal_passiv_items, RELP_ITEMS, MAIN_CLAUSES,
                     dativ_chunks, shapes_main)

BANKS = {}


def bank(name, dims, templates, slots):
    BANKS[name] = {"dims": list(dims), "templates": list(templates),
                   "slots": slots}


P = [(t, p) for t, p in PERSONS if t != "es"]
ADV = ["leider", "natürlich", "eigentlich", "wirklich", "hoffentlich",
       "vielleicht", "wahrscheinlich", "normalerweise", "manchmal", "oft",
       "immer", "sicherlich", "sicher", "meistens", "glücklicherweise",
       ]

# ------------------------------------------------------ 1. Passiv mit Modalverb
def modal_passiv_pool():
    out = []
    for item in modal_passiv_items():
        for m, mp in (("muss", "müssen"), ("kann", "können"),
                      ("soll", "sollen"), ("darf", "dürfen"),
                      ("will", "wollen")):
            row = dict(item)
            row["M"] = m
            row["MP"] = mp
            out.append(row)
    return out


bank("de-b2-passiv-modal", ["PM", "TIME", "ADV"],
     ["{PM_S} {PM_M} {TIME} {ADV} {PM_P} werden.",
      "{TIME} {PM_M} {PM_S} {ADV} {PM_P} werden.",
      "{PM_M} {PM_S} {TIME} {ADV} {PM_P} werden?",
      "Warum {PM_M} {PM_S} {TIME} {ADV} {PM_P} werden?",
      "{PM_SP} {PM_MP} {TIME} {ADV} {PM_P} werden.",
      "{TIME} {PM_MP} {PM_SP} {ADV} {PM_P} werden.",
      "{PM_MP} {PM_SP} {TIME} {ADV} {PM_P} werden?",
      "{ADV} {PM_MP} {PM_SP} {TIME} {PM_P} werden?"],
     {"PM": modal_passiv_pool(), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------ 2. Konjunktiv II der Vergangenheit
KV_PARTS = [("gelernt", "Deutsch", "hätte"), ("gemacht", "die Hausaufgaben", "hätte"),
            ("gekauft", "ein Auto", "hätte"), ("gelesen", "das Buch", "hätte"),
            ("geschrieben", "einen Brief", "hätte"),
            ("gekocht", "eine Suppe", "hätte"),
            ("gearbeitet", "im Büro", "hätte"), ("gesehen", "den Film", "hätte"),
            ("genommen", "den Bus", "hätte"),
            ("gefunden", "den Schlüssel", "hätte"),
            ("geholfen", "dem Nachbarn", "hätte"),
            ("gesagt", "die Wahrheit", "hätte"), ("gefragt", "den Lehrer", "hätte"),
            ("gespielt", "Fußball", "hätte"),
            ("gewartet", "auf den Bus", "hätte"),
            ("vergessen", "den Termin", "hätte"),
            ("verkauft", "das Auto", "hätte"), ("besucht", "meine Eltern", "hätte"),
            ("gemacht", "die Prüfung", "hätte"), ("gehört", "die Musik", "hätte"),
            ("geblieben", "zu Hause", "wäre"), ("gefahren", "nach Berlin", "wäre"),
            ("gegangen", "nach Hause", "wäre"), ("gekommen", "zu spät", "wäre")]

_KV_AUX = {"hätte": ["hätte", "hättest", "hätte", "hätten", "hättet", "hätten"],
           "wäre": ["wäre", "wärst", "wäre", "wären", "wärt", "wären"]}


def kv_chunks():
    out = []
    for part, comp, aux in KV_PARTS:
        forms = _KV_AUX[aux]
        for text, pi in P:
            out.append({"S": text, "V": forms[pi], "H": forms[pi],
                        "P": part, "O": comp, "VS": forms[pi] + " " + text})
    return out


bank("de-b2-k2-vergangenheit", ["KV", "TIME", "ADV"],
     shapes_main("KV", "{KV_O} {KV_P}", neg=False),
     {"KV": kv_chunks(), "TIME": TIME_PAST, "ADV": ADV})

# ------------------------------------------------------- 3. Konjunktiv I (Rede)
K1_ITEMS = [
    ("er", "habe", "keine Zeit"),
    ("er", "sei", "krank"),
    ("sie", "müsse", "arbeiten"),
    ("sie", "könne", "nicht kommen"),
    ("er", "werde", "später anrufen"),
    ("sie", "habe", "keine Stelle"),
    ("er", "wolle", "mitkommen"),
    ("sie", "dürfe", "das nicht"),
    ("der Test", "sei", "einfach"),
    ("ich", "solle", "mich ausruhen"),
    ("er", "habe", "das nicht gewusst"),
    ("sie", "sei", "pünktlich gewesen"),
    ("der Chef", "komme", "später"),
    ("die Firma", "suche", "neue Mitarbeiter"),
    ("er", "könne", "gut Deutsch"),
    ("sie", "müsse", "früher gehen"),
    ("er", "brauche", "mehr Zeit"),
    ("sie", "arbeite", "zu viel"),
    ("der Kurs", "beginne", "im September"),
    ("er", "habe", "einen neuen Job"),
]
K1_MAIN = [{"S": "ich", "V": "glaube"},
           {"S": "er", "V": "sagt"},
           {"S": "sie", "V": "meint"},
           {"S": "der Chef", "V": "erklärt"},
           {"S": "die Firma", "V": "behauptet"},
           {"S": "niemand", "V": "weiß"},
           {"S": "sie", "V": "betont"},
           {"S": "man", "V": "sagt"},
           {"S": "der Lehrer", "V": "sagt"}]


def k1_chunks():
    out = []
    for s, k, r in K1_ITEMS:
        out.append({"S": s, "K": k, "R": r})
    return out


bank("de-b2-k1-indirekt", ["IF", "M", "TIME", "ADV"],
     ["{M_S} {M_V} {TIME} {ADV}, {IF_S} {IF_K} {IF_R}.",
      "{TIME} {M_V} {M_S} {ADV}, {IF_S} {IF_K} {IF_R}.",
      "{ADV} {M_V} {M_S} {TIME}, {IF_S} {IF_K} {IF_R}.",
      "{M_S} {M_V} {TIME} {ADV}, {IF_S} {IF_K} {IF_R}.",
      "{TIME} {M_V} {M_S} {ADV}, {IF_S} {IF_K} {IF_R}, oder?",
      "{ADV} {M_V} {M_S} {TIME}, {IF_S} {IF_K} {IF_R}, und zwar genau.",
      "{M_S} {M_V} {TIME} {ADV}, {IF_S} {IF_K} {IF_R}, richtig?",
      "{TIME} {M_V} {M_S} {ADV}, {IF_S} {IF_K} {IF_R}, oder nicht?"],
     {"IF": k1_chunks(), "M": K1_MAIN, "TIME": TIME_BASE, "ADV": ADV})

# ---------------------------------------------------------- 4. Nominalisierung
NOM_PP = ["beim Lernen", "beim Kochen", "beim Lesen", "beim Essen",
          "nach dem Essen", "nach der Arbeit", "nach dem Unterricht",
          "vor dem Schlafen", "vor dem Treffen", "während der Arbeit",
          "während der Pause", "während des Unterrichts", "trotz der Kälte",
          "trotz des Regens", "wegen des Wetters", "wegen der Arbeit",
          "beim Sport", "nach dem Sport", "vor dem Frühstück",
          "beim Einkaufen", "nach dem Einkaufen", "während des Essens",
          "beim Frühstück", "beim Spaziergang"]

bank("de-b2-nominalisierung", ["PP", "M", "TIME", "ADV"],
     ["{PP} {M_V} {M_S} {TIME} {ADV} {M_R}.",
      "{TIME} {M_V} {M_S} {ADV} {PP} {M_R}.",
      "{M_V} {M_S} {PP} {TIME} {ADV} {M_R}?",
      "Warum {M_V} {M_S} {PP} {TIME} {ADV} {M_R}?",
      "{ADV} {M_V} {M_S} {PP} {TIME} {M_R}.",
      "{PP} {M_V} {M_S} {TIME} {ADV} {M_R}, oder?",
      "{ADV} {M_V} {M_S} {PP} {TIME} {M_R}?",
      "{ADV} {M_V} {M_S} {TIME} {PP} {M_R}."],
     {"PP": NOM_PP, "M": MAIN_CLAUSES, "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------- 5. Partizip als Adjektiv
PARTIZIP_STEMS = ["gebaut", "gekauft", "geöffnet", "geschlossen", "gemietet",
                  "verkauft", "repariert", "geputzt", "geschrieben", "gelesen",
                  "gekocht", "gebacken", "vorbereitet", "organisiert",
                  "erledigt", "gelöst", "geprüft", "geliefert", "benutzt",
                  "gestrichen", "verschoben", "übersetzt", "eingeladen",
                  "besucht", "gesucht", "gefunden", "gewaschen", "gezahlt",
                  "geholt", "erklärt"]

NOUN_ROWS = [("der", "Tisch", "Tische"), ("der", "Stuhl", "Stühle"),
             ("das", "Bett", "Betten"), ("das", "Sofa", "Sofas"),
             ("der", "Schrank", "Schränke"), ("die", "Lampe", "Lampen"),
             ("die", "Tür", "Türen"), ("das", "Fenster", "Fenster"),
             ("der", "Teppich", "Teppiche"), ("das", "Regal", "Regale"),
             ("der", "Computer", "Computer"), ("das", "Handy", "Handys"),
             ("der", "Drucker", "Drucker"), ("die", "Kamera", "Kameras"),
             ("die", "Tasche", "Taschen"), ("das", "Buch", "Bücher"),
             ("der", "Stift", "Stifte"), ("das", "Heft", "Hefte"),
             ("die", "Zeitung", "Zeitungen"), ("der", "Apfel", "Äpfel"),
             ("das", "Brot", "Brote"), ("das", "Auto", "Autos"),
             ("das", "Fahrrad", "Fahrräder"), ("der", "Bahnhof", "Bahnhöfe"),
             ("die", "Straße", "Straßen"), ("der", "Park", "Parks"),
             ("die", "Schule", "Schulen"), ("das", "Büro", "Büros"),
             ("die", "Firma", "Firmen"), ("das", "Restaurant", "Restaurants"),
             ("das", "Hotel", "Hotels"), ("die", "Küche", "Küchen"),
             ("der", "Garten", "Gärten"), ("die", "Stadt", "Städte"),
             ("der", "Vertrag", "Verträge"), ("die", "Rechnung", "Rechnungen")]

ADJ_LIKE = ["teuer", "billig", "praktisch", "modern", "kaputt", "alt", "neu",
            "schön", "bequem", "wichtig", "sauber", "hell", "dunkel", "ruhig",
            "laut", "warm", "kalt", "gemütlich", "leer", "voll"]


PARTIZIP_NOUNS = [
    ("der", "Tisch", "Tische", ["gekauft", "gebaut", "repariert", "gestrichen"]),
    ("der", "Stuhl", "Stühle", ["gekauft", "repariert", "gestrichen"]),
    ("das", "Bett", "Betten", ["gekauft", "gebaut", "geliefert"]),
    ("das", "Sofa", "Sofas", ["gekauft", "geliefert", "geputzt"]),
    ("der", "Schrank", "Schränke", ["gekauft", "gebaut", "gestrichen"]),
    ("die", "Lampe", "Lampen", ["gekauft", "repariert", "angeschlossen"]),
    ("die", "Tür", "Türen", ["geöffnet", "geschlossen", "repariert", "gestrichen"]),
    ("das", "Fenster", "Fenster", ["geöffnet", "geschlossen", "geputzt"]),
    ("der", "Teppich", "Teppiche", ["gekauft", "geputzt", "geliefert"]),
    ("das", "Regal", "Regale", ["gekauft", "gebaut", "gestrichen"]),
    ("der", "Computer", "Computer", ["gekauft", "repariert", "installiert", "benutzt"]),
    ("das", "Handy", "Handys", ["gekauft", "repariert", "benutzt"]),
    ("der", "Drucker", "Drucker", ["gekauft", "repariert", "angeschlossen"]),
    ("die", "Kamera", "Kameras", ["gekauft", "repariert", "benutzt"]),
    ("die", "Tasche", "Taschen", ["gekauft", "geputzt", "geliefert"]),
    ("das", "Buch", "Bücher", ["gekauft", "gelesen", "übersetzt", "verkauft"]),
    ("der", "Stift", "Stifte", ["gekauft", "gefunden", "benutzt"]),
    ("das", "Heft", "Hefte", ["gekauft", "gefunden", "benutzt"]),
    ("die", "Zeitung", "Zeitungen", ["gekauft", "gelesen", "geliefert"]),
    ("der", "Apfel", "Äpfel", ["gekauft", "gewaschen", "gegessen"]),
    ("das", "Brot", "Brote", ["gekauft", "gebacken", "geschnitten"]),
    ("das", "Auto", "Autos", ["gekauft", "repariert", "gewaschen", "verkauft"]),
    ("das", "Fahrrad", "Fahrräder", ["gekauft", "repariert", "geputzt"]),
    ("der", "Bahnhof", "Bahnhöfe", ["gebaut", "renoviert", "geputzt"]),
    ("die", "Straße", "Straßen", ["gebaut", "renoviert", "geputzt"]),
    ("der", "Park", "Parks", ["angelegt", "geputzt", "renoviert"]),
    ("die", "Schule", "Schulen", ["gebaut", "renoviert", "geputzt"]),
    ("das", "Büro", "Büros", ["gebaut", "renoviert", "geputzt"]),
    ("die", "Firma", "Firmen", ["gekauft", "verkauft", "renoviert"]),
    ("das", "Restaurant", "Restaurants", ["gekauft", "renoviert", "geputzt"]),
    ("das", "Hotel", "Hotels", ["gebaut", "renoviert", "gekauft"]),
    ("die", "Küche", "Küchen", ["renoviert", "geputzt", "gestrichen"]),
    ("der", "Garten", "Gärten", ["angelegt", "geputzt", "verkauft"]),
    ("die", "Stadt", "Städte", ["gebaut", "renoviert", "geputzt"]),
    ("der", "Vertrag", "Verträge", ["unterschrieben", "geprüft", "übersetzt"]),
    ("die", "Rechnung", "Rechnungen", ["bezahlt", "geprüft", "geschrieben"]),
]


def partizip_nps():
    out = []
    for art, noun, _plural, parts in PARTIZIP_NOUNS:
        g = {"der": "m", "die": "f", "das": "n"}[art]
        for stem in parts:
            nom = art + " " + stem + "e " + noun
            if g == "m":
                akk = "den " + stem + "en " + noun
            else:
                akk = nom
            out.append({"NOM": nom, "AKK": akk})
    return out


bank("de-b2-partizip-adj", ["PNP", "TIME", "ADV"],
     ["{PNP_NOM} gefällt mir {TIME} {ADV}.",
      "{TIME} gefällt mir {PNP_NOM} {ADV}.",
      "Gefällt dir {PNP_NOM} {TIME} {ADV}?",
      "{ADV} gefällt mir {PNP_NOM} {TIME}.",
      "Ich kaufe {PNP_AKK} {TIME} {ADV}.",
      "{TIME} kaufe ich {PNP_AKK} {ADV}.",
      "Warum gefällt dir {PNP_NOM} {TIME} {ADV} nicht?",
      "{ADV} kaufe ich {PNP_AKK} {TIME} nicht."],
     {"PNP": partizip_nps(), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------ 6. Zweiteilige Konnektoren
ZWEI_PAIRS = [("sowohl im Büro als auch zu Hause"),
              ("sowohl in der Küche als auch im Wohnzimmer"),
              ("sowohl im Garten als auch auf dem Balkon"),
              ("sowohl in der Schule als auch in der Bibliothek"),
              ("sowohl im Restaurant als auch im Hotel"),
              ("sowohl im Supermarkt als auch auf dem Markt"),
              ("sowohl am Bahnhof als auch im Zentrum"),
              ("sowohl im Park als auch am See"),
              ("weder im Büro noch zu Hause"),
              ("weder in der Küche noch im Wohnzimmer"),
              ("weder im Garten noch auf dem Balkon"),
              ("weder in der Schule noch in der Bibliothek"),
              ("weder im Restaurant noch im Hotel"),
              ("weder im Supermarkt noch auf dem Markt"),
              ("weder am Bahnhof noch im Zentrum"),
              ("weder im Park noch am See"),
              ("entweder im Büro oder zu Hause"),
              ("entweder in der Küche oder im Wohnzimmer"),
              ("entweder im Garten oder auf dem Balkon"),
              ("entweder in der Schule oder in der Bibliothek"),
              ("entweder im Restaurant oder im Hotel"),
              ("entweder im Supermarkt oder auf dem Markt"),
              ("entweder am Bahnhof oder im Zentrum"),
              ("entweder im Park oder am See"),
              ("nicht nur im Büro, sondern auch zu Hause"),
              ("nicht nur in der Küche, sondern auch im Wohnzimmer"),
              ("nicht nur im Garten, sondern auch auf dem Balkon"),
              ("nicht nur in der Schule, sondern auch in der Bibliothek"),
              ("nicht nur im Restaurant, sondern auch im Hotel"),
              ("nicht nur im Supermarkt, sondern auch auf dem Markt"),
              ("nicht nur am Bahnhof, sondern auch im Zentrum"),
              ("nicht nur im Park, sondern auch am See")]

ZWEI_SUBJECTS = [{"S": "ich", "V": "arbeite"}, {"S": "er", "V": "arbeitet"},
                 {"S": "sie", "V": "arbeitet"}, {"S": "wir", "V": "arbeiten"},
                 {"S": "mein Bruder", "V": "arbeitet"},
                 {"S": "die Kinder", "V": "spielen"},
                 {"S": "meine Kollegen", "V": "arbeiten"},
                 {"S": "der Chef", "V": "arbeitet"}]

bank("de-b2-zweiteilig", ["Z", "S", "TIME", "ADV"],
     ["{S_S} {S_V} {TIME} {ADV} {Z}.",
      "{Z} {S_V} {S_S} {TIME} {ADV}.",
      "{TIME} {S_V} {S_S} {ADV} {Z}.",
      "{ADV} {S_V} {S_S} {TIME} {Z}.",
      "{S_S} {S_V} {TIME} {ADV} nicht {Z}.",
      "{S_V} {S_S} {TIME} {ADV} {Z}?",
      "{Z} {S_V} {S_S} {ADV} {TIME}.",
      "Warum {S_V} {S_S} {TIME} {ADV} {Z}?"],
     {"Z": ZWEI_PAIRS, "S": ZWEI_SUBJECTS, "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------- 7. Relativsatz mit Präposition
def relp_pool():
    out = []
    for np_, rel, rest, main in RELP_ITEMS:
        parts = main.split(" ", 1)
        np_low = np_[0].lower() + np_[1:]
        akk = "den" + np_low[3:] if np_low.startswith("der ") else np_low
        out.append({"NP": np_low, "AKK": akk, "REL": rel,
                    "REST": rest, "V": parts[0],
                    "C": parts[1] if len(parts) > 1 else ""})
    return out


bank("de-b2-relativ-praep", ["RL", "TIME", "ADV"],
     ["{RL_NP}, {RL_REL} {RL_REST}, {RL_V} {TIME} {ADV} {RL_C}.",
      "{RL_NP}, {RL_REL} {RL_REST}, {RL_V} {ADV} {TIME} {RL_C}.",
      "{TIME} {RL_V} {RL_NP}, {RL_REL} {RL_REST}, {ADV} {RL_C}.",
      "{ADV} {RL_V} {RL_NP}, {RL_REL} {RL_REST}, {TIME} {RL_C}.",
      "kennst du {RL_AKK}, {RL_REL} {RL_REST}, {TIME} {ADV}?",
      "Warum {RL_V} {RL_NP}, {RL_REL} {RL_REST}, {TIME} {ADV} {RL_C}?",
      "{RL_NP}, {RL_REL} {RL_REST}, {RL_V} {TIME} {ADV} {RL_C}, oder?",
      "{RL_NP}, {RL_REL} {RL_REST}, {RL_V} {TIME} {ADV} nicht {RL_C}.",
      "Kennst du {RL_AKK}, {RL_REL} {RL_REST}, {ADV} {TIME}?",
      "{RL_NP}, {RL_REL} {RL_REST}, {RL_V} {ADV} {TIME} {RL_C}, nicht wahr?",
      "{ADV} {RL_V} {RL_NP}, {RL_REL} {RL_REST}, {TIME} {RL_C}?",
      "{TIME} kennst du {RL_AKK}, {RL_REL} {RL_REST}, {ADV}?",
      "Warum {RL_V} {RL_NP}, {RL_REL} {RL_REST}, {ADV} {TIME} nicht {RL_C}?",
      "{RL_NP}, {RL_REL} {TIME} {RL_REST}, {RL_V} {ADV} {RL_C}."],
     {"RL": relp_pool(), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------ 8. Genitiv-Präpositionen
GEN_PP = ["wegen des Regens", "trotz der Kälte", "während der Pause",
          "statt des Autos", "außerhalb der Stadt", "innerhalb einer Woche",
          "aufgrund des Wetters", "angesichts der Lage",
          "hinsichtlich der Kosten", "mangels Erfahrung",
          "trotz des Lärms", "wegen der Arbeit", "während des Unterrichts",
          "statt eines Geschenks", "außerhalb der Öffnungszeiten",
          "innerhalb des Gebäudes", "aufgrund der Nachfrage",
          "angesichts des Problems", "mangels Zeit", "wegen des Verkehrs",
          "trotz der Schwierigkeiten", "während der Ferien"]

bank("de-b2-genitiv-praep", ["PP", "M", "TIME", "ADV"],
     ["{PP} {M_V} {M_S} {TIME} {ADV} {M_R}.",
      "{TIME} {M_V} {M_S} {ADV} {PP} {M_R}.",
      "{M_V} {M_S} {PP} {TIME} {ADV} {M_R}?",
      "Warum {M_V} {M_S} {PP} {TIME} {ADV} {M_R}?",
      "{ADV} {M_V} {M_S} {PP} {TIME} {M_R}.",
      "{PP} {M_V} {M_S} {TIME} {ADV} {M_R}, oder?",
      "{ADV} {M_V} {M_S} {PP} {TIME} {M_R}?",
      "{ADV} {M_V} {M_S} {TIME} {PP} {M_R}."],
     {"PP": GEN_PP, "M": MAIN_CLAUSES, "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------------ 9. je ... desto
_JE_RAW = [
    ("mehr", "ich", "lerne", "besser", "verstehe", "ich"),
    ("länger", "ich", "warte", "ungeduldiger", "werde", "ich"),
    ("früher", "du", "kommst", "mehr Zeit", "haben", "wir"),
    ("schneller", "du", "fährst", "gefährlicher", "wird", "es"),
    ("mehr", "du", "übst", "sicherer", "sprichst", "du"),
    ("höher", "wir", "steigen", "kälter", "wird", "es"),
    ("weniger", "ich", "arbeite", "entspannter", "bin", "ich"),
    ("mehr", "man", "lernt", "besser", "versteht", "man"),
    ("länger", "wir", "warten", "nervöser", "werden", "wir"),
    ("mehr", "sie", "trainiert", "stärker", "wird", "sie"),
    ("öfter", "er", "übt", "besser", "spielt", "er"),
    ("lauter", "du", "sprichst", "schneller", "gehen", "wir"),
    ("später", "es", "wird", "dunkler", "ist", "es"),
    ("mehr", "ich", "lerne", "früher", "kann", "ich"),
    ("geduldiger", "du", "bist", "besser", "läuft", "es"),
    ("weniger", "wir", "essen", "besser", "schlafen", "wir"),
]


def je_items():
    return [{"C1": c1, "S1": s1, "V1": v1, "C2": c2, "V2": v2, "S2": s2}
            for c1, s1, v1, c2, v2, s2 in _JE_RAW]


bank("de-b2-je-desto", ["J", "PLACE", "TIME", "ADV"],
     ["Je {J_C1} {J_S1} {TIME} {ADV} {PLACE} {J_V1}, desto {J_C2} {J_V2} {J_S2}.",
      "Je {J_C1} {J_S1} {TIME} {ADV} {PLACE} {J_V1}, desto {J_C2} {J_V2} {J_S2}.",
      "{ADV} gilt: je {J_C1} {J_S1} {TIME} {PLACE} {J_V1}, desto {J_C2} {J_V2} {J_S2}.",
      "{TIME} gilt: je {J_C1} {J_S1} {ADV} {PLACE} {J_V1}, desto {J_C2} {J_V2} {J_S2}.",
      "Je {J_C1} {J_S1} {TIME} {ADV} {PLACE} {J_V1}, desto {J_C2} {J_V2} {J_S2}, oder?",
      "Warum gilt: je {J_C1} {J_S1} {TIME} {ADV} {PLACE} {J_V1}, desto {J_C2} {J_V2} {J_S2}?",
      "{ADV} gilt {TIME}: je {J_C1} {J_S1} {PLACE} {J_V1}, desto {J_C2} {J_V2} {J_S2}.",
      "Je {J_C1} {J_S1} {ADV} {PLACE} {J_V1}, desto {J_C2} {J_V2} {J_S2} {TIME}."],
     {"J": je_items(), "PLACE": PLACE_ROOM + PLACE_CITY, "TIME": TIME_BASE,
      "ADV": ADV})

# ------------------------------------------------------ 10. Verben mit Dativ
DAT_PAIRS = [("helfen", "dem Nachbarn"), ("danken", "der Lehrerin"),
             ("gratulieren", "dem Kollegen"), ("vertrauen", "meinem Freund"),
             ("antworten", "dem Chef"), ("folgen", "dem Hund"),
             ("begegnen", "dem Nachbarn"), ("folgen", "der Kollegin"),
             ("danken", "dem Arzt"), ("antworten", "der Chefin"),
             ("helfen", "der Kollegin"), ("vertrauen", "dem Team")]

bank("de-b2-verben-dativ", ["DV", "TIME", "ADV"],
     shapes_main("DV", "{DV_D}", neg=False),
     {"DV": dativ_chunks(DAT_PAIRS, P), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------- 11. Passiv-Ersatz
ERSATZ_PAIRS = [
    ("das Problem", "lösen"), ("die Aufgabe", "erledigen"),
    ("der Vertrag", "unterschreiben"), ("die Rechnung", "bezahlen"),
    ("das Formular", "ausfüllen"), ("das Haus", "verkaufen"),
    ("das Auto", "reparieren"), ("die Tür", "schließen"),
    ("das Paket", "liefern"), ("die Wohnung", "renovieren"),
    ("der Text", "übersetzen"), ("die Frage", "beantworten"),
    ("das Projekt", "finanzieren"), ("die Maschine", "benutzen"),
    ("der Termin", "verschieben"), ("der Bericht", "prüfen"),
    ("die Küche", "putzen"), ("das Fenster", "öffnen"),
    ("die Fahrkarte", "kaufen"), ("das Buch", "lesen"),
    ("die Präsentation", "vorbereiten"), ("das Essen", "kochen"),
    ("das Zimmer", "streichen"), ("der Boden", "wischen"),
    ("die Wäsche", "waschen"), ("der Schlüssel", "finden"),
    ("die E-Mail", "schreiben"), ("der Antrag", "stellen"),
    ("das Programm", "installieren"), ("der Drucker", "anschließen"),
    ("das Konto", "eröffnen"), ("die Heizung", "prüfen"),
    ("der Brief", "schicken"), ("das Dach", "reparieren"),
    ("der Garten", "gießen"), ("die Rechnung", "kontrollieren"),
    ("der Wagen", "waschen"), ("die Blumen", "gießen"),
    ("der Kuchen", "backen"), ("das Zimmer", "renovieren"),
    ("die Gardinen", "waschen"), ("der Teppich", "reinigen"),
    ("das Sofa", "reparieren"), ("die Lampe", "anschließen"),
    ("der Computer", "installieren"), ("die Tür", "reparieren"),
    ("das Fahrrad", "reparieren"), ("der Koffer", "packen"),
    ("die Wand", "streichen"), ("das Geschirr", "spülen"),
    ("der Rasen", "mähen"), ("die Post", "bringen"),
    ("das Zimmer", "aufräumen"), ("der Tisch", "decken"),
]


def ersatz_items():
    out = []
    for subj, inf in ERSATZ_PAIRS:
        s = subj[0].lower() + subj[1:]
        out.append({"S": s, "V": "ist", "ZU": "zu " + inf,
                    "SICHV": "lässt sich", "SICHR": inf,
                    "BAR": "leicht zu " + inf})
    return out


bank("de-b2-passiv-ersatz", ["E", "TIME", "ADV"],
     ["{E_S} {E_V} {TIME} {ADV} {E_ZU}.",
      "{E_S} {E_SICHV} {TIME} {ADV} {E_SICHR}.",
      "Warum {E_V} {E_S} {TIME} {ADV} {E_ZU}?",
      "{E_SICHV} {E_S} {TIME} {ADV} {E_SICHR}?",
      "{TIME} {E_V} {E_S} {ADV} {E_ZU}.",
      "{E_S} {E_V} {TIME} {ADV} {E_BAR}.",
      "{E_S} {E_V} {TIME} {ADV} nicht {E_ZU}.",
      "{ADV} {E_SICHV} {E_S} {TIME} {E_SICHR}.",
      "{E_S} {E_SICHV} {ADV} {TIME} {E_SICHR}, oder?",
      "{E_V} {E_S} {TIME} {ADV} {E_ZU}?",
      "{TIME} {E_SICHV} {E_S} {ADV} {E_SICHR}?"],
     {"E": ersatz_items(), "TIME": TIME_BASE, "ADV": ADV})
