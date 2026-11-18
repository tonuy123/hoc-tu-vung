# -*- coding: utf-8 -*-
"""A2 German grammar drill banks."""
from lexicon import (VERBS, PERSONS, TIME_BASE, TIME_PAST, PLACE_ROOM,
                     PLACE_CITY, pred_pres, pred_perf, pred_prat,
                     pred_modal_prat, dativ_chunks, wechsel_chunks,
                     WECHSEL_PAIRS, reflexiv_chunks, TEMPORAL_PP, shapes_main,
                     shapes_sub, shapes_pair, adj_np_pool, adj_stem)

BANKS = {}


def bank(name, dims, templates, slots):
    BANKS[name] = {"dims": list(dims), "templates": list(templates),
                   "slots": slots}


P = [(t, p) for t, p in PERSONS if t != "es"]
ADV = ["leider", "natürlich", "eigentlich", "wirklich", "hoffentlich",
       "vielleicht", "wahrscheinlich", "normalerweise", "manchmal", "oft",
       "immer", "sicherlich", "sicher", "meistens", "glücklicherweise",
       ]

# ------------------------------------------------------------- 1. Perfekt mit haben
PERF_H_PAIRS = [("lernen", "Deutsch"), ("machen", "die Hausaufgaben"),
                ("kaufen", "ein Auto"), ("lesen", "das Buch"),
                ("schreiben", "einen Brief"), ("kochen", "eine Suppe"),
                ("putzen", "die Küche"), ("hören", "Musik"),
                ("sehen", "den Film"), ("besuchen", "meine Eltern"),
                ("bezahlen", "die Rechnung"), ("finden", "den Schlüssel"),
                ("trinken", "einen Kaffee"), ("suchen", "die Fahrkarte")]

bank("de-a2-perfekt-haben", ["P", "TIME", "ADV"],
     shapes_main("P", "{P_O} {P_P}", neg=False),
     {"P": pred_perf(PERF_H_PAIRS, P), "TIME": TIME_PAST, "ADV": ADV})

# -------------------------------------------------------------- 2. Perfekt mit sein
PERF_S_PAIRS = [("fahren", "nach Berlin"), ("gehen", "nach Hause"),
                ("laufen", "im Park"), ("aufstehen", "früh"),
                ("ankommen", "in Berlin"), ("abfahren", "nach Hamburg"),
                ("einsteigen", "in den Bus"), ("aussteigen", "aus dem Bus"),
                ("umsteigen", "in den Zug"), ("mitkommen", "ins Kino"),
                ("bleiben", "zu Hause"), ("kommen", "aus Spanien"),
                ("gehen", "in die Schule"), ("ankommen", "am Bahnhof")]

bank("de-a2-perfekt-sein", ["P", "TIME", "ADV"],
     shapes_main("P", "{P_O} {P_P}", neg=False),
     {"P": pred_perf(PERF_S_PAIRS, P), "TIME": TIME_PAST, "ADV": ADV})

# ---------------------------------------------------------------- 3. Präteritum
PRAT_PAIRS = [("lernen", "Deutsch"), ("machen", "die Hausaufgaben"),
              ("kaufen", "ein Auto"), ("spielen", "Fußball"),
              ("sehen", "den Film"), ("lesen", "das Buch"),
              ("schreiben", "einen Brief"), ("besuchen", "meine Eltern"),
              ("suchen", "den Schlüssel"), ("finden", "das Buch"),
              ("arbeiten", "im Büro"), ("bleiben", "zu Hause")]

bank("de-a2-praeteritum", ["P", "TIME", "ADV"],
     shapes_main("P", "{P_O}"),
     {"P": pred_prat(PRAT_PAIRS, P), "TIME": TIME_PAST, "ADV": ADV})

# -------------------------------------------------------------------- 4. Dativ
DAT_PAIRS = [("helfen", "dem Nachbarn"), ("danken", "der Lehrerin"),
             ("gratulieren", "dem Kollegen"), ("vertrauen", "meinem Freund"),
             ("antworten", "dem Chef"), ("folgen", "dem Hund"),
             ("begegnen", "dem Nachbarn"), ("folgen", "der Kollegin"),
             ("danken", "dem Arzt"), ("antworten", "der Lehrerin"),
             ("helfen", "der Kollegin"), ("vertrauen", "dem Team")]

bank("de-a2-dativ", ["D", "TIME", "ADV"],
     shapes_main("D", "{D_D}", neg=False),
     {"D": dativ_chunks(DAT_PAIRS, P), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------- 5. Wechselpräpositionen
bank("de-a2-wechsel", ["SV", "W", "TIME", "ADV"],
     ["{SV_S} {SV_MD} {TIME} {ADV} {W_DIR}.",
      "{SV_S} {SV_ML} {TIME} {ADV} {W_LOC}.",
      "{TIME} {SV_MD} {SV_S} {ADV} {W_DIR}.",
      "{TIME} {SV_ML} {SV_S} {ADV} {W_LOC}.",
      "{ADV} {SV_MD} {SV_S} {TIME} {W_DIR}.",
      "Warum {SV_MD} {SV_S} {TIME} {ADV} {W_DIR}?",
      "Warum {SV_ML} {SV_S} {TIME} {ADV} {W_LOC}?",
      "{ADV} {SV_ML} {SV_S} {TIME} {W_LOC}."],
     {"SV": wechsel_chunks(P), "W": WECHSEL_PAIRS, "TIME": TIME_BASE,
      "ADV": ADV})

# ------------------------------------------------------- 6. Nebensätze mit weil
WEIL_PAIRS = [("lernen", "Deutsch"), ("arbeiten", "im Büro"),
              ("wohnen", "in Berlin"), ("spielen", "Fußball"),
              ("kochen", "eine Suppe"), ("putzen", "die Küche"),
              ("bleiben", "zu Hause"), ("einkaufen", "im Supermarkt"),
              ("lesen", "das Buch"), ("besuchen", "meine Eltern"),
              ("arbeiten", "im Garten"), ("warten", "auf den Bus")]

bank("de-a2-nebensatz-weil", ["P", "TIME", "ADV"],
     shapes_sub("P", "{P_O}"),
     {"P": pred_pres(WEIL_PAIRS, P), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------------- 7. Konnektoren
KONN_A = [("lernen", "Deutsch"), ("arbeiten", "im Büro"),
          ("kochen", "eine Suppe"), ("lesen", "das Buch"),
          ("spielen", "Fußball"), ("putzen", "die Küche"),
          ("trinken", "einen Tee"), ("bringen", "ein Buch")]
KONN_B = [("hören", "Musik"), ("suchen", "den Schlüssel"),
          ("kaufen", "ein Brot"), ("schreiben", "einen Brief"),
          ("besuchen", "meine Eltern"), ("bezahlen", "die Rechnung"),
          ("trinken", "einen Kaffee"), ("warten", "auf den Bus")]

bank("de-a2-konnektoren", ["A", "B", "K", "TIME", "ADV"],
     shapes_pair("A", "B", "K", "{A_O}", "{B_O}"),
     {"A": pred_pres(KONN_A, P), "B": pred_pres(KONN_B, P),
      "K": ["und", "aber", "oder", "denn"], "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------------- 8. Komparativ
CMP_TABLE = [("schneller", "am schnellsten"), ("älter", "am ältesten"),
             ("größer", "am größten"), ("kleiner", "am kleinsten"),
             ("schöner", "am schönsten"), ("teurer", "am teuersten"),
             ("billiger", "am billigsten"), ("moderner", "am modernsten"),
             ("bequemer", "am bequemsten"), ("praktischer", "am praktischsten"),
             ("wichtiger", "am wichtigsten"),
             ("interessanter", "am interessantesten"),
             ("ruhiger", "am ruhigsten"), ("lauter", "am lautesten"),
             ("wärmer", "am wärmsten"), ("kälter", "am kältesten"),
             ("freundlicher", "am freundlichsten"),
             ("gemütlicher", "am gemütlichsten"),
             ("langsamer", "am langsamsten"), ("stärker", "am stärksten"),
             ("besser", "am besten"), ("höher", "am höchsten")]

CMP_TARGETS = ["als der Bus", "als das Auto", "als das Fahrrad", "als der Zug",
               "als das Zimmer", "als die Wohnung", "als das Fahrrad",
               "als im letzten Jahr", "als gestern", "als früher",
               "als der Computer", "als das Handy"]

CMP_SUBJECTS = ["der Zug", "das Auto", "der Bus", "das Fahrrad",
                "die Wohnung", "das Zimmer", "der Computer", "das Handy"]


def cmp_items():
    out = []
    for subj in CMP_SUBJECTS:
        for comp, sup in CMP_TABLE:
            for target in CMP_TARGETS:
                if target == "als " + subj or target == "als das " + subj:
                    continue
                out.append({"S": subj, "V": "ist", "VS": "ist " + subj,
                            "CMP": comp + " " + target, "SUP": sup})
    return out


bank("de-a2-komparativ", ["A", "TIME", "ADV"],
     ["{A_S} ist {TIME} {ADV} {A_CMP}.",
      "Ist {A_S} {TIME} {ADV} {A_CMP}?",
      "{ADV} ist {A_S} {TIME} {A_CMP}.",
      "{TIME} finde ich {A_S} {ADV} {A_CMP}.",
      "Warum ist {A_S} {TIME} {ADV} {A_CMP}?",
      "{A_S} ist {TIME} {ADV} nicht {A_CMP}.",
      "{TIME} ist {A_S} {ADV} {A_SUP}.",
      "{TIME} ist {A_S} {ADV} {A_CMP}, oder?"],
     {"A": cmp_items(), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------------------- 9. Futur I
FUT_FORMS = ["werde", "wirst", "wird", "werden", "werdet", "werden"]
FUT_PAIRS = [("lesen", "das Buch"), ("schreiben", "einen Brief"),
             ("arbeiten", "im Büro"), ("lernen", "Deutsch"),
             ("kaufen", "ein Auto"), ("besuchen", "meine Eltern"),
             ("kochen", "eine Suppe"), ("fahren", "nach Berlin"),
             ("gehen", "nach Hause"), ("spielen", "Fußball"),
             ("aufstehen", "früh"), ("anrufen", "meinen Bruder")]


def futur_chunks():
    out = []
    for name, comp in FUT_PAIRS:
        v = VERBS[name]
        for text, pi in P:
            out.append({"S": text, "V": FUT_FORMS[pi],
                        "VS": FUT_FORMS[pi] + " " + text,
                        "O": comp, "I": v.inf})
    return out


bank("de-a2-futur", ["F", "TIME", "ADV"],
     shapes_main("F", "{F_O} {F_I}"),
     {"F": futur_chunks(), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------- 10. Modalverben im Präteritum
MODAL_PAIRS = [("arbeiten", "im Büro"), ("lernen", "Deutsch"),
               ("kommen", "mit dem Bus"), ("gehen", "nach Hause"),
               ("fahren", "nach Berlin"), ("helfen", "dem Nachbarn"),
               ("kochen", "eine Suppe"), ("warten", "auf den Bus"),
               ("aufstehen", "früh"), ("einkaufen", "im Supermarkt"),
               ("anrufen", "den Arzt"), ("lesen", "das Buch")]

bank("de-a2-modal-praet", ["M", "TIME", "ADV"],
     shapes_main("M", "{M_O} {M_I}"),
     {"M": pred_modal_prat(["können", "müssen", "wollen", "dürfen",
                            "sollen", "mögen"], MODAL_PAIRS, P),
      "TIME": TIME_PAST, "ADV": ADV})

# ------------------------------------------------------------- 11. Reflexiv
bank("de-a2-reflexiv", ["R", "TIME", "ADV"],
     ["{R_S} {R_V} {R_R} {TIME} {ADV} {R_PP}.",
      "{R_V} {R_S} {R_R} {TIME} {ADV} {R_PP}?",
      "{ADV} {R_V} {R_S} {R_R} {TIME} {R_PP}.",
      "{R_S} {R_V} {R_R} {TIME} {ADV} {R_PP}.",
      "Warum {R_V} {R_S} {R_R} {TIME} {ADV} {R_PP}?",
      "{TIME} {R_V} {R_S} {R_R} {ADV} {R_PP}.",
      "{ADV} {R_V} {R_S} {R_R} {TIME} nicht {R_PP}.",
      "Warum {R_V} {R_S} {R_R} {TIME} {ADV} nicht {R_PP}?"],
     {"R": reflexiv_chunks(P), "TIME": TIME_BASE, "ADV": ADV})

# --------------------------------------------------- 12. Temporale Präpositionen
TEMP_PAIRS = [("arbeiten", "im Büro"), ("lernen", "Deutsch"),
              ("fahren", "nach Berlin"), ("gehen", "nach Hause"),
              ("bleiben", "zu Hause"), ("kochen", "eine Suppe"),
              ("lesen", "das Buch"), ("warten", "auf den Bus")]

TEMP_PP_NOW = [p for p in TEMPORAL_PP
               if p not in ("vor drei Jahren", "in letzter Zeit")]

bank("de-a2-temporal-praep", ["PP", "P", "ADV"],
     ["{P_S} {P_V} {ADV} {PP} {P_O}.",
      "{P_S} {P_V} {PP} {ADV} {P_O}.",
      "{P_VS} {ADV} {PP} {P_O}?",
      "Warum {P_VS} {PP} {ADV} {P_O}?",
      "{PP} {P_V} {P_S} {ADV} {P_O}.",
      "{ADV} {P_V} {P_S} {PP} {P_O}.",
      "{P_S} {P_V} {ADV} {PP} {P_O} nicht.",
      "{ADV} {P_VS} {PP} {P_O}?"],
     {"PP": TEMP_PP_NOW, "P": pred_pres(TEMP_PAIRS, P), "ADV": ADV})

# --------------------------------------------- 13. Adjektiv nach best. Artikel
ADJ_PRED = ["neu", "alt", "groß", "klein", "schön", "teuer", "billig", "modern",
            "bequem", "praktisch", "kaputt", "sauber", "hell", "dunkel",
            "wichtig", "interessant", "ruhig", "laut", "warm", "kalt",
            "gemütlich", "komisch", "leer", "voll", "eng"]

OBJ_NOUNS = [("der", "Tisch", "Tische"), ("der", "Stuhl", "Stühle"),
             ("der", "Schrank", "Schränke"), ("der", "Computer", "Computer"),
             ("das", "Fenster", "Fenster"), ("das", "Bett", "Betten"),
             ("das", "Sofa", "Sofas"), ("das", "Regal", "Regale"),
             ("das", "Buch", "Bücher"), ("das", "Auto", "Autos"),
             ("das", "Zimmer", "Zimmer"), ("das", "Büro", "Büros"),
             ("das", "Haus", "Häuser"), ("die", "Lampe", "Lampen"),
             ("die", "Tür", "Türen"), ("die", "Küche", "Küchen"),
             ("die", "Wohnung", "Wohnungen"), ("die", "Tasche", "Taschen"),
             ("die", "Uhr", "Uhren"), ("die", "Flasche", "Flaschen")]


def adj_nouns():
    """Full article + adjective + noun phrase, nominative and accusative baked."""
    out = []
    for art, noun, plural in OBJ_NOUNS:
        g = {"der": "m", "die": "f", "das": "n"}[art]
        for adj in ADJ_PRED:
            st = adj_stem(adj)
            if g == "m":
                nom = "der " + st + "e " + noun
                akk = "den " + st + "en " + noun
            elif g == "f":
                nom = "die " + st + "e " + noun
                akk = "die " + st + "e " + noun
            else:
                nom = "das " + st + "e " + noun
                akk = "das " + st + "e " + noun
            out.append({"NOM": nom, "AKK": akk,
                        "S": nom, "V": "ist", "VS": "ist " + nom})
    return out


bank("de-a2-adj-best", ["NP", "TIME", "ADV"],
     ["{NP_NOM} gefällt mir {TIME} {ADV}.",
      "{TIME} gefällt mir {NP_NOM} {ADV}.",
      "Gefällt dir {NP_NOM} {TIME} {ADV}?",
      "{ADV} gefällt mir {NP_NOM} {TIME}.",
      "Ich kaufe {NP_AKK} {TIME} {ADV}.",
      "{TIME} kaufe ich {NP_AKK} {ADV}.",
      "Warum gefällt dir {NP_NOM} {TIME} {ADV} nicht?",
      "{ADV} kaufe ich {NP_AKK} {TIME} nicht."],
     {"NP": adj_nouns(), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------------- 14. zu + Infinitiv
ZU_INF = ["den Text zu lesen", "die Aufgabe zu machen", "das Buch zu kaufen",
          "den Brief zu schreiben", "Deutsch zu lernen", "früher zu kommen",
          "mehr zu arbeiten", "die Wahrheit zu sagen", "das Problem zu lösen",
          "den Termin zu verschieben", "die Rechnung zu bezahlen",
          "nach Berlin zu fahren", "zu Hause zu bleiben", "mehr zu schlafen",
          "Sport zu machen", "die E-Mail zu beantworten", "den Chef zu fragen",
          "das Auto zu reparieren", "im Garten zu arbeiten",
          "auf die Kinder zu warten", "ein Auto zu kaufen",
          "den Eltern zu helfen"]

ZU_VERBS = ["versuchen", "beginnen", "vergessen", "hoffen"]

bank("de-a2-zu-inf", ["SV", "Z", "TIME", "ADV"],
     ["{SV_S} {SV_V} {TIME} {ADV}, {Z}.",
      "{ADV} {SV_V} {SV_S} {TIME}, {Z}.",
      "{TIME} {SV_V} {SV_S} {ADV}, {Z}.",
      "{SV_VS} {TIME} {ADV}, {Z}?",
      "Warum {SV_VS} {TIME} {ADV}, {Z}?",
      "{SV_S} {SV_V} {TIME} {ADV} nicht, {Z}.",
      "{ADV} {SV_V} {SV_S} {TIME} nicht, {Z}.",
      "{TIME} {SV_V} {SV_S} {ADV} nicht, {Z}?"],
     {"SV": pred_pres([(v, "") for v in ZU_VERBS], P), "Z": ZU_INF,
      "TIME": TIME_BASE, "ADV": ADV})
