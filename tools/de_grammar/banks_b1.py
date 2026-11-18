# -*- coding: utf-8 -*-
"""B1 German grammar drill banks."""
from lexicon import (VERBS, PERSONS, TIME_BASE, TIME_PAST, PLACE_ROOM, PLACE_CITY,
                     passiv_pairs, AGENTS, N_DEKL, genitiv_items,
                     RELP_ITEMS, PRAEP_VERBEN, UM_ZU_ITEMS, plusquam_chunks,
                     pred_pres, pred_prat, pred_modal_prat, shapes_main)

BANKS = {}


def bank(name, dims, templates, slots):
    BANKS[name] = {"dims": list(dims), "templates": list(templates),
                   "slots": slots}


P = [(t, p) for t, p in PERSONS if t != "es"]
ADV = ["leider", "natürlich", "eigentlich", "wirklich", "hoffentlich",
       "vielleicht", "wahrscheinlich", "normalerweise", "manchmal", "oft",
       "immer", "sicherlich", "sicher", "meistens", "glücklicherweise",
       ]

# ------------------------------------------------------------------- 1. Passiv
bank("de-b1-passiv", ["P", "AGENT", "TIME", "ADV"],
     ["{P_S} {P_W} {TIME} {ADV} {AGENT} {P_P}.",
      "{TIME} {P_W} {P_S} {ADV} {AGENT} {P_P}.",
      "{P_W} {P_S} {TIME} {ADV} {AGENT} {P_P}?",
      "Warum {P_W} {P_S} {TIME} {ADV} {AGENT} {P_P}?",
      "{P_SP} {P_WP} {TIME} {ADV} {AGENT} {P_P}.",
      "{TIME} {P_WP} {P_SP} {ADV} {AGENT} {P_P}.",
      "{P_WP} {P_SP} {TIME} {ADV} {AGENT} {P_P}?",
      "{ADV} {P_WP} {P_SP} {TIME} {AGENT} {P_P}."],
     {"P": passiv_pairs(), "AGENT": AGENTS, "TIME": TIME_BASE, "ADV": ADV})

# -------------------------------------------------------------- 2. Relativsatz
REL_ROWS = [
    ("Der Mann", "der", "arbeitet", "ist mein Nachbar"),
    ("Die Frau", "die", "arbeitet", "ist meine Nachbarin"),
    ("Das Kind", "das", "spielt", "ist mein Sohn"),
    ("Die Kinder", "die", "spielen", "sind meine Nachbarn"),
    ("Der Lehrer", "der", "unterrichtet", "kommt aus Berlin"),
    ("Die Lehrerin", "die", "unterrichtet", "kommt aus Berlin"),
    ("Der Kollege", "der", "sitzt", "ist sehr freundlich"),
    ("Die Kollegin", "die", "sitzt", "ist sehr freundlich"),
    ("Das Auto", "das", "steht", "gehört meinem Bruder"),
    ("Die Wohnung", "die", "liegt", "ist sehr teuer"),
    ("Der Film", "der", "läuft", "ist wirklich gut"),
    ("Die Bücher", "die", "liegen", "gehören mir"),
    ("Der Bus", "der", "fährt", "ist immer pünktlich"),
    ("Die Tasche", "die", "liegt", "ist meine"),
    ("Das Restaurant", "das", "liegt", "ist sehr bekannt"),
    ("Die Freunde", "die", "wohnen", "kommen aus Hamburg"),
    ("Der Arzt", "der", "arbeitet", "hat Dienst"),
    ("Die Ärztin", "die", "arbeitet", "hat Dienst"),
    ("Der Zug", "der", "ankommt", "hat Verspätung"),
    ("Die Blumen", "die", "wachsen", "sind wunderschön"),
    ("Der Computer", "der", "steht", "funktioniert sehr gut"),
    ("Das Handy", "das", "liegt", "ist kaputt"),
    ("Der Nachbar", "der", "arbeitet", "ist sehr hilfsbereit"),
    ("Die Nachbarin", "die", "arbeitet", "ist sehr hilfsbereit"),
    ("Die Schüler", "die", "lernen", "kommen aus Spanien"),
    ("Der Student", "der", "studiert", "wohnt in Wien"),
    ("Die Studentin", "die", "studiert", "wohnt in Wien"),
    ("Das Café", "das", "liegt", "hat guten Kaffee"),
    ("Der Chef", "der", "arbeitet", "ist nicht da"),
    ("Die Firma", "die", "liegt", "ist sehr groß"),
    ("Der Roman", "der", "liegt", "ist sehr spannend"),
    ("Die Straße", "die", "liegt", "ist ziemlich lang"),
]


def rel_pool():
    out = []
    for np_, rel, rest, main in REL_ROWS:
        out.append({"NP": np_[0].lower() + np_[1:], "REL": rel,
                    "REST": rest, "MAIN": main})
    return out


MANNER = ["gern", "schnell", "ruhig", "sorgfältig", "allein", "ohne Pause",
          "mit Freude", "sehr genau", "recht gut", "ziemlich gut", "zu zweit",
          "mit Geduld"]

bank("de-b1-relativ", ["R", "TIME", "ADV", "MAN"],
     ["{R_NP}, {R_REL} {TIME} {ADV} {MAN} {R_REST}, {R_MAIN}.",
      "{R_NP}, {R_REL} {TIME} {ADV} {MAN} {R_REST}, {R_MAIN}.",
      "{R_NP}, {R_REL} {ADV} {TIME} {MAN} {R_REST}, {R_MAIN}.",
      "{ADV} kennst du {R_NP}, {R_REL} {TIME} {MAN} {R_REST}?",
      "{TIME} kennst du {R_NP}, {R_REL} {ADV} {MAN} {R_REST}?",
      "{R_NP}, {R_REL} {ADV} {MAN} {R_REST}, {R_MAIN} {TIME}.",
      "Ich finde {R_NP}, {R_REL} {TIME} {ADV} {MAN} {R_REST}, sehr interessant.",
      "{TIME} ist {R_NP}, {R_REL} {ADV} {MAN} {R_REST}, sehr bekannt."],
     {"R": rel_pool(), "TIME": TIME_BASE, "ADV": ADV, "MAN": MANNER})

# ------------------------------------------------------------- 3. Konjunktiv II
K2_FORMS = ["würde", "würdest", "würde", "würden", "würdet", "würden"]
K2_PAIRS = [("lernen", "Deutsch"), ("machen", "die Hausaufgaben"),
            ("kaufen", "ein Auto"), ("lesen", "das Buch"),
            ("arbeiten", "im Büro"), ("kochen", "eine Suppe"),
            ("fahren", "nach Berlin"), ("besuchen", "meine Eltern"),
            ("schreiben", "einen Brief"), ("bleiben", "zu Hause"),
            ("anrufen", "den Arzt"), ("aufstehen", "früh")]


def k2_pred_chunks():
    out = []
    for name, comp in K2_PAIRS:
        v = VERBS[name]
        for text, pi in P:
            form = K2_FORMS[pi]
            out.append({"S": text, "V": form, "VS": form + " " + text,
                        "O": comp, "I": v.inf})
    return out


bank("de-b1-konjunktiv2", ["K", "TIME", "ADV"],
     shapes_main("K", "{K_O} {K_I}"),
     {"K": k2_pred_chunks(), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------------- 4. hätte / wäre
O2 = ["mehr Zeit", "mehr Geld", "mehr Geduld", "eine Idee", "einen Plan",
      "einen Termin", "ein Auto", "ein Problem", "Glück", "viel Arbeit",
      "eine Frage", "ein eigenes Haus", "einen Garten", "ein Fahrrad",
      "eine Wohnung", "mehr Ruhe"]
MOOD_ADJ = ["glücklich", "zufrieden", "entspannt", "ruhig", "froh", "bereit",
            "flexibel", "unabhängig", "kreativ", "produktiv", "optimistisch",
            "motiviert", "gelassen", "energisch", "freundlich", "großzügig",
            "hilfsbereit", "neugierig", "zuversichtlich", "spontan"]

bank("de-b1-hte-waere", ["O2", "ADJ", "TIME", "ADV"],
     ["Wenn ich {TIME} {ADV} {O2} hätte, wäre ich {ADJ}.",
      "{TIME} hätte ich {ADV} {O2}, dann wäre ich {ADJ}.",
      "Hätte ich {TIME} {ADV} {O2}, wäre ich {ADJ}.",
      "Ich hätte {TIME} {ADV} {O2}, dann wäre ich {ADJ}.",
      "{ADV} hätte ich {TIME} {O2}, wäre ich {ADJ}.",
      "Ich wäre {TIME} {ADV} {ADJ}, wenn ich {O2} hätte.",
      "{TIME} wäre ich {ADV} {ADJ}, hätte ich {O2}.",
      "{ADV} wäre ich {TIME} {ADJ}, wenn ich {O2} hätte."],
     {"O2": O2, "ADJ": MOOD_ADJ, "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------------------ 5. Genitiv
PERSON_HEADS = ("Lehrer", "Lehrerin", "Arzt", "Ärztin", "Student", "Studentin",
                "Kollege", "Kollegin", "Nachbar", "Nachbarin", "Kind", "Chef",
                "Chefin", "Bruder", "Schwester", "Vater", "Mutter")


def gen_pool():
    out = []
    for item in genitiv_items():
        np_ = item["NP"]
        parts = np_.split(" ")
        if len(parts) >= 4 and parts[1] in PERSON_HEADS \
                and parts[3] in ("Firma", "Vereins", "Teams"):
            continue
        out.append({"NP": np_[0].lower() + np_[1:]})
    return out


bank("de-b1-genitiv", ["G", "TIME", "ADV"],
     ["{TIME} ist {G_NP} {ADV} sehr alt.",
      "{G_NP} ist {TIME} {ADV} wirklich neu.",
      "Ist {G_NP} {TIME} {ADV} neu?",
      "Warum ist {G_NP} {TIME} {ADV} so teuer?",
      "{TIME} finde ich {G_NP} {ADV} praktisch.",
      "{ADV} ist {G_NP} {TIME} kaputt.",
      "{G_NP} ist {TIME} {ADV} leider sehr teuer.",
      "Mir gefällt {G_NP} {TIME} {ADV}."],
     {"G": gen_pool(), "TIME": TIME_BASE, "ADV": ADV})

# --------------------------------------------------- 6. Adjektiv (unbestimmt)
INDEF_NOUNS = [("der", "Tisch", "Tische"), ("der", "Stuhl", "Stühle"),
               ("das", "Fenster", "Fenster"), ("das", "Bett", "Betten"),
               ("das", "Sofa", "Sofas"), ("das", "Buch", "Bücher"),
               ("das", "Auto", "Autos"), ("das", "Zimmer", "Zimmer"),
               ("das", "Haus", "Häuser"), ("das", "Regal", "Regale"),
               ("die", "Lampe", "Lampen"), ("die", "Tür", "Türen"),
               ("die", "Küche", "Küchen"), ("die", "Wohnung", "Wohnungen"),
               ("die", "Tasche", "Taschen"), ("die", "Uhr", "Uhren")]

INDEF_ADJ = ["neu", "alt", "groß", "klein", "schön", "teuer", "billig",
             "modern", "bequem", "praktisch", "kaputt", "sauber", "hell",
             "dunkel", "wichtig", "ruhig", "laut", "warm", "kalt", "gemütlich",
             "leer", "voll", "eng", "komisch", "interessant"]


def indef_pool():
    out = []
    for art, noun, plural in INDEF_NOUNS:
        g = {"der": "m", "die": "f", "das": "n"}[art]
        for adj in INDEF_ADJ:
            if g == "m":
                nom = "ein " + adj + "er " + noun
                akk = "einen " + adj + "en " + noun
            elif g == "f":
                nom = "eine " + adj + "e " + noun
                akk = "eine " + adj + "e " + noun
            else:
                nom = "ein " + adj + "es " + noun
                akk = "ein " + adj + "es " + noun
            out.append({"S": nom, "V": "ist", "VS": "ist " + nom,
                        "AKK": akk, "PL": "viele " + adj + "e " + plural})
    return out


bank("de-b1-adj-unbest", ["NP", "TIME", "ADV"],
     ["{NP_S} gefällt mir {TIME} {ADV}.",
      "{TIME} gefällt mir {NP_S} {ADV}.",
      "Gefällt dir {NP_S} {TIME} {ADV}?",
      "{ADV} gefällt mir {NP_S} {TIME}.",
      "Ich kaufe {NP_AKK} {TIME} {ADV}.",
      "{TIME} kaufe ich {NP_AKK} {ADV}.",
      "Warum gefällt dir {NP_S} {TIME} {ADV} nicht?",
      "{ADV} kaufe ich {NP_AKK} {TIME} nicht."],
     {"NP": indef_pool(), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------ 7. Verben mit festen Präpositionen
def praep_chunks():
    out = []
    for name, pps in PRAEP_VERBEN:
        if name == "gehören":
            continue
        v = VERBS[name]
        for text, pi in P:
            form = v.pres[pi]
            for pp in pps:
                out.append({"S": text, "V": form, "VS": form + " " + text,
                            "PP": pp})
    return out


bank("de-b1-verben-praep", ["VP", "TIME", "ADV"],
     shapes_main("VP", "{VP_PP}"),
     {"VP": praep_chunks(), "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------------ 8. um ... zu
UM_PAIRS = [("lernen", "Deutsch"), ("arbeiten", "im Büro"),
            ("suchen", "die Wohnung"), ("bezahlen", "die Rechnung"),
            ("kochen", "eine Suppe"), ("lesen", "das Buch")]

bank("de-b1-um-zu", ["P", "Z", "TIME", "ADV"],
     ["{P_S} {P_V} {TIME} {ADV} {P_O}, {Z}.",
      "{ADV} {P_V} {P_S} {TIME} {P_O}, {Z}.",
      "{TIME} {P_V} {P_S} {ADV} {P_O}, {Z}.",
      "{P_VS} {TIME} {ADV} {P_O}, {Z}?",
      "Warum {P_VS} {TIME} {ADV} {P_O}, {Z}?",
      "{P_S} {P_V} {TIME} {ADV} nicht {P_O}, {Z}.",
      "{ADV} {P_V} {P_S} {TIME} {P_O} nicht, {Z}.",
      "{TIME} {P_VS} {ADV} {P_O}, {Z}?"],
     {"P": pred_pres(UM_PAIRS, P), "Z": UM_ZU_ITEMS, "TIME": TIME_BASE,
      "ADV": ADV})

# --------------------------------------------------- 9. Konzessiv / Kausal
KONZ_A = [("lernen", "Deutsch"), ("arbeiten", "im Büro"),
          ("kochen", "eine Suppe"), ("lesen", "das Buch"),
          ("spielen", "Fußball"), ("putzen", "die Küche"),
          ("suchen", "den Schlüssel"), ("bezahlen", "die Rechnung")]
KONZ_B = [("arbeiten", "im Garten"), ("lernen", "Deutsch"),
          ("spielen", "Fußball"), ("kochen", "eine Suppe"),
          ("lesen", "das Buch"), ("putzen", "die Küche"),
          ("warten", "auf den Bus"), ("trinken", "einen Tee")]

bank("de-b1-konzessiv", ["C", "Q", "TIME", "ADV"],
     ["{C_S} {C_V} {TIME} {ADV} {C_O}, obwohl {Q_S} {Q_O} {Q_VN}.",
      "Obwohl {Q_S} {TIME} {ADV} {Q_O} {Q_VN}, {C_V} {C_S} {C_O}.",
      "{C_S} {C_V} {TIME} {ADV} {C_O}, weil {Q_S} {Q_O} {Q_VN}.",
      "{Q_S} {Q_VN} {TIME} {ADV} {Q_O}, deshalb {C_V} {C_S} {C_O}.",
      "{C_VS} {TIME} {ADV} {C_O}, obwohl {Q_S} {Q_O} {Q_VN}?",
      "{ADV} {C_V} {C_S} {TIME} {C_O}, obwohl {Q_S} {Q_O} {Q_VN}.",
      "Warum {C_V} {C_S} {TIME} {ADV} {C_O}, obwohl {Q_S} {Q_O} {Q_VN}?",
      "{C_S} {C_V} {TIME} {ADV} nicht {C_O}, weil {Q_S} {Q_O} {Q_VN}."],
     {"C": pred_pres(KONZ_A, P), "Q": pred_pres(KONZ_B, P),
      "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------ 10. Plusquamperfekt
PLUS_PAIRS = [("lernen", "Deutsch"), ("machen", "die Hausaufgaben"),
              ("kaufen", "ein Auto"), ("lesen", "das Buch"),
              ("schreiben", "einen Brief"), ("kochen", "eine Suppe"),
              ("trinken", "einen Tee"), ("gehen", "nach Hause"),
              ("fahren", "nach Berlin"), ("bleiben", "zu Hause"),
              ("arbeiten", "im Büro"), ("suchen", "die Fahrkarte")]

bank("de-b1-plusquam", ["N", "M", "TIME"],
     ["Nachdem {N_S} {N_P} {N_A}, {M_V} {M_S} {TIME} {M_O}.",
      "Nachdem {N_S} {N_P} {N_A}, {M_V} {M_S} {M_O} {TIME}.",
      "{TIME} {M_V} {M_S} {M_O}, nachdem {N_S} {N_P} {N_A}.",
      "Warum {M_V} {M_S} {TIME} {M_O}, nachdem {N_S} {N_P} {N_A}?",
      "Nachdem {N_S} {N_P} {N_A}, {M_V} {M_S} {TIME} {M_O} doch noch.",
      "{N_S} {N_A} {N_P}, danach {M_V} {M_S} {TIME} {M_O}.",
      "Nachdem {N_S} {N_P} {N_A}, {M_V} {M_S} {TIME} {M_O}?",
      "Nachdem {N_S} {N_P} {N_A}, {M_V} {M_S} {M_O}, und zwar {TIME}."],
     {"N": plusquam_chunks([p[0] for p in PLUS_PAIRS], P),
      "M": pred_prat(PLUS_PAIRS, P), "TIME": TIME_PAST})

# ------------------------------------------------- 11. Temporale Nebensätze
TEMP_NS_PAIRS = [("arbeiten", "im Büro"), ("lernen", "Deutsch"),
                 ("spielen", "Fußball"), ("kochen", "eine Suppe"),
                 ("lesen", "das Buch"), ("putzen", "die Küche"),
                 ("warten", "auf den Bus"), ("trinken", "einen Tee")]

bank("de-b1-temporal-ns", ["K", "P", "TIME", "ADV"],
     ["{K} {P_S} {TIME} {ADV} {P_O} {P_V}, war ich sehr müde.",
      "Ich war {TIME} {ADV} müde, {K} {P_S} {P_O} {P_V}.",
      "Warum war ich müde, {K} {P_S} {TIME} {ADV} {P_O} {P_V}?",
      "{ADV} war ich müde, {K} {P_S} {TIME} {P_O} {P_V}.",
      "{K} {P_S} {TIME} {ADV} {P_O} {P_V}, bin ich nach Hause gegangen.",
      "{K} {P_S} {ADV} {P_O} {P_V}, habe ich {TIME} geschlafen.",
      "{TIME} war ich {ADV} müde, {K} {P_S} {P_O} {P_V}.",
      "Warum bin ich nach Hause gegangen, {K} {P_S} {TIME} {ADV} {P_O} {P_V}?"],
     {"K": ["als", "während"], "P": pred_prat(TEMP_NS_PAIRS, P),
      "TIME": TIME_PAST, "ADV": ADV})

# -------------------------------------------------------- 12. Indirekte Fragen
IF_CLAUSES = ["wann der Zug fährt", "ob er heute kommt", "wo sie wohnt",
              "warum er nicht anruft", "wie das funktioniert",
              "wer das gemacht hat", "was er gesagt hat", "wie viel das kostet",
              "ob wir Zeit haben", "wann der Kurs beginnt",
              "wie lange die Reise dauert", "ob das möglich ist",
              "wo der Bahnhof ist", "wann sie ankommt", "warum das so ist",
              "wie ich das machen soll", "ob er die Wahrheit sagt",
              "was wir noch brauchen", "wann es losgeht", "ob das stimmt",
              "wer den Vertrag unterschreibt", "wie spät es ist",
              "wohin wir fahren", "ob sie mitkommt"]
IF_MAIN = [{"A": "ich weiß es", "B": "nicht"},
           {"A": "du kannst mir sagen", "B": ""},
           {"A": "ich frage mich", "B": ""},
           {"A": "niemand weiß es", "B": "genau"},
           {"A": "er möchte es wissen", "B": ""},
           {"A": "sie fragt", "B": ""},
           {"A": "du weißt es", "B": "nicht"},
           {"A": "ich habe es vergessen", "B": ""},
           {"A": "ich verstehe es", "B": "nicht"},
           {"A": "man weiß es", "B": "nicht"}]

bank("de-b1-indirekte-frage", ["IF", "M", "TIME", "ADV"],
     ["{M_A} {TIME} {ADV} {M_B}, {IF}.",
      "{M_A} {ADV} {TIME} {M_B}, {IF}.",
      "{M_A} {TIME} {ADV} {M_B}, und zwar {IF}.",
      "{M_A} {ADV} {TIME} {M_B}, {IF}, oder?",
      "{M_A} {TIME} {ADV} {M_B}, {IF}, richtig?",
      "{M_A} {ADV} {TIME} {M_B} – {IF}.",
      "{M_A} {TIME} {ADV} {M_B}, {IF}, und zwar genau.",
      "{M_A} {ADV} {TIME} {M_B}, {IF}, oder nicht?"],
     {"IF": IF_CLAUSES, "M": IF_MAIN, "TIME": TIME_BASE, "ADV": ADV})

# ------------------------------------------------------------ 13. n-Deklination
def n_dekl_chunks():
    out = []
    for nom, akk, dat, _gen in N_DEKL:
        for name in ("kennen", "sehen", "besuchen", "fragen"):
            v = VERBS[name]
            for text, pi in P:
                out.append({"S": text, "V": v.pres[pi], "O": akk,
                            "VS": v.pres[pi] + " " + text})
        for name in ("helfen", "danken", "antworten", "gratulieren"):
            v = VERBS[name]
            for text, pi in P:
                out.append({"S": text, "V": v.pres[pi], "O": dat,
                            "VS": v.pres[pi] + " " + text})
        out.append({"S": nom, "V": "kommt", "VS": "kommt " + nom,
                    "O": "aus Berlin"})
        out.append({"S": nom, "V": "arbeitet", "VS": "arbeitet " + nom,
                    "O": "im Büro"})
    return out


bank("de-b1-n-deklination", ["ND", "TIME", "ADV"],
     shapes_main("ND", "{ND_O}"),
     {"ND": n_dekl_chunks(), "TIME": TIME_BASE, "ADV": ADV})
