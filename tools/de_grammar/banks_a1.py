# -*- coding: utf-8 -*-
"""A1 German grammar drill banks.

Every bank shares the same contract with the drill engine: a template must use
each declared dimension, otherwise two index tuples would render the same
sentence.  `shapes_main` / `shapes_yfrage` generate that kind of template, and
they keep the German word order legal:

  * a time adverbial sits right after the finite verb (or opens the clause),
  * a comment adverb stays in the middle field, never dangling at the end,
  * the separable prefix / participle / infinitive is always the final chunk,
  * every verb carries its own complement, so no "Ich fahre den Text".
"""
from lexicon import (VERBS, PERSONS, TIME_BASE, PLACE_ROOM, PLACE_CITY,
                     PLURAL_POOL, imperativ_items, pres_chunks, pred_pres,
                     pred_modal, shapes_main, shapes_yfrage)

BANKS = {}


def bank(name, dims, templates, slots):
    BANKS[name] = {"dims": list(dims), "templates": list(templates),
                   "slots": slots}


P = [(t, p) for t, p in PERSONS if t != "es"]

ADV = ["leider", "natürlich", "eigentlich", "wirklich", "hoffentlich",
       "vielleicht", "wahrscheinlich", "normalerweise", "manchmal", "oft",
       "immer", "sicherlich", "sicher", "meistens", "glücklicherweise",
       ]

# ------------------------------------------------------------------ 1. sein/haben
SEIN_COMP = ["müde", "hungrig", "krank", "zu Hause", "aus Berlin", "Lehrer",
             "Student", "22 Jahre alt", "sehr nett", "schon fertig", "im Büro",
             "in der Schule", "nicht zu Hause", "bereit", "glücklich",
             "traurig", "pünktlich", "verheiratet", "zu spät", "sehr beschäftigt"]
HABEN_COMP = ["Hunger", "Durst", "Zeit", "Geld", "Fragen", "einen Hund",
              "ein Auto", "einen Bruder", "eine Schwester", "ein Problem",
              "Glück", "einen Termin", "einen Plan", "eine Frage",
              "viel Arbeit", "einen Kuli", "eine Wohnung", "einen Computer",
              "einen Kaffee", "eine Idee"]


def sein_haben_items():
    out = []
    for comp in SEIN_COMP:
        out += pred_pres([("sein", comp)], P)
    for comp in HABEN_COMP:
        out += pred_pres([("haben", comp)], P)
    return out


bank("de-a1-sein-haben", ["X", "TIME", "ADV"],
     shapes_main("X", "{X_O}", neg=False),
     {"X": sein_haben_items(), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------------- 2. Präsens regelmäßig
REG_PAIRS = [("lernen", "Deutsch"), ("machen", "die Hausaufgaben"),
             ("kaufen", "ein Brot"), ("suchen", "den Schlüssel"),
             ("brauchen", "eine Fahrkarte"), ("hören", "Musik"),
             ("spielen", "Fußball"), ("kochen", "eine Suppe"),
             ("putzen", "die Küche"), ("besuchen", "meine Eltern"),
             ("fragen", "den Lehrer"), ("sagen", "die Wahrheit"),
             ("bauen", "ein Haus"), ("arbeiten", "im Büro"),
             ("warten", "auf den Bus"), ("bringen", "ein Geschenk")]

bank("de-a1-praesens-reg", ["P", "TIME", "ADV"],
     shapes_main("P", "{P_O}"),
     {"P": pred_pres(REG_PAIRS, P), "TIME": TIME_BASE, "ADV": ADV})

# ----------------------------------------------------------- 3. Präsens unregelmäßig
IRR_PAIRS = [("fahren", "nach Berlin"), ("sehen", "den Film"),
             ("lesen", "das Buch"), ("nehmen", "den Bus"),
             ("essen", "eine Suppe"), ("sprechen", "Deutsch"),
             ("treffen", "meine Freunde"), ("schlafen", "acht Stunden"),
             ("laufen", "im Park"), ("trinken", "einen Tee"),
             ("geben", "dem Kind ein Buch"), ("helfen", "dem Nachbarn"),
             ("waschen", "das Auto"), ("besprechen", "den Plan"),
             ("vergessen", "den Termin"), ("empfehlen", "das Restaurant")]

bank("de-a1-praesens-irr", ["P", "TIME", "ADV"],
     shapes_main("P", "{P_O}"),
     {"P": pred_pres(IRR_PAIRS, P), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------------------- 4. Artikel
ADJ_OBJ = ["neu", "alt", "groß", "klein", "schön", "teuer", "billig", "modern",
           "bequem", "praktisch", "kaputt", "sauber", "hell", "dunkel",
           "wichtig", "interessant", "langweilig", "ruhig", "laut", "warm",
           "kalt", "freundlich", "gemütlich", "komisch", "leer"]

OBJECT_NOUNS = [("der", "Tisch"), ("der", "Stuhl"), ("der", "Schrank"),
                ("der", "Computer"), ("der", "Drucker"), ("der", "Schlüssel"),
                ("der", "Kuli"), ("der", "Apfel"), ("der", "Kaffee"),
                ("der", "Anzug"), ("der", "Wagen"), ("der", "Garten"),
                ("die", "Lampe"), ("die", "Tür"), ("die", "Tasche"),
                ("die", "Küche"), ("die", "Wohnung"), ("die", "Zeitung"),
                ("die", "Fahrkarte"), ("die", "Flasche"), ("die", "Uhr"),
                ("die", "Jacke"), ("die", "Straße"), ("die", "Blume"),
                ("das", "Fenster"), ("das", "Bett"), ("das", "Sofa"),
                ("das", "Regal"), ("das", "Handy"), ("das", "Buch"),
                ("das", "Heft"), ("das", "Auto"), ("das", "Fahrrad"),
                ("das", "Zimmer"), ("das", "Büro"), ("das", "Brot"),
                ("das", "Glas"), ("das", "Bild"), ("das", "Haus"),
                ("das", "Restaurant"), ("das", "Kleid"), ("das", "Hemd")]


def art_nouns():
    out = []
    for art, noun in OBJECT_NOUNS:
        akk = "den" if art == "der" else art
        out.append({"S": art + " " + noun, "AK": akk + " " + noun,
                    "V": "ist", "VS": "ist " + art + " " + noun})
    return out


bank("de-a1-artikel", ["X", "ADJ", "TIME", "ADV"],
     ["{X_S} {X_V} {TIME} {ADV} {ADJ}.",
      "{X_VS} {TIME} {ADV} {ADJ}?",
      "{ADV} {X_V} {X_S} {TIME} {ADJ}.",
      "{X_S} {X_V} {TIME} {ADV} {ADJ}.",
      "{TIME} {X_V} {X_S} {ADV} {ADJ}.",
      "Warum {X_VS} {TIME} {ADV} {ADJ}?",
      "{X_S} {X_V} {TIME} {ADV} nicht {ADJ}.",
      "{ADV} finde ich {X_AK} {TIME} {ADJ}.",
      "{TIME} finde ich {X_AK} {ADV} {ADJ}.",
      "Warum finde ich {X_AK} {TIME} {ADV} {ADJ}?"],
     {"X": art_nouns(), "ADJ": ADJ_OBJ, "TIME": TIME_BASE, "ADV": ADV})

# -------------------------------------------------------------------- 5. Plural
PL_COUNTABLE = [r for r in PLURAL_POOL
                if r["PL"] != r["A"] + " " + r["N"]]

bank("de-a1-plural", ["PL", "TIME", "ADV"],
     ["{PL_A} {PL_N} ist {TIME} {ADV} neu, {PL_PL} sind alt.",
      "{TIME} ist {PL_A} {PL_N} {ADV} teuer, {PL_PL} nicht.",
      "{TIME} sind {ADV} {PL_PL} im Angebot, {PL_A} {PL_N} nicht.",
      "Wo ist {TIME} {ADV} {PL_A} {PL_N}? Wo sind {PL_PL}?",
      "Ist {PL_A} {PL_N} {TIME} {ADV} teuer? Nein, {PL_PL} sind teuer.",
      "{PL_A} {PL_N} ist {TIME} {ADV} klein, {PL_PL} sind groß.",
      "{ADV} ist {PL_A} {PL_N} {TIME} neu, {PL_PL} sind alt.",
      "{TIME} ist {ADV} {PL_A} {PL_N} kaputt, {PL_PL} sind ganz.",
      "{TIME} ist {ADV} {PL_A} {PL_N} sauber, {PL_PL} sind schmutzig.",
      "Warum ist {PL_A} {PL_N} {TIME} {ADV} so teuer? {PL_PL} sind billiger.",
      "{ADV} sind {PL_PL} {TIME} sehr alt, {PL_A} {PL_N} ist neu."],
     {"PL": PL_COUNTABLE, "TIME": TIME_BASE, "ADV": ADV})

# ----------------------------------------------------------------- 6. Akkusativ
AKK_PAIRS = [("kaufen", "einen Apfel"), ("suchen", "den Schlüssel"),
             ("brauchen", "eine Fahrkarte"), ("finden", "das Buch"),
             ("sehen", "den Film"), ("nehmen", "den Bus"),
             ("besuchen", "meine Eltern"), ("holen", "einen Kaffee"),
             ("bezahlen", "die Rechnung"), ("lesen", "die Zeitung"),
             ("fragen", "den Lehrer"), ("besprechen", "die Aufgabe"),
             ("öffnen", "das Fenster"), ("reparieren", "den Computer"),
             ("bringen", "ein Buch"), ("benutzen", "den Drucker")]

bank("de-a1-akkusativ", ["P", "TIME", "ADV"],
     shapes_main("P", "{P_O}"),
     {"P": pred_pres(AKK_PAIRS, P), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------------------- 7. Negation
NEG_ITEMS = {
    "haben": ["kein Geld", "keine Zeit", "keinen Hunger", "keinen Durst",
              "keine Ahnung", "kein Auto", "keinen Hund", "kein Problem",
              "keine Fragen", "kein Glück", "keinen Termin", "kein Interesse"],
    "brauchen": ["keine Milch", "kein Brot", "keinen Schlüssel",
                 "keine Fahrkarte", "kein Handy", "keine Tasche",
                 "keinen Computer", "kein Buch", "keine Zeitung",
                 "kein Wasser", "keine Suppe", "keinen Kaffee"],
    "kaufen": ["kein Brot", "keine Milch", "keinen Apfel", "kein Auto",
               "kein Fahrrad", "keine Fahrkarte", "keinen Kaffee",
               "kein Wasser", "keine Zeitung", "keinen Kuchen",
               "kein Fleisch", "keine Blumen"],
    "suchen": ["keinen Schlüssel", "keine Tasche", "kein Handy", "kein Buch",
               "keine Fahrkarte", "keinen Plan", "keine Wohnung"],
}
NEG_PAIRS = []
for _v, _items in NEG_ITEMS.items():
    for _it in _items:
        NEG_PAIRS.append((_v, _it))

bank("de-a1-negation", ["P", "TIME", "ADV"],
     shapes_main("P", "{P_O}", neg=False),
     {"P": pred_pres(NEG_PAIRS, P), "TIME": TIME_BASE, "ADV": ADV})

# --------------------------------------------------------------- 8. Ja/Nein-Fragen
bank("de-a1-yesno", ["P", "TIME", "ADV"],
     shapes_yfrage("P", "{P_O}"),
     {"P": pred_pres(AKK_PAIRS, P), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------------------ 9. W-Fragen
WF_ROWS = [("lernen", "Deutsch", "warum"), ("arbeiten", "im Büro", "wo"),
           ("wohnen", "in Berlin", "wo"), ("kaufen", "ein Brot", "wo"),
           ("suchen", "den Schlüssel", "wo"), ("fahren", "nach Berlin", "wohin"),
           ("kommen", "aus Spanien", "woher"), ("spielen", "Fußball", "wann"),
           ("trinken", "einen Kaffee", "wann"), ("lesen", "die Zeitung", "wann"),
           ("besuchen", "meine Eltern", "wie oft"),
           ("kochen", "eine Suppe", "warum")]


def wf_chunks():
    out = []
    for name, comp, word in WF_ROWS:
        v = VERBS[name]
        for text, pi in P:
            form = v.pres[pi]
            out.append({"S": text, "V": form, "VS": form + " " + text,
                        "O": comp, "W": word})
    return out


bank("de-a1-wfragen", ["P", "TIME", "ADV"],
     ["{P_W} {P_VS} {TIME} {ADV} {P_O}?",
      "{P_W} {P_VS} {ADV} {TIME} {P_O}?",
      "{P_W} {P_VS} {TIME} {ADV} nicht {P_O}?",
      "{P_W} {P_VS} {ADV} {TIME} nicht {P_O}?",
      "{P_W} {P_VS} denn {TIME} {ADV} {P_O}?",
      "{P_W} {P_VS} denn {ADV} {TIME} {P_O}?",
      "{P_W} {P_VS} {ADV} denn {TIME} {P_O}?"],
     {"P": wf_chunks(), "TIME": TIME_BASE, "ADV": ADV})

# ---------------------------------------------------------------- 10. Imperativ
ADV_IMP = ["bitte", "doch", "mal", "schnell", "sofort", "gleich", "ruhig",
           "einfach", "erst", "dann", "kurz", "ordentlich", "vorsichtig",
           "nochmal"]
TIME_IMP = ["jetzt", "heute", "morgen", "heute Abend", "am Montag", "am Abend",
            "am Morgen", "am Wochenende", "vor dem Essen", "nach der Arbeit",
            "in der Pause", "um acht Uhr", "um neun Uhr", "später", "zuerst",
            "danach", "diese Woche", "nächste Woche", "jeden Tag",
            "jeden Morgen", "im Sommer", "im Winter", "heute Morgen",
            "in einer Stunde", "gleich danach"]

bank("de-a1-imperativ", ["I", "X", "TIME"],
     ["{I_V} {X} {TIME} {I_OB}.",
      "{X} {I_V} {TIME} {I_OB}.",
      "{TIME} {I_V} {X} {I_OB}.",
      "{I_V} {TIME} {X} {I_OB}.",
      "{I_V} {TIME} {I_OB}, {X}.",
      "{X} {I_V} {TIME} {I_OB}, bitte.",
      "{TIME} {I_V} {I_OB}, {X}.",
      "{I_V} {X} {I_OB}, und zwar {TIME}.",
      "{TIME} {I_V} {X} {I_OB}, ja?",
      "{I_V} {I_OB}, {X}, und zwar {TIME}."],
     {"I": imperativ_items(), "X": ADV_IMP, "TIME": TIME_IMP})

# ------------------------------------------------------- 11. Trennbare Verben
SEP_PAIRS = [("aufstehen", "früh"), ("einkaufen", "im Supermarkt"),
             ("anrufen", "meinen Bruder"), ("abfahren", "nach Hamburg"),
             ("ankommen", "in Berlin"), ("einsteigen", "in den Bus"),
             ("aussteigen", "aus dem Bus"), ("umsteigen", "in den Zug"),
             ("mitkommen", "ins Kino"), ("aufmachen", "die Tür"),
             ("anfangen", "mit der Arbeit"), ("einladen", "meine Freunde"),
             ("teilnehmen", "an dem Kurs"), ("abfahren", "nach Hamburg"),
             ("ankommen", "am Bahnhof"), ("einsteigen", "in den Zug")]

bank("de-a1-trennbar", ["P", "TIME", "ADV"],
     shapes_main("P", "{P_O} {P_P}"),
     {"P": pred_pres(SEP_PAIRS, P), "TIME": TIME_BASE, "ADV": ADV})

# --------------------------------------------------------- 12. Modalverben
MODAL_PAIRS = [("arbeiten", "im Büro"), ("lernen", "Deutsch"),
               ("kommen", "pünktlich"), ("gehen", "nach Hause"),
               ("fahren", "nach Berlin"), ("helfen", "dem Nachbarn"),
               ("kochen", "eine Suppe"), ("warten", "auf den Bus"),
               ("aufstehen", "früh"), ("einkaufen", "im Supermarkt"),
               ("anrufen", "den Arzt"), ("lesen", "das Buch"),
               ("schlafen", "bis zehn Uhr"), ("trinken", "einen Tee")]

bank("de-a1-modal", ["P", "TIME", "ADV"],
     shapes_main("P", "{P_O} {P_I}"),
     {"P": pred_modal(["können", "müssen", "wollen", "dürfen", "sollen",
                       "mögen"], MODAL_PAIRS, P),
      "TIME": TIME_BASE, "ADV": ADV})

# -------------------------------------------------------------- 13. Possessiv
POSS_FORMS = {
    "ich": ("mein", "meinen", "meine"),
    "du": ("dein", "deinen", "deine"),
    "er": ("sein", "seinen", "seine"),
    "sie": ("ihr", "ihren", "ihre"),
    "wir": ("unser", "unseren", "unsere"),
    "ihr": ("euer", "euren", "eure"),
}
POSS_PERSON = {"ich": 0, "du": 1, "er": 2, "sie": 5, "wir": 3, "ihr": 4}
# (accusative noun, gender, verbs that accept it)
POSS_ITEMS = [
    ("Bruder", "m", ["besuchen", "suchen", "finden"]),
    ("Schwester", "f", ["besuchen", "suchen", "finden"]),
    ("Vater", "m", ["besuchen", "finden"]),
    ("Mutter", "f", ["besuchen", "finden"]),
    ("Freund", "m", ["besuchen", "suchen", "finden"]),
    ("Freundin", "f", ["besuchen", "suchen", "finden"]),
    ("Kollegen", "m", ["besuchen", "suchen", "finden"]),
    ("Kollegin", "f", ["besuchen", "suchen", "finden"]),
    ("Nachbarn", "m", ["besuchen", "suchen", "finden"]),
    ("Nachbarin", "f", ["besuchen", "suchen", "finden"]),
    ("Handy", "n", ["suchen", "brauchen", "finden"]),
    ("Schlüssel", "m", ["suchen", "brauchen", "finden"]),
    ("Tasche", "f", ["suchen", "brauchen", "finden"]),
    ("Buch", "n", ["suchen", "brauchen", "finden"]),
    ("Auto", "n", ["suchen", "brauchen", "finden"]),
    ("Fahrrad", "n", ["suchen", "brauchen", "finden"]),
    ("Koffer", "m", ["suchen", "brauchen", "finden"]),
    ("Zimmer", "n", ["suchen", "brauchen", "finden"]),
    ("Wohnung", "f", ["suchen", "brauchen", "finden"]),
    ("Computer", "m", ["suchen", "brauchen", "finden"]),
    ("Kuli", "m", ["suchen", "brauchen", "finden"]),
    ("Jacke", "f", ["suchen", "brauchen", "finden"]),
]


def poss_chunks():
    out = []
    for subj, pi in sorted(POSS_PERSON.items()):
        base, akk_m, akk_fn = POSS_FORMS[subj]
        for noun, g, verbs in POSS_ITEMS:
            if g == "m":
                obj = akk_m + " " + noun
            elif g == "f":
                obj = akk_fn + " " + noun
            else:
                obj = base + " " + noun
            for verb in verbs:
                form = VERBS[verb].pres[pi]
                out.append({"S": subj, "V": form, "VS": form + " " + subj,
                            "O": obj})
    return out


bank("de-a1-possessiv", ["P", "TIME", "ADV"],
     shapes_main("P", "{P_O}"),
     {"P": poss_chunks(), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------------ 14. Ortspräpositionen
LOC_VERBS = ["arbeiten", "lernen", "spielen", "kochen", "essen", "schlafen",
             "lesen", "wohnen"]
PREP_PLACES = ["in der Küche", "im Wohnzimmer", "im Garten", "im Restaurant",
               "in der Schule", "im Supermarkt", "im Park", "im Hotel",
               "zu Hause", "im Büro", "am Bahnhof", "in der Stadt",
               "in Berlin", "in Wien", "in Hamburg", "in München"]

bank("de-a1-praepositionen", ["PP", "P", "TIME", "ADV"],
     ["{P_S} {P_V} {TIME} {ADV} {PP}.",
      "{P_S} {P_V} {TIME} {ADV} {PP} nicht.",
      "{ADV} {P_V} {P_S} {TIME} {PP}.",
      "{P_VS} {TIME} {ADV} {PP}?",
      "Warum {P_VS} {TIME} {ADV} {PP}?",
      "{PP} {P_V} {P_S} {TIME} {ADV}.",
      "{ADV} {P_VS} {TIME} {PP}?",
      "{ADV} {P_V} {P_S} {TIME} {PP} nicht."],
     {"PP": PREP_PLACES, "P": pres_chunks(LOC_VERBS, P), "TIME": TIME_BASE,
      "ADV": ADV})
