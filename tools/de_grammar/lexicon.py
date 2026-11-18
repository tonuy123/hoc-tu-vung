# -*- coding: utf-8 -*-
"""German lexicon for grammar drill banks (A1-B2).

Everything here is pre-inflected on purpose: the JS runtime only substitutes
strings, so agreement (person, case, article) must be baked in at build time.
"""

# (text, person index) - 0 ich, 1 du, 2 er/sie/es, 3 wir, 4 ihr, 5 sie/Sie
PERSONS = [
    ("ich", 0),
    ("du", 1),
    ("er", 2),
    ("sie", 2),
    ("es", 2),
    ("wir", 3),
    ("ihr", 4),
    ("sie", 5),
    ("Tom", 2),
    ("Anna", 2),
    ("mein Bruder", 2),
    ("meine Schwester", 2),
    ("meine Eltern", 5),
    ("die Kinder", 5),
    ("der Lehrer", 2),
    ("die Lehrerin", 2),
    ("Herr Weber", 2),
    ("Frau Klein", 2),
]

P3 = [("er", 2), ("sie", 2), ("Tom", 2), ("Anna", 2), ("mein Bruder", 2),
      ("die Lehrerin", 2), ("Herr Weber", 2)]

P_PL = [("wir", 3), ("ihr", 4), ("sie", 5), ("meine Eltern", 5), ("die Kinder", 5)]


def _weak(stem, e_insert=False):
    e = "e" if e_insert else ""
    return [stem + "e", stem + e + "st", stem + e + "t",
            stem + "en", stem + e + "t", stem + "en"]


def _prat(stem):
    return [stem + "te", stem + "test", stem + "te",
            stem + "ten", stem + "tet", stem + "ten"]


class V(object):
    def __init__(self, inf, pres, prat, part, aux="haben", sep=""):
        self.inf = inf
        self.pres = pres
        self.prat = prat
        self.part = part
        self.aux = aux
        self.sep = sep

    def __repr__(self):
        return "V(%s)" % self.inf


VERBS = {
    # regular
    "lernen": V("lernen", _weak("lern"), ["lernte", "lerntest", "lernte", "lernten", "lerntet", "lernten"], "gelernt"),
    "machen": V("machen", _weak("mach"), ["machte", "machtest", "machte", "machten", "machtet", "machten"], "gemacht"),
    "kaufen": V("kaufen", _weak("kauf"), ["kaufte", "kauftest", "kaufte", "kauften", "kauftet", "kauften"], "gekauft"),
    "suchen": V("suchen", _weak("such"), ["suchte", "suchtest", "suchte", "suchten", "suchtet", "suchten"], "gesucht"),
    "brauchen": V("brauchen", _weak("brauch"), ["brauchte", "brauchtest", "brauchte", "brauchten", "brauchtet", "brauchten"], "gebraucht"),
    "bezahlen": V("bezahlen", _weak("bezahl"), ["bezahlte", "bezahltest", "bezahlte", "bezahlten", "bezahltet", "bezahlten"], "bezahlt"),
    "hören": V("hören", _weak("hör"), ["hörte", "hörtest", "hörte", "hörten", "hörtet", "hörten"], "gehört"),
    "sagen": V("sagen", _weak("sag"), ["sagte", "sagtest", "sagte", "sagten", "sagtet", "sagten"], "gesagt"),
    "fragen": V("fragen", _weak("frag"), ["fragte", "fragtest", "fragte", "fragten", "fragtet", "fragten"], "gefragt"),
    "spielen": V("spielen", _weak("spiel"), ["spielte", "spieltest", "spielte", "spielten", "spieltet", "spielten"], "gespielt"),
    "wohnen": V("wohnen", _weak("wohn"), ["wohnte", "wohntest", "wohnte", "wohnten", "wohntet", "wohnten"], "gewohnt"),
    "arbeiten": V("arbeiten", _weak("arbeit", e_insert=True), ["arbeitete", "arbeitetest", "arbeitete", "arbeiteten", "arbeitetet", "arbeiteten"], "gearbeitet"),
    "besuchen": V("besuchen", _weak("besuch"), ["besuchte", "besuchtest", "besuchte", "besuchten", "besuchtet", "besuchten"], "besucht"),
    "kochen": V("kochen", _weak("koch"), ["kochte", "kochtest", "kochte", "kochten", "kochtet", "kochten"], "gekocht"),
    "putzen": V("putzen", _weak("putz"), ["putzte", "putztest", "putzte", "putzten", "putztet", "putzten"], "geputzt"),
    "öffnen": V("öffnen", _weak("öffn", e_insert=True), ["öffnete", "öffnetest", "öffnete", "öffneten", "öffnetet", "öffneten"], "geöffnet"),
    # stem change present
    "fahren": V("fahren", ["fahre", "fährst", "fährt", "fahren", "fahrt", "fahren"],
                ["fuhr", "fuhrst", "fuhr", "fuhren", "fuhrt", "fuhren"], "gefahren", aux="sein"),
    "schlafen": V("schlafen", ["schlafe", "schläfst", "schläft", "schlafen", "schlaft", "schlafen"],
                  ["schlief", "schliefst", "schlief", "schliefen", "schlieft", "schliefen"], "geschlafen"),
    "laufen": V("laufen", ["laufe", "läufst", "läuft", "laufen", "lauft", "laufen"],
                ["lief", "liefst", "lief", "liefen", "lieft", "liefen"], "gelaufen", aux="sein"),
    "essen": V("essen", ["esse", "isst", "isst", "essen", "esst", "essen"],
               ["aß", "aßest", "aß", "aßen", "aßt", "aßen"], "gegessen"),
    "lesen": V("lesen", ["lese", "liest", "liest", "lesen", "lest", "lesen"],
               ["las", "last", "las", "lasen", "last", "lasen"], "gelesen"),
    "sprechen": V("sprechen", ["spreche", "sprichst", "spricht", "sprechen", "sprecht", "sprechen"],
                  ["sprach", "sprachst", "sprach", "sprachen", "spracht", "sprachen"], "gesprochen"),
    "nehmen": V("nehmen", ["nehme", "nimmst", "nimmt", "nehmen", "nehmt", "nehmen"],
                ["nahm", "nahmst", "nahm", "nahmen", "nahmt", "nahmen"], "genommen"),
    "sehen": V("sehen", ["sehe", "siehst", "sieht", "sehen", "seht", "sehen"],
               ["sah", "sahst", "sah", "sahen", "saht", "sahen"], "gesehen"),
    "geben": V("geben", ["gebe", "gibst", "gibt", "geben", "gebt", "geben"],
               ["gab", "gabst", "gab", "gaben", "gabt", "gaben"], "gegeben"),
    "treffen": V("treffen", ["treffe", "triffst", "trifft", "treffen", "trefft", "treffen"],
                 ["traf", "trafst", "traf", "trafen", "traft", "trafen"], "getroffen"),
    # auxiliaries / irregular
    "sein": V("sein", ["bin", "bist", "ist", "sind", "seid", "sind"],
              ["war", "warst", "war", "waren", "wart", "waren"], "gewesen", aux="sein"),
    "haben": V("haben", ["habe", "hast", "hat", "haben", "habt", "haben"],
               ["hatte", "hattest", "hatte", "hatten", "hattet", "hatten"], "gehabt"),
    "werden": V("werden", ["werde", "wirst", "wird", "werden", "werdet", "werden"],
                ["wurde", "wurdest", "wurde", "wurden", "wurdet", "wurden"], "geworden", aux="sein"),
    # modals
    "können": V("können", ["kann", "kannst", "kann", "können", "könnt", "können"],
                ["konnte", "konntest", "konnte", "konnten", "konntet", "konnten"], "gekonnt"),
    "müssen": V("müssen", ["muss", "musst", "muss", "müssen", "müsst", "müssen"],
                ["musste", "musstest", "musste", "mussten", "musstet", "mussten"], "gemusst"),
    "wollen": V("wollen", ["will", "willst", "will", "wollen", "wollt", "wollen"],
                ["wollte", "wolltest", "wollte", "wollten", "wolltet", "wollten"], "gewollt"),
    "dürfen": V("dürfen", ["darf", "darfst", "darf", "dürfen", "dürft", "dürfen"],
                ["durfte", "durftest", "durfte", "durften", "durftet", "durften"], "gedurft"),
    "sollen": V("sollen", ["soll", "sollst", "soll", "sollen", "sollt", "sollen"],
                ["sollte", "solltest", "sollte", "sollten", "solltet", "sollten"], "gesollt"),
    "mögen": V("mögen", ["mag", "magst", "mag", "mögen", "mögt", "mögen"],
               ["mochte", "mochtest", "mochte", "mochten", "mochtet", "mochten"], "gemocht"),
    # separable
    "aufstehen": V("aufstehen", ["stehe auf", "stehst auf", "steht auf", "stehen auf", "steht auf", "stehen auf"],
                   ["stand auf", "standst auf", "stand auf", "standen auf", "standet auf", "standen auf"],
                   "aufgestanden", aux="sein", sep="auf"),
    "anrufen": V("anrufen", ["rufe an", "rufst an", "ruft an", "rufen an", "ruft an", "rufen an"],
                 ["rief an", "riefst an", "rief an", "riefen an", "rieft an", "riefen an"],
                 "angerufen", sep="an"),
    "einkaufen": V("einkaufen", ["kaufe ein", "kaufst ein", "kauft ein", "kaufen ein", "kauft ein", "kaufen ein"],
                   ["kaufte ein", "kauftest ein", "kaufte ein", "kauften ein", "kauftet ein", "kauften ein"],
                   "eingekauft", sep="ein"),
    "aufmachen": V("aufmachen", ["mache auf", "machst auf", "macht auf", "machen auf", "macht auf", "machen auf"],
                   ["machte auf", "machtest auf", "machte auf", "machten auf", "machtet auf", "machten auf"],
                   "aufgemacht", sep="auf"),
    "anfangen": V("anfangen", ["fange an", "fängst an", "fängt an", "fangen an", "fangt an", "fangen an"],
                  ["fing an", "fingst an", "fing an", "fingen an", "fingt an", "fingen an"],
                  "angefangen", sep="an"),
    "mitkommen": V("mitkommen", ["komme mit", "kommst mit", "kommt mit", "kommen mit", "kommt mit", "kommen mit"],
                   ["kam mit", "kamst mit", "kam mit", "kamen mit", "kamt mit", "kamen mit"],
                   "mitgekommen", aux="sein", sep="mit"),
    "einladen": V("einladen", ["lade ein", "lädst ein", "lädt ein", "laden ein", "ladet ein", "laden ein"],
                  ["lud ein", "ludst ein", "lud ein", "luden ein", "ludet ein", "luden ein"],
                  "eingeladen", sep="ein"),
    "finden": V("finden", ["finde", "findest", "findet", "finden", "findet", "finden"],
                ["fand", "fandst", "fand", "fanden", "fandet", "fanden"], "gefunden"),
    "gehen": V("gehen", ["gehe", "gehst", "geht", "gehen", "geht", "gehen"],
               ["ging", "gingst", "ging", "gingen", "gingt", "gingen"], "gegangen", aux="sein"),
    "helfen": V("helfen", ["helfe", "hilfst", "hilft", "helfen", "helft", "helfen"],
                ["half", "halfst", "half", "halfen", "halft", "halfen"], "geholfen"),
    "warten": V("warten", _weak("wart", True),
                ["wartete", "wartetest", "wartete", "warteten", "wartetet", "warteten"], "gewartet"),
    "trinken": V("trinken", ["trinke", "trinkst", "trinkt", "trinken", "trinkt", "trinken"],
                 ["trank", "trankst", "trank", "tranken", "trankt", "tranken"], "getrunken"),
    "bringen": V("bringen", ["bringe", "bringst", "bringt", "bringen", "bringt", "bringen"],
                 ["brachte", "brachtest", "brachte", "brachten", "brachtet", "brachten"], "gebracht"),
    "schreiben": V("schreiben", ["schreibe", "schreibst", "schreibt", "schreiben", "schreibt", "schreiben"],
                   ["schrieb", "schriebst", "schrieb", "schrieben", "schriebt", "schrieben"], "geschrieben"),
    "waschen": V("waschen", ["wasche", "wäschst", "wäscht", "waschen", "wascht", "waschen"],
                 ["wusch", "wuschst", "wusch", "wuschen", "wuscht", "wuschen"], "gewaschen"),
    "zahlen": V("zahlen", _weak("zahl"), _prat("zahl"), "gezahlt"),
    "holen": V("holen", _weak("hol"), _prat("hol"), "geholt"),
    "räumen": V("räumen", _weak("räum"), _prat("räum"), "geräumt"),
    "schließen": V("schließen", ["schließe", "schließt", "schließt", "schließen", "schließt", "schließen"],
                   ["schloss", "schlossest", "schloss", "schlossen", "schlosst", "schlossen"], "geschlossen"),
    "antworten": V("antworten", _weak("antwort", True),
                   ["antwortete", "antwortetest", "antwortete", "antworteten", "antwortetet", "antworteten"],
                   "geantwortet"),
    "erzählen": V("erzählen", _weak("erzähl"), _prat("erzähl"), "erzählt"),
    "bleiben": V("bleiben", ["bleibe", "bleibst", "bleibt", "bleiben", "bleibt", "bleiben"],
                 ["blieb", "bliebst", "blieb", "blieben", "bliebt", "blieben"], "geblieben", aux="sein"),
    "vergessen": V("vergessen", ["vergesse", "vergisst", "vergisst", "vergessen", "vergesst", "vergessen"],
                   ["vergaß", "vergaßest", "vergaß", "vergaßen", "vergaßt", "vergaßen"], "vergessen"),
    "empfehlen": V("empfehlen", ["empfehle", "empfiehlst", "empfiehlt", "empfehlen", "empfehlt", "empfehlen"],
                   ["empfahl", "empfahlst", "empfahl", "empfahlen", "empfahlt", "empfahlen"], "empfohlen"),
    "reparieren": V("reparieren", _weak("reparier"), _prat("reparier"), "repariert"),
    "organisieren": V("organisieren", _weak("organisier"), _prat("organisier"), "organisiert"),
    "besichtigen": V("besichtigen", _weak("besichtig"), _prat("besichtig"), "besichtigt"),
    "besprechen": V("besprechen", ["bespreche", "besprichst", "bespricht", "besprechen", "besprecht", "besprechen"],
                    ["besprach", "besprachst", "besprach", "besprachen", "bespracht", "besprachen"], "besprochen"),
    "entscheiden": V("entscheiden", ["entscheide", "entscheidest", "entscheidet", "entscheiden", "entscheidet", "entscheiden"],
                     ["entschied", "entschiedst", "entschied", "entschieden", "entschiedet", "entschieden"], "entschieden"),
    "erreichen": V("erreichen", _weak("erreich"), _prat("erreich"), "erreicht"),
    "verbessern": V("verbessern", _weak("verbesser"), _prat("verbesser"), "verbessert"),
    "verschieben": V("verschieben", ["verschiebe", "verschiebst", "verschiebt", "verschieben", "verschiebt", "verschieben"],
                     ["verschob", "verschobst", "verschob", "verschoben", "verschobt", "verschoben"], "verschoben"),
    "bauen": V("bauen", _weak("bau"), _prat("bau"), "gebaut"),
    "prüfen": V("prüfen", _weak("prüf"), _prat("prüf"), "geprüft"),
    "verkaufen": V("verkaufen", _weak("verkauf"), _prat("verkauf"), "verkauft"),
    "liefern": V("liefern", _weak("liefer"), _prat("liefer"), "geliefert"),
    "benutzen": V("benutzen", _weak("benutz"), _prat("benutz"), "benutzt"),
    "passieren": V("passieren", _weak("passier"), _prat("passier"), "passiert", aux="sein"),
    "einsteigen": V("einsteigen", ["steige ein", "steigst ein", "steigt ein", "steigen ein", "steigt ein", "steigen ein"],
                    ["stieg ein", "stiegst ein", "stieg ein", "stiegen ein", "stiegt ein", "stiegen ein"],
                    "eingestiegen", aux="sein", sep="ein"),
    "aussteigen": V("aussteigen", ["steige aus", "steigst aus", "steigt aus", "steigen aus", "steigt aus", "steigen aus"],
                    ["stieg aus", "stiegst aus", "stieg aus", "stiegen aus", "stiegt aus", "stiegen aus"],
                    "ausgestiegen", aux="sein", sep="aus"),
    "umsteigen": V("umsteigen", ["steige um", "steigst um", "steigt um", "steigen um", "steigt um", "steigen um"],
                   ["stieg um", "stiegst um", "stieg um", "stiegen um", "stiegt um", "stiegen um"],
                   "umgestiegen", aux="sein", sep="um"),
    "ankommen": V("ankommen", ["komme an", "kommst an", "kommt an", "kommen an", "kommt an", "kommen an"],
                  ["kam an", "kamst an", "kam an", "kamen an", "kamt an", "kamen an"],
                  "angekommen", aux="sein", sep="an"),
    "abfahren": V("abfahren", ["fahre ab", "fährst ab", "fährt ab", "fahren ab", "fahrt ab", "fahren ab"],
                  ["fuhr ab", "fuhrst ab", "fuhr ab", "fuhren ab", "fuhrt ab", "fuhren ab"],
                  "abgefahren", aux="sein", sep="ab"),
    "gratulieren": V("gratulieren", _weak("gratulier"), _prat("gratulier"), "gratuliert"),
    "danken": V("danken", _weak("dank"), _prat("dank"), "gedankt"),
    "zuhören": V("zuhören", ["höre zu", "hörst zu", "hört zu", "hören zu", "hört zu", "hören zu"],
                 ["hörte zu", "hörtest zu", "hörte zu", "hörten zu", "hörtet zu", "hörten zu"],
                 "zugehört", sep="zu"),
    "vertrauen": V("vertrauen", _weak("vertrau"), _prat("vertrau"), "vertraut"),
    "folgen": V("folgen", _weak("folg"), _prat("folg"), "gefolgt", aux="sein"),
    "begegnen": V("begegnen", _weak("begegn", True), _prat("begegn"), "begegnet", aux="sein"),
    "hoffen": V("hoffen", _weak("hoff"), _prat("hoff"), "gehofft"),
    "denken": V("denken", ["denke", "denkst", "denkt", "denken", "denkt", "denken"],
                ["dachte", "dachtest", "dachte", "dachten", "dachtet", "dachten"], "gedacht"),
    "diskutieren": V("diskutieren", _weak("diskutier"), _prat("diskutier"), "diskutiert"),
    "bitten": V("bitten", ["bitte", "bittest", "bittet", "bitten", "bittet", "bitten"],
                ["bat", "batst", "bat", "baten", "batet", "baten"], "gebeten"),
    "achten": V("achten", _weak("acht", True),
                ["achtete", "achtetest", "achtete", "achteten", "achtetet", "achteten"], "geachtet"),
    "teilnehmen": V("teilnehmen", ["nehme teil", "nimmst teil", "nimmt teil", "nehmen teil", "nehmt teil", "nehmen teil"],
                    ["nahm teil", "nahmst teil", "nahm teil", "nahmen teil", "nahmt teil", "nahmen teil"],
                    "teilgenommen", sep="teil"),
    "abhängen": V("abhängen", ["hänge ab", "hängst ab", "hängt ab", "hängen ab", "hängt ab", "hängen ab"],
                  ["hing ab", "hingst ab", "hing ab", "hingen ab", "hingt ab", "hingen ab"],
                  "abgehangen", sep="ab"),
    "gehören": V("gehören", _weak("gehör"), _prat("gehör"), "gehört"),
    "bestehen": V("bestehen", ["bestehe", "bestehst", "besteht", "bestehen", "besteht", "bestehen"],
                  ["bestand", "bestandst", "bestand", "bestanden", "bestandet", "bestanden"],
                  "bestanden"),
    "protestieren": V("protestieren", _weak("protestier"), _prat("protestier"), "protestiert"),
    "versuchen": V("versuchen", _weak("versuch"), _prat("versuch"), "versucht"),
    "beginnen": V("beginnen", ["beginne", "beginnst", "beginnt", "beginnen", "beginnt", "beginnen"],
                  ["begann", "begannst", "begann", "begannen", "begannt", "begannen"], "begonnen"),
    "kommen": V("kommen", ["komme", "kommst", "kommt", "kommen", "kommt", "kommen"],
                ["kam", "kamst", "kam", "kamen", "kamt", "kamen"], "gekommen", aux="sein"),
    "kennen": V("kennen", ["kenne", "kennst", "kennt", "kennen", "kennt", "kennen"],
                ["kannte", "kanntest", "kannte", "kannten", "kanntet", "kannten"], "gekannt"),
}

REGULAR = ["lernen", "machen", "kaufen", "suchen", "brauchen", "hören", "sagen",
           "fragen", "spielen", "wohnen", "arbeiten", "besuchen", "kochen", "putzen"]
IRREGULAR_PRES = ["fahren", "schlafen", "laufen", "essen", "lesen", "sprechen",
                  "nehmen", "sehen", "geben", "treffen"]
SEPARABLE = ["aufstehen", "anrufen", "einkaufen", "aufmachen", "anfangen",
             "mitkommen", "einladen"]
MODALS = ["können", "müssen", "wollen", "dürfen", "sollen", "mögen"]
SEIN_VERBS = ["fahren", "laufen", "aufstehen", "mitkommen"]

# --------------------------------------------------------------------------
# pre-inflected pools

OBJ_TEXT = ["den Text", "den Brief", "den Bericht", "das Buch", "die E-Mail",
            "die Aufgabe", "den Artikel", "das Formular", "die Nachricht",
            "den Vertrag", "das Heft", "die Zeitung"]

OBJ_FOOD = ["den Apfel", "die Suppe", "das Brot", "den Kuchen", "den Salat",
            "das Frühstück", "den Kaffee", "den Tee", "das Wasser", "die Pizza",
            "das Ei", "den Reis"]

OBJ_THING = ["den Laptop", "das Handy", "den Tisch", "das Auto", "die Fahrkarte",
             "den Schlüssel", "die Tasche", "das Fahrrad", "den Drucker",
             "die Kamera", "den Stuhl", "das Regal"]

OBJ_PERSON = ["den Chef", "die Kollegin", "den Nachbarn", "den Arzt",
              "die Lehrerin", "den Freund", "den Bruder", "die Schwester",
              "den Vater", "die Mutter", "das Kind", "den Mann"]

DAT_PERSON = ["dem Chef", "der Kollegin", "dem Nachbarn", "dem Arzt",
              "der Lehrerin", "dem Freund", "dem Bruder", "der Schwester",
              "dem Vater", "der Mutter", "dem Kind", "dem Mann"]

DAT_THING = ["dem Kunden", "der Firma", "dem Team", "der Gruppe", "dem Verein"]

TIME_BASE = ["heute", "morgen", "jetzt", "am Montag", "am Dienstag",
             "am Abend", "am Morgen", "am Wochenende", "jeden Tag", "jede Woche",
             "um acht Uhr", "um neun Uhr", "nach dem Frühstück", "vor dem Essen",
             "in der Mittagspause", "nächste Woche", "nächsten Monat",
             "im Sommer", "im Winter", "am Nachmittag", "zu dieser Zeit",
             "jeden Abend", "heute Abend"]

TIME_PAST = ["gestern", "vorgestern", "letzte Woche", "letzten Monat",
             "letzten Sommer", "vor einer Woche", "vor drei Tagen",
             "am Montag", "am Dienstag", "am Abend", "im Winter",
             "um acht Uhr", "in der Mittagspause", "nach dem Frühstück",
             "am Wochenende", "zu dieser Zeit", "damals", "neulich"]

ADV = ["gern", "oft", "immer", "manchmal", "nie", "leider", "natürlich",
       "wahrscheinlich", "schnell", "langsam", "sehr gut", "allein", "zusammen",
       "wieder", "noch", "schon", "hoffentlich", "eigentlich", "sicherlich",
       "meistens", "wirklich", "vielleicht"]

PLACE_ROOM = ["in der Küche", "im Wohnzimmer", "im Büro", "im Schlafzimmer",
              "im Flur", "im Garten", "auf dem Balkon", "in der Garage",
              "im Keller", "in der Schule", "im Supermarkt", "im Restaurant",
              "im Hotel", "am Bahnhof", "in der Bibliothek", "beim Arzt",
              "in der Firma", "zu Hause", "in der Stadt", "im Park",
              "an der Wand", "auf dem Tisch", "im Regal", "vor dem Haus",
              "neben dem Bett"]

PLACE_CITY = ["in Berlin", "in Wien", "in München", "in Hamburg", "in Zürich",
              "in Frankfurt", "in Köln", "in Dresden", "in Leipzig", "in Salzburg"]

# noun table: (article, noun, plural article+noun, accusative article, dative article)
NOUNS = [
    ("der", "Tisch", "die Tische", "den", "dem"),
    ("der", "Stuhl", "die Stühle", "den", "dem"),
    ("das", "Bett", "die Betten", "das", "dem"),
    ("das", "Sofa", "die Sofas", "das", "dem"),
    ("der", "Schrank", "die Schränke", "den", "dem"),
    ("die", "Lampe", "die Lampen", "die", "der"),
    ("die", "Tür", "die Türen", "die", "der"),
    ("das", "Fenster", "die Fenster", "das", "dem"),
    ("der", "Teppich", "die Teppiche", "den", "dem"),
    ("das", "Regal", "die Regale", "das", "dem"),
    ("der", "Computer", "die Computer", "den", "dem"),
    ("das", "Handy", "die Handys", "das", "dem"),
    ("der", "Drucker", "die Drucker", "den", "dem"),
    ("die", "Kamera", "die Kameras", "die", "der"),
    ("der", "Schlüssel", "die Schlüssel", "den", "dem"),
    ("die", "Tasche", "die Taschen", "die", "der"),
    ("das", "Buch", "die Bücher", "das", "dem"),
    ("der", "Stift", "die Stifte", "den", "dem"),
    ("das", "Heft", "die Hefte", "das", "dem"),
    ("die", "Zeitung", "die Zeitungen", "die", "der"),
    ("der", "Apfel", "die Äpfel", "den", "dem"),
    ("das", "Brot", "die Brote", "das", "dem"),
    ("die", "Milch", "die Milch", "die", "der"),
    ("der", "Käse", "die Käse", "den", "dem"),
    ("das", "Wasser", "die Wasser", "das", "dem"),
    ("der", "Kaffee", "die Kaffees", "den", "dem"),
    ("der", "Tee", "die Tees", "den", "dem"),
    ("die", "Suppe", "die Suppen", "die", "der"),
    ("der", "Salat", "die Salate", "den", "dem"),
    ("das", "Ei", "die Eier", "das", "dem"),
    ("der", "Zug", "die Züge", "den", "dem"),
    ("das", "Auto", "die Autos", "das", "dem"),
    ("das", "Fahrrad", "die Fahrräder", "das", "dem"),
    ("der", "Bus", "die Busse", "den", "dem"),
    ("die", "Bahn", "die Bahnen", "die", "der"),
    ("der", "Bahnhof", "die Bahnhöfe", "den", "dem"),
    ("die", "Straße", "die Straßen", "die", "der"),
    ("der", "Park", "die Parks", "den", "dem"),
    ("die", "Schule", "die Schulen", "die", "der"),
    ("die", "Universität", "die Universitäten", "die", "der"),
    ("das", "Büro", "die Büros", "das", "dem"),
    ("die", "Firma", "die Firmen", "die", "der"),
    ("der", "Supermarkt", "die Supermärkte", "den", "dem"),
    ("das", "Restaurant", "die Restaurants", "das", "dem"),
    ("das", "Hotel", "die Hotels", "das", "dem"),
    ("die", "Küche", "die Küchen", "die", "der"),
    ("das", "Wohnzimmer", "die Wohnzimmer", "das", "dem"),
    ("der", "Garten", "die Gärten", "den", "dem"),
    ("die", "Stadt", "die Städte", "die", "der"),
    ("das", "Dorf", "die Dörfer", "das", "dem"),
    ("der", "Arzt", "die Ärzte", "den", "dem"),
    ("der", "Lehrer", "die Lehrer", "den", "dem"),
    ("das", "Kind", "die Kinder", "das", "dem"),
    ("die", "Frau", "die Frauen", "die", "der"),
    ("der", "Mann", "die Männer", "den", "dem"),
    ("der", "Freund", "die Freunde", "den", "dem"),
    ("die", "Familie", "die Familien", "die", "der"),
]

ADJ_PRED = ["neu", "alt", "groß", "klein", "schön", "teuer", "billig", "modern",
            "bequem", "praktisch", "kaputt", "sauber", "schmutzig", "hell",
            "dunkel", "wichtig", "interessant", "langweilig", "ruhig", "laut",
            "warm", "kalt", "freundlich", "gemütlich", "komisch"]


def pres_chunks(verb_names, persons):
    """Subject + finite verb; VE keeps the separable prefix attached."""
    out = []
    for name in verb_names:
        v = VERBS[name]
        for text, pi in persons:
            form = v.pres[pi]
            if v.sep:
                main = form.rsplit(" ", 1)[0]
                d = {"S": text, "V": main, "P": v.sep, "VS": main + " " + text,
                     "VE": form, "VN": form.replace(" ", "")}
            else:
                d = {"S": text, "V": form, "P": "", "VS": form + " " + text,
                     "VE": form, "VN": form}
            out.append(d)
    return out


def _perf_aux(v, pi):
    if v.aux == "sein":
        return ["bin", "bist", "ist", "sind", "seid", "sind"][pi]
    return ["habe", "hast", "hat", "haben", "habt", "haben"][pi]


def perf_chunks(verb_names, persons):
    """Subject + haben/sein + Partizip II (PA = participle + aux, verb final)."""
    out = []
    for name in verb_names:
        v = VERBS[name]
        for text, pi in persons:
            aux = _perf_aux(v, pi)
            out.append({"S": text, "A": aux, "P": v.part,
                        "VS": aux + " " + text, "PA": v.part + " " + aux,
                        "VP": aux + " " + v.part})
    return out


def prat_chunks(verb_names, persons):
    out = []
    for name in verb_names:
        v = VERBS[name]
        for text, pi in persons:
            form = v.prat[pi]
            out.append({"S": text, "V": form, "VS": form + " " + text,
                        "VE": form})
    return out


def modal_chunks(modal_names, infinitives, persons):
    out = []
    for m in modal_names:
        v = VERBS[m]
        for inf in infinitives:
            for text, pi in persons:
                form = v.pres[pi]
                out.append({"S": text, "M": form, "I": inf,
                            "MS": form + " " + text, "MI": inf + " " + form})
    return out


def modal_prat_chunks(modal_names, infinitives, persons):
    out = []
    for m in modal_names:
        v = VERBS[m]
        for inf in infinitives:
            for text, pi in persons:
                form = v.prat[pi]
                out.append({"S": text, "M": form, "I": inf,
                            "MS": form + " " + text, "MI": inf + " " + form})
    return out


def nominativ_nouns():
    return [(a, n) for a, n, _p, _ak, _da in NOUNS]


def akk_nouns():
    return [(ak, n) for _a, n, _p, ak, _da in NOUNS]


def dat_nouns():
    return [(da, n) for _a, n, _p, _ak, da in NOUNS]


# ---------------------------------------------------------------- A1 pools

PLURAL_POOL = []
for _a, _n, _pl, _ak, _da in NOUNS:
    PLURAL_POOL.append({"A": _a, "N": _n, "PL": _pl})

POSS_TABLE = {"mein": ("meinen", "meine", "mein"),
              "dein": ("deinen", "deine", "dein"),
              "sein": ("seinen", "seine", "sein"),
              "ihr": ("ihren", "ihre", "ihr"),
              "unser": ("unseren", "unsere", "unser"),
              "euer": ("euren", "eure", "euer")}

POSS_ITEMS = [("Bruder", "m"), ("Schwester", "f"), ("Handy", "n"),
              ("Chef", "m"), ("Kollegin", "f"), ("Auto", "n"),
              ("Schlüssel", "m"), ("Tasche", "f"), ("Buch", "n"),
              ("Freund", "m"), ("Freundin", "f"), ("Fahrrad", "n"),
              ("Vater", "m"), ("Mutter", "f"), ("Kind", "n"),
              ("Nachbar", "m"), ("Lehrerin", "f"), ("Computer", "m"),
              ("Lampe", "f"), ("Zimmer", "n")]


def poss_items():
    out = []
    idx = {"m": 0, "f": 1, "n": 2}
    for stem, forms in POSS_TABLE.items():
        nom = stem if stem != "euer" else "euer"
        for noun, g in POSS_ITEMS:
            akk = forms[idx[g]] + " " + noun
            nf = (nom if g != "euer" else "euer") + " " + noun
            out.append({"P": akk, "PN": nf})
    return out


PLACE_ALL = PLACE_ROOM + PLACE_CITY

TIME_SHORT = ["heute", "morgen", "gestern", "jetzt", "am Montag", "am Dienstag",
              "am Abend", "am Morgen", "am Wochenende", "jeden Tag", "jede Woche",
              "um acht Uhr", "um neun Uhr", "nach dem Frühstück", "vor dem Essen",
              "in der Mittagspause", "im Sommer", "im Winter", "am Nachmittag"]

# --------------------------------------------------------------- A2 helpers

def passiv_pairs():
    """(subject, plural subject, participle) - pair keeps meaning sensible."""
    rows = [
        ("das Haus", "die Häuser", "gebaut"),
        ("die Wohnung", "die Wohnungen", "renoviert"),
        ("das Büro", "die Büros", "geputzt"),
        ("die Küche", "die Küchen", "geputzt"),
        ("das Auto", "die Autos", "repariert"),
        ("das Fahrrad", "die Fahrräder", "repariert"),
        ("der Brief", "die Briefe", "geschrieben"),
        ("die E-Mail", "die E-Mails", "geschrieben"),
        ("der Bericht", "die Berichte", "geprüft"),
        ("die Rechnung", "die Rechnungen", "bezahlt"),
        ("der Vertrag", "die Verträge", "unterschrieben"),
        ("das Formular", "die Formulare", "ausgefüllt"),
        ("die Aufgabe", "die Aufgaben", "erledigt"),
        ("das Problem", "die Probleme", "gelöst"),
        ("das Zimmer", "die Zimmer", "gestrichen"),
        ("der Tisch", "die Tische", "verkauft"),
        ("das Fenster", "die Fenster", "geöffnet"),
        ("die Tür", "die Türen", "geschlossen"),
        ("das Paket", "die Pakete", "geliefert"),
        ("die Fahrkarte", "die Fahrkarten", "gekauft"),
        ("der Text", "die Texte", "übersetzt"),
        ("das Essen", "die Speisen", "gekocht"),
        ("der Kuchen", "die Kuchen", "gebacken"),
        ("das Buch", "die Bücher", "gelesen"),
        ("der Film", "die Filme", "gesehen"),
        ("die Präsentation", "die Präsentationen", "vorbereitet"),
        ("der Termin", "die Termine", "verschoben"),
        ("das Projekt", "die Projekte", "organisiert"),
        ("die Maschine", "die Maschinen", "benutzt"),
        ("der Schlüssel", "die Schlüssel", "gefunden"),
    ]
    out = []
    for sg, pl, part in rows:
        out.append({"S": sg, "SP": pl, "P": part,
                    "W": "wird", "WP": "werden",
                    "PW": part + " wird", "PPW": part + " werden"})
    return out


AGENTS = ["von dem Chef", "von der Firma", "von den Kindern", "von meinem Bruder",
          "von der Lehrerin", "vom Team", "von dem Nachbarn", "von der Polizei"]


def adj_stems():
    return ["neu", "alt", "groß", "klein", "schön", "teur", "billig", "modern",
            "bequem", "praktisch", "kaputt", "sauber", "schmutzig", "hell",
            "dunkl", "wichtig", "interessant", "langweilig", "ruhig", "laut",
            "warm", "kalt", "freundlich", "gemütlich", "komisch"]


ADJ_END = {
    "def": {"nom": {"m": "e", "f": "e", "n": "e", "p": "en"},
            "akk": {"m": "en", "f": "e", "n": "e", "p": "en"},
            "dat": {"m": "en", "f": "en", "n": "en", "p": "en"},
            "gen": {"m": "en", "f": "en", "n": "en", "p": "en"}},
    "indef": {"nom": {"m": "er", "f": "e", "n": "es", "p": "en"},
              "akk": {"m": "en", "f": "e", "n": "es", "p": "en"},
              "dat": {"m": "en", "f": "en", "n": "en", "p": "en"},
              "gen": {"m": "en", "f": "en", "n": "en", "p": "en"}},
    "zero": {"nom": {"m": "er", "f": "e", "n": "es", "p": "e"},
             "akk": {"m": "en", "f": "e", "n": "es", "p": "e"},
             "dat": {"m": "em", "f": "er", "n": "em", "p": "en"},
             "gen": {"m": "en", "f": "er", "n": "en", "p": "er"}},
}

DEF_ART = {"m": "der", "f": "die", "n": "das", "p": "die"}
DEF_ART_AKK = {"m": "den", "f": "die", "n": "das", "p": "die"}
DEF_ART_DAT = {"m": "dem", "f": "der", "n": "dem", "p": "den"}
INDEF_ART = {"m": "ein", "f": "eine", "n": "ein", "p": "keine"}
INDEF_ART_AKK = {"m": "einen", "f": "eine", "n": "ein", "p": "keine"}


def gender_of(article):
    return {"der": "m", "die": "f", "das": "n"}[article]


def adj_np_pool(mode="def", case="nom", limit_nouns=None):
    """Full adjective+noun phrases with correct endings."""
    nouns = NOUNS[:limit_nouns] if limit_nouns else NOUNS
    out = []
    for art, noun, plural, akk_art, dat_art in nouns:
        g = gender_of(art)
        sing = [("s", g, art, noun)]
        out_sg = sing[0]
        s, gg, a, n = out_sg
        end = ADJ_END[mode][case][gg]
        if mode == "def":
            det = {"nom": art, "akk": akk_art, "dat": dat_art,
                   "gen": "des" if gg in ("m", "n") else "der"}[case]
            if case == "gen":
                end = "en"
        elif mode == "indef":
            det = {"nom": INDEF_ART[gg], "akk": INDEF_ART_AKK[gg],
                   "dat": {"m": "einem", "f": "einer", "n": "einem"}[gg],
                   "gen": {"m": "eines", "f": "einer", "n": "eines"}[gg]}[case]
        else:
            det = ""
            if case == "dat":
                det = ""
        for adj in adj_stems():
            ph = (det + " " if det else "") + adj + end + " " + noun
            out.append(ph)
    return out


def adj_np_plural(mode="def", case="nom"):
    out = []
    for art, noun, plural, akk_art, dat_art in NOUNS:
        g = "p"
        end = ADJ_END[mode][case]["p"]
        if mode == "def":
            det = {"nom": "die", "akk": "die", "dat": "den", "gen": "der"}[case]
        elif mode == "indef":
            det = "keine"
        else:
            det = ""
        for adj in adj_stems():
            ph = (det + " " if det else "") + adj + end + " " + plural.split(" ", 1)[1]
            out.append(ph)
    return out


# --------------------------------------------------------------- B helpers

REL_ITEMS = [
    ("Der Mann", "der", "arbeitet", "ist mein Nachbar", "m"),
    ("Die Frau", "die", "arbeitet", "ist meine Nachbarin", "f"),
    ("Das Kind", "das", "spielt", "ist mein Sohn", "n"),
    ("Die Kinder", "die", "spielen", "sind meine Nachbarn", "p"),
    ("Der Lehrer", "der", "unterrichtet", "kommt aus Berlin", "m"),
    ("Die Lehrerin", "die", "unterrichtet", "kommt aus Berlin", "f"),
    ("Der Kollege", "der", "sitzt", "ist sehr freundlich", "m"),
    ("Die Kollegin", "die", "sitzt", "ist sehr freundlich", "f"),
    ("Das Auto", "das", "steht", "gehört meinem Bruder", "n"),
    ("Die Wohnung", "die", "liegt", "ist sehr teuer", "f"),
    ("Der Film", "der", "läuft", "war wirklich gut", "m"),
    ("Die Bücher", "die", "liegen", "gehören mir", "p"),
    ("Der Bus", "der", "fährt", "ist immer pünktlich", "m"),
    ("Die Tasche", "die", "liegt", "ist meine", "f"),
    ("Das Restaurant", "das", "liegt", "ist sehr bekannt", "n"),
    ("Die Freunde", "die", "kommen", "wohnen in Hamburg", "p"),
    ("Der Arzt", "der", "arbeitet", "ist sehr erfahren", "m"),
    ("Die Ärztin", "die", "arbeitet", "ist sehr erfahren", "f"),
    ("Der Zug", "der", "fährt", "hat Verspätung", "m"),
    ("Die Blumen", "die", "wachsen", "sind wunderschön", "p"),
    ("Der Computer", "der", "steht", "funktioniert sehr gut", "m"),
    ("Das Handy", "das", "liegt", "muss repariert werden", "n"),
    ("Der Nachbar", "der", "arbeitet", "ist sehr hilfsbereit", "m"),
    ("Die Nachbarin", "die", "arbeitet", "ist sehr hilfsbereit", "f"),
    ("Die Schüler", "die", "lernen", "kommen aus Spanien", "p"),
    ("Der Student", "der", "studiert", "wohnt in Wien", "m"),
    ("Die Studentin", "die", "studiert", "wohnt in Wien", "f"),
    ("Das Café", "das", "liegt", "hat guten Kaffee", "n"),
    ("Der Chef", "der", "ist", "ruft später an", "m"),
    ("Die Firma", "die", "sucht", "ist sehr groß", "f"),
]

GEN_PAIRS = [
    ("das Auto", "meines Bruders"), ("das Zimmer", "meiner Schwester"),
    ("der Computer", "des Lehrers"), ("die Tasche", "der Kollegin"),
    ("das Buch", "des Studenten"), ("die Wohnung", "der Familie"),
    ("das Handy", "meines Freundes"), ("der Schlüssel", "des Nachbarn"),
    ("das Fahrrad", "meines Kindes"), ("die Zeitung", "des Vaters"),
    ("das Haus", "der Eltern"), ("der Tisch", "der Firma"),
]

N_DEKL = [
    ("der Student", "den Studenten", "dem Studenten", "des Studenten"),
    ("der Junge", "den Jungen", "dem Jungen", "des Jungen"),
    ("der Nachbar", "den Nachbarn", "dem Nachbarn", "des Nachbarn"),
    ("der Kollege", "den Kollegen", "dem Kollegen", "des Kollegen"),
    ("der Mensch", "den Menschen", "dem Menschen", "des Menschen"),
    ("der Herr", "den Herrn", "dem Herrn", "des Herrn"),
    ("der Polizist", "den Polizisten", "dem Polizisten", "des Polizisten"),
    ("der Journalist", "den Journalisten", "dem Journalisten", "des Journalisten"),
    ("der Präsident", "den Präsidenten", "dem Präsidenten", "des Präsidenten"),
    ("der Chef", "den Chef", "dem Chef", "des Chefs"),
    ("der Kunde", "den Kunden", "dem Kunden", "des Kunden"),
    ("der Experte", "den Experten", "dem Experten", "des Experten"),
]

NOMINAL_PP = ["beim Lernen", "beim Kochen", "beim Lesen", "beim Essen",
              "nach dem Essen", "nach der Arbeit", "nach dem Unterricht",
              "vor dem Schlafen", "vor dem Treffen", "während der Arbeit",
              "während der Pause", "während des Unterrichts", "trotz der Kälte",
              "trotz des Regens", "wegen des Wetters", "wegen der Arbeit",
              "beim Sport", "nach dem Sport", "vor dem Frühstück"]

MAIN_CLAUSES = [
    {"S": "ich", "V": "gehe", "R": "spazieren"},
    {"S": "ich", "V": "höre", "R": "Musik"},
    {"S": "er", "V": "liest", "R": "ein Buch"},
    {"S": "sie", "V": "kocht", "R": "eine Suppe"},
    {"S": "wir", "V": "treffen", "R": "Freunde"},
    {"S": "die Kinder", "V": "spielen", "R": "im Garten"},
    {"S": "mein Bruder", "V": "arbeitet", "R": "im Büro"},
    {"S": "die Studenten", "V": "lernen", "R": "Deutsch"},
    {"S": "ich", "V": "trinke", "R": "einen Kaffee"},
    {"S": "sie", "V": "fährt", "R": "nach Berlin"},
]

K1_ITEMS = [
    ("Er sagt,", "er", "habe", "keine Zeit"),
    ("Er sagt,", "er", "sei", "krank"),
    ("Sie meint,", "sie", "müsse", "arbeiten"),
    ("Sie sagt,", "sie", "könne", "nicht kommen"),
    ("Der Chef sagt,", "er", "werde", "später anrufen"),
    ("Die Firma sagt,", "sie", "habe", "keine Stelle"),
    ("Er erklärt,", "er", "wolle", "mitkommen"),
    ("Sie antwortet,", "sie", "dürfe", "das nicht"),
    ("Der Lehrer sagt,", "der Test", "sei", "einfach"),
    ("Die Ärztin sagt,", "ich", "solle", "mich ausruhen"),
    ("Er behauptet,", "er", "habe", "das nicht gewusst"),
    ("Sie betont,", "sie", "sei", "pünktlich gewesen"),
]

JE_DESTO = [
    ("mehr", "ich lerne", "besser", "verstehe ich"),
    ("länger", "ich warte", "ungeduldiger", "werde ich"),
    ("früher", "du kommst", "mehr Zeit", "haben wir"),
    ("schneller", "du fährst", "gefährlicher", "wird es"),
    ("mehr", "du übst", "sicherer", "sprichst du"),
    ("höher", "wir steigen", "kälter", "wird es"),
    ("weniger", "ich arbeite", "entspannter", "bin ich"),
    ("mehr", "man lernt", "besser", "versteht man"),
]


# ------------------------------------------------------- topic-specific pools

def imperativ_items():
    """(du, Sie) imperative forms with the object already attached."""
    rows = [
        ("mach", "Machen Sie", "die Tür", "zu"),
        ("mach", "Machen Sie", "das Fenster", "auf"),
        ("räum", "Räumen Sie", "das Zimmer", "auf"),
        ("kauf", "Kaufen Sie", "das Brot", ""),
        ("lern", "Lernen Sie", "den Text", ""),
        ("öffne", "Öffnen Sie", "die Tür", ""),
        ("schließ", "Schließen Sie", "das Fenster", ""),
        ("ruf", "Rufen Sie", "den Arzt", "an"),
        ("bring", "Bringen Sie", "die Tasche", "mit"),
        ("lies", "Lesen Sie", "den Brief", ""),
        ("schreib", "Schreiben Sie", "die E-Mail", ""),
        ("putze", "Putzen Sie", "die Küche", ""),
        ("wasch", "Waschen Sie", "das Auto", ""),
        ("hol", "Holen Sie", "den Schlüssel", ""),
        ("zahl", "Zahlen Sie", "die Rechnung", ""),
        ("nimm", "Nehmen Sie", "den Bus", ""),
        ("trink", "Trinken Sie", "einen Tee", ""),
        ("iss", "Essen Sie", "eine Suppe", ""),
        ("fahr", "Fahren Sie", "nach Berlin", ""),
        ("sprich", "Sprechen Sie", "mit dem Chef", ""),
        ("warte", "Warten Sie", "auf den Bus", ""),
        ("antworte", "Antworten Sie", "auf die Frage", ""),
        ("erzähl", "Erzählen Sie", "die Geschichte", ""),
        ("hilf", "Helfen Sie", "dem Nachbarn", ""),
        ("bleib", "Bleiben Sie", "zu Hause", ""),
        ("steh", "Stehen Sie", "früh", "auf"),
        ("komm", "Kommen Sie", "pünktlich", "mit"),
        ("kauf", "Kaufen Sie", "die Fahrkarte", "ein"),
        ("schick", "Schicken Sie", "das Paket", ""),
        ("buch", "Buchen Sie", "das Hotel", ""),
        ("pack", "Packen Sie", "den Koffer", ""),
        ("klingel", "Klingeln Sie", "beim Nachbarn", ""),
        ("gieß", "Gießen Sie", "die Blumen", ""),
        ("deck", "Decken Sie", "den Tisch", ""),
        ("spül", "Spülen Sie", "das Geschirr", ""),
        ("wisch", "Wischen Sie", "den Boden", ""),
        ("häng", "Hängen Sie", "das Bild", "auf"),
    ]
    out = []
    for du, sie, obj, sep in rows:
        ob = obj + (" " + sep if sep else "")
        for verb in (du, sie):
            out.append({"V": verb[0].lower() + verb[1:], "OB": ob})
    return out


def wechsel_chunks(persons):
    """Direction (gehen) and location (sein) finite forms for the same person."""
    out = []
    for text, pi in persons:
        out.append({"S": text, "MD": VERBS["gehen"].pres[pi],
                    "ML": VERBS["sein"].pres[pi],
                    "MS": VERBS["gehen"].pres[pi] + " " + text})
    return out


WECHSEL_PAIRS = [
    {"DIR": "in die Stadt", "LOC": "in der Stadt"},
    {"DIR": "in die Schule", "LOC": "in der Schule"},
    {"DIR": "in das Büro", "LOC": "im Büro"},
    {"DIR": "in die Küche", "LOC": "in der Küche"},
    {"DIR": "in den Garten", "LOC": "im Garten"},
    {"DIR": "in das Wohnzimmer", "LOC": "im Wohnzimmer"},
    {"DIR": "in das Schlafzimmer", "LOC": "im Schlafzimmer"},
    {"DIR": "in das Restaurant", "LOC": "im Restaurant"},
    {"DIR": "in den Supermarkt", "LOC": "im Supermarkt"},
    {"DIR": "in das Hotel", "LOC": "im Hotel"},
    {"DIR": "in die Bibliothek", "LOC": "in der Bibliothek"},
    {"DIR": "in den Park", "LOC": "im Park"},
    {"DIR": "auf den Tisch", "LOC": "auf dem Tisch"},
    {"DIR": "auf den Balkon", "LOC": "auf dem Balkon"},
    {"DIR": "auf die Straße", "LOC": "auf der Straße"},
    {"DIR": "auf den Bahnhof", "LOC": "auf dem Bahnhof"},
    {"DIR": "auf das Sofa", "LOC": "auf dem Sofa"},
    {"DIR": "auf die Bank", "LOC": "auf der Bank"},
    {"DIR": "an die Wand", "LOC": "an der Wand"},
    {"DIR": "an den See", "LOC": "am See"},
    {"DIR": "an den Bahnhof", "LOC": "am Bahnhof"},
    {"DIR": "neben das Bett", "LOC": "neben dem Bett"},
    {"DIR": "unter den Tisch", "LOC": "unter dem Tisch"},
    {"DIR": "vor das Haus", "LOC": "vor dem Haus"},
    {"DIR": "hinter das Haus", "LOC": "hinter dem Haus"},
    {"DIR": "zwischen die Stühle", "LOC": "zwischen den Stühlen"},
]

REFLEXIV = [
    ("freuen", "auf", ["auf den Urlaub", "auf das Wochenende", "auf die Reise"],
     ["freue", "freust", "freut", "freuen", "freut", "freuen"], "gefreut"),
    ("interessieren", "für", ["für Sport", "für Musik", "für Sprachen"],
     ["interessiere", "interessierst", "interessiert", "interessieren", "interessiert", "interessieren"], "interessiert"),
    ("erinnern", "an", ["an den Termin", "an die Schule", "an den Sommer"],
     ["erinnere", "erinnerst", "erinnert", "erinnern", "erinnert", "erinnern"], "erinnert"),
    ("ärgern", "über", ["über das Wetter", "über den Lärm", "über die Arbeit"],
     ["ärgere", "ärgerst", "ärgert", "ärgern", "ärgert", "ärgern"], "geärgert"),
    ("bedanken", "für", ["für die Hilfe", "für das Geschenk", "für die Einladung"],
     ["bedanke", "bedankst", "bedankt", "bedanken", "bedankt", "bedanken"], "bedankt"),
    ("beschäftigen", "mit", ["mit dem Projekt", "mit der Aufgabe", "mit dem Text"],
     ["beschäftige", "beschäftigst", "beschäftigt", "beschäftigen", "beschäftigt", "beschäftigen"], "beschäftigt"),
]

REFLEXIV_PRON = ["mich", "dich", "sich", "uns", "euch", "sich"]


def reflexiv_chunks(persons):
    out = []
    for inf, prep, pps, forms, part in REFLEXIV:
        for text, pi in persons:
            for pp in pps:
                out.append({"S": text, "R": REFLEXIV_PRON[pi], "V": forms[pi],
                            "PP": pp, "P": part,
                            "VR": forms[pi] + " " + REFLEXIV_PRON[pi]})
    return out


DATIVE_VERBS = ["helfen", "danken", "gratulieren", "zuhören", "antworten",
                "vertrauen", "folgen", "begegnen"]


def dativ_chunks(pairs, persons):
    """pairs: [(verb, dative_object), ...] - keeps cases semantically correct."""
    out = []
    for name, obj in pairs:
        v = VERBS[name]
        for text, pi in persons:
            form = v.pres[pi]
            out.append({"S": text, "V": form, "D": obj, "VS": form + " " + text})
    return out


# ------------------------------------------------------------ predication
# (verb, complement) pairs: the complement is chosen per verb so the drill
# never produces nonsense like "Ich fahre den Text".

# ------------------------------------------------------------ template shapes
# The drill engine needs every template of a bank to reference every declared
# dimension, otherwise two different index tuples render the same sentence.
# These shape builders emit templates that (a) use S/V/VS, TIME and ADV in every
# row and (b) keep German word order legal:
#   * TIME follows the finite verb (or opens the clause),
#   * ADV sits in the middle field, never as a dangling clause-final element,
#   * anything that must stay last (separable prefix, participle, infinitive)
#     lives inside `comp`, which is always the final chunk.

def adj_stem(adj):
    """Adjectives like teuer/dunkel drop the -e- before an ending."""
    return {"teuer": "teur", "sauer": "saur", "dunkel": "dunkl",
            "übel": "übl", "edel": "edl"}.get(adj, adj)


def shapes_main(p, comp="{P_O}", neg=True):
    """9 main-clause templates for one item dim `p`."""
    s, v, vs = "{%s_S}" % p, "{%s_V}" % p, "{%s_VS}" % p
    out = [
        "%s %s {TIME} {ADV} %s." % (s, v, comp),
        "%s {TIME} {ADV} %s?" % (vs, comp),
        "{ADV} %s %s {TIME} %s." % (v, s, comp),
        "{TIME} %s %s {ADV} %s." % (v, s, comp),
        "Warum %s {TIME} {ADV} %s?" % (vs, comp),
        "{TIME} %s {ADV} %s?" % (vs, comp),
        "%s %s {TIME} {ADV} %s, oder?" % (s, v, comp),
        "{ADV} %s %s {TIME} %s, richtig?" % (v, s, comp),
    ]
    if neg:
        out.append("%s %s {TIME} {ADV} nicht %s." % (s, v, comp))
        out.append("{ADV} %s %s {TIME} nicht %s." % (v, s, comp))
    else:
        out.append("{TIME} %s %s {ADV} %s." % (v, s, comp))
        out.append("%s %s {TIME} {ADV} %s, ja?" % (s, v, comp))
    return out


def shapes_yfrage(p, comp="{P_O}"):
    """8 yes/no-question templates."""
    s, v, vs = "{%s_S}" % p, "{%s_V}" % p, "{%s_VS}" % p
    return [
        "%s {TIME} {ADV} %s?" % (vs, comp),
        "%s %s {TIME} {ADV} %s?" % (v, s, comp),
        "{ADV} %s %s {TIME} %s?" % (v, s, comp),
        "%s {TIME} {ADV} %s?" % (vs, comp),
        "{TIME} %s %s {ADV} %s?" % (v, s, comp),
        "%s {TIME} {ADV} nicht %s?" % (vs, comp),
        "%s {TIME} {ADV} %s oder nicht?" % (vs, comp),
        "{ADV} %s %s {TIME} %s, ja?" % (v, s, comp),
    ]


SUB_MAINS = [
    "ich bleibe zu Hause",
    "ich frage vorsichtig",
    "er kommt nicht mit",
    "wir warten hier",
    "sie geht nach Hause",
    "die Kinder sind still",
    "ich bin sehr müde",
    "er ruft später an",
]


def shapes_sub(p, comp="{P_O}", conj="weil"):
    """8 templates with a verb-final subordinate clause."""
    s, vn = "{%s_S}" % p, "{%s_VN}" % p
    out = []
    for i, main in enumerate(SUB_MAINS):
        k = i % 4
        if k == 0:
            tpl = "%s, %s %s {TIME} {ADV} %s %s." % (main, conj, s, comp, vn)
        elif k == 1:
            tpl = "%s, %s %s {TIME} {ADV} %s %s." % (main, conj, s, comp, vn)
        elif k == 2:
            tpl = "%s, %s %s {TIME} {ADV} nicht %s %s." % (main, conj, s, comp, vn)
        else:
            tpl = "%s, %s %s {TIME} {ADV} %s %s." % (main, conj, s, comp, vn)
        out.append(tpl)
    return out


def shapes_pair(a, b, link="K", comp_a="{A_O}", comp_b="{B_O}"):
    """8 two-clause templates; every row uses both dims plus TIME and ADV."""
    rows = [
        "{A_S} {A_V} {TIME} {ADV} %(a)s, {%(l)s} {B_S} {B_V} %(b)s.",
        "{%(l)s} {B_S} {B_V} %(b)s, {A_S} {A_V} {TIME} {ADV} %(a)s.",
        "{A_VS} {TIME} {ADV} %(a)s, {%(l)s} {B_S} {B_V} %(b)s?",
        "{ADV} {A_V} {A_S} {TIME} %(a)s, {%(l)s} {B_S} {B_V} %(b)s.",
        "Warum {A_VS} {TIME} {ADV} %(a)s, {%(l)s} {B_S} {B_V} %(b)s?",
        "{TIME} {A_V} {A_S} {ADV} %(a)s, {%(l)s} {B_S} {B_V} %(b)s.",
        "{ADV} {A_V} {A_S} {TIME} %(a)s, {%(l)s} {B_S} {B_V} %(b)s, ja?",
        "{TIME} {A_VS} {ADV} %(a)s, {%(l)s} {B_S} {B_V} %(b)s?",
    ]
    return [r % {"a": comp_a, "l": link, "b": comp_b} for r in rows]


def pred_pres(pairs, persons):
    out = []
    for name, comp in pairs:
        v = VERBS[name]
        for text, pi in persons:
            form = v.pres[pi]
            if v.sep:
                main, pref = form.rsplit(" ", 1)
            else:
                main, pref = form, ""
            out.append({"S": text, "V": main, "P": pref, "O": comp,
                        "VS": main + " " + text, "VE": form,
                        "VN": (pref + main) if v.sep else main})
    return out


def pred_perf(pairs, persons):
    out = []
    for name, comp in pairs:
        v = VERBS[name]
        for text, pi in persons:
            aux = _perf_aux(v, pi)
            out.append({"S": text, "A": aux, "V": aux, "P": v.part, "O": comp,
                        "PA": v.part + " " + aux, "VS": aux + " " + text})
    return out


def pred_prat(pairs, persons):
    out = []
    for name, comp in pairs:
        v = VERBS[name]
        for text, pi in persons:
            form = v.prat[pi]
            if v.sep:
                main, pref = form.rsplit(" ", 1)
            else:
                main, pref = form, ""
            out.append({"S": text, "V": main, "P": pref, "O": comp,
                        "VS": main + " " + text})
    return out


def pred_modal(modal_names, pairs, persons):
    """Modal + (infinitive, complement) pair; complement fits the infinitive."""
    out = []
    for m in modal_names:
        mv = VERBS[m]
        for inf_name, comp in pairs:
            iv = VERBS[inf_name]
            for text, pi in persons:
                form = mv.pres[pi]
                out.append({"S": text, "M": form, "V": form, "I": iv.inf,
                            "O": comp, "MS": form + " " + text,
                            "VS": form + " " + text})
    return out


def pred_modal_prat(modal_names, pairs, persons):
    out = []
    for m in modal_names:
        mv = VERBS[m]
        for inf_name, comp in pairs:
            iv = VERBS[inf_name]
            for text, pi in persons:
                form = mv.prat[pi]
                out.append({"S": text, "M": form, "V": form, "I": iv.inf,
                            "O": comp, "MS": form + " " + text,
                            "VS": form + " " + text})
    return out

def k2_chunks(persons):
    wd = ["würde", "würdest", "würde", "würden", "würdet", "würden"]
    ht = ["hätte", "hättest", "hätte", "hätten", "hättet", "hätten"]
    wr = ["wäre", "wärst", "wäre", "wären", "wärt", "wären"]
    out = []
    for text, pi in persons:
        out.append({"S": text, "WD": wd[pi], "HT": ht[pi], "WR": wr[pi],
                    "WDS": wd[pi] + " " + text})
    return out


def plusquam_chunks(verb_names, persons):
    """Subject + hatte/waren (Präteritum of the perfect auxiliary) + participle."""
    out = []
    for name in verb_names:
        v = VERBS[name]
        for text, pi in persons:
            if v.aux == "sein":
                aux = ["war", "warst", "war", "waren", "wart", "waren"][pi]
            else:
                aux = ["hatte", "hattest", "hatte", "hatten", "hattet", "hatten"][pi]
            out.append({"S": text, "A": aux, "P": v.part,
                        "PA": v.part + " " + aux})
    return out


def modal_passiv_items():
    modals = ["muss", "kann", "soll", "darf", "will"]
    pl_forms = ["müssen", "können", "sollen", "dürfen", "wollen"]
    out = []
    for row in passiv_pairs():
        for ms, mp in zip(modals, pl_forms):
            out.append({"S": row["S"], "SP": row["SP"], "P": row["P"],
                        "M": ms, "MP": mp,
                        "MPW": ms + " " + row["P"] + " werden"})
    return out


POSSESSORS = ["meines Bruders", "meiner Schwester", "des Lehrers",
              "der Kollegin", "des Kindes", "der Eltern", "meines Freundes",
              "meiner Mutter", "des Nachbarn", "der Familie", "des Studenten",
              "der Firma", "meines Vaters", "der Lehrerin", "des Chefs"]


def genitiv_items():
    out = []
    for art, noun, plural, akk, dat in NOUNS:
        for poss in POSSESSORS:
            out.append({"NP": art + " " + noun + " " + poss,
                        "PL": plural + " " + poss})
    return out


RELP_ITEMS = [
    ("Der Mann", "mit dem", "ich zusammenarbeite", "ist sehr nett"),
    ("Die Frau", "mit der", "ich zusammenarbeite", "ist sehr nett"),
    ("Der Kollege", "von dem", "ich dir erzählt habe", "kommt aus Wien"),
    ("Die Kollegin", "von der", "ich dir erzählt habe", "kommt aus Wien"),
    ("Das Buch", "über das", "wir gesprochen haben", "ist sehr interessant"),
    ("Der Film", "über den", "alle reden", "läuft seit gestern"),
    ("Die Wohnung", "in der", "wir wohnen", "ist ziemlich klein"),
    ("Das Zimmer", "in dem", "ich arbeite", "ist sehr hell"),
    ("Der Tisch", "auf dem", "die Bücher liegen", "ist neu"),
    ("Die Bank", "auf der", "wir sitzen", "ist im Park"),
    ("Der Zug", "mit dem", "ich fahre", "hat Verspätung"),
    ("Die Firma", "für die", "ich arbeite", "ist international"),
    ("Der Chef", "bei dem", "ich arbeite", "ist sehr freundlich"),
    ("Die Aufgabe", "an der", "ich gerade arbeite", "ist schwierig"),
    ("Das Projekt", "an dem", "wir arbeiten", "endet im Mai"),
    ("Die Leute", "mit denen", "ich arbeite", "sind sehr hilfsbereit"),
    ("Die Freunde", "bei denen", "ich wohne", "sind im Urlaub"),
    ("Der Arzt", "zu dem", "ich gehe", "hat heute Sprechstunde"),
    ("Die Ärztin", "zu der", "ich gehe", "hat heute Sprechstunde"),
    ("Das Café", "in dem", "wir uns treffen", "liegt am Markt"),
    ("Der Park", "in dem", "die Kinder spielen", "ist sehr groß"),
    ("Die Schule", "in die", "mein Sohn geht", "ist ganz in der Nähe"),
    ("Der Kurs", "an dem", "ich teilnehme", "dauert drei Monate"),
    ("Die Prüfung", "auf die", "ich mich vorbereite", "ist nächste Woche"),
    ("Der Vertrag", "über den", "wir verhandeln", "ist noch nicht fertig"),
    ("Die Rechnung", "für die", "ich bezahlt habe", "liegt auf dem Tisch"),
    ("Das Auto", "mit dem", "mein Bruder fährt", "ist ziemlich alt"),
    ("Die Tasche", "in der", "mein Handy ist", "steht im Flur"),
    ("Der Nachbar", "mit dem", "ich mich unterhalte", "ist Rentner"),
    ("Die Nachbarin", "mit der", "ich mich unterhalte", "ist Rentnerin"),
    ("Der Kurs", "für den", "ich mich angemeldet habe", "beginnt im Mai"),
    ("Die Stelle", "für die", "ich mich beworben habe", "ist schon besetzt"),
    ("Das Thema", "über das", "wir diskutieren", "ist sehr aktuell"),
    ("Der Plan", "von dem", "alle sprechen", "ist noch geheim"),
    ("Die Entscheidung", "auf die", "wir warten", "ist wichtig"),
    ("Das Angebot", "auf das", "ich gehofft habe", "ist endlich da"),
    ("Der Kollege", "an den", "ich mich erinnere", "arbeitet jetzt in Köln"),
    ("Die Kollegin", "an die", "ich mich erinnere", "arbeitet jetzt in Köln"),
    ("Das Projekt", "von dem", "ich dir erzählt habe", "ist abgeschlossen"),
    ("Die Besprechung", "an der", "ich teilgenommen habe", "war sehr lang"),
    ("Der Termin", "auf den", "ich mich freue", "ist am Freitag"),
    ("Das Geschenk", "über das", "sie sich gefreut hat", "war nicht teuer"),
    ("Die Wohnung", "nach der", "ich suche", "ist ziemlich groß"),
    ("Der Job", "um den", "es hier geht", "ist sehr interessant"),
    ("Die Bibliothek", "in der", "ich lerne", "ist sehr ruhig"),
    ("Das Museum", "in dem", "wir waren", "ist wirklich sehenswert"),
    ("Der Zug", "auf den", "wir warten", "kommt zu spät"),
    ("Die Firma", "mit der", "wir zusammenarbeiten", "sitzt in Berlin"),
]

ERSATZ_ITEMS = [
    ("Das Problem", "ist zu lösen", "lässt sich lösen", "ist lösbar"),
    ("Die Aufgabe", "ist zu erledigen", "lässt sich erledigen", "ist erledigbar"),
    ("Der Vertrag", "ist zu unterschreiben", "lässt sich unterschreiben", "ist unterschreibbar"),
    ("Die Rechnung", "ist zu bezahlen", "lässt sich bezahlen", "ist bezahlbar"),
    ("Das Formular", "ist auszufüllen", "lässt sich ausfüllen", "ist ausfüllbar"),
    ("Das Haus", "ist zu verkaufen", "lässt sich verkaufen", "ist verkäuflich"),
    ("Das Auto", "ist zu reparieren", "lässt sich reparieren", "ist reparierbar"),
    ("Die Tür", "ist zu schließen", "lässt sich schließen", "ist schließbar"),
    ("Das Paket", "ist zu liefern", "lässt sich liefern", "ist lieferbar"),
    ("Die Wohnung", "ist zu renovieren", "lässt sich renovieren", "ist renovierbar"),
    ("Der Text", "ist zu übersetzen", "lässt sich übersetzen", "ist übersetzbar"),
    ("Die Frage", "ist zu beantworten", "lässt sich beantworten", "ist beantwortbar"),
    ("Das Projekt", "ist zu finanzieren", "lässt sich finanzieren", "ist finanzierbar"),
    ("Die Maschine", "ist zu benutzen", "lässt sich benutzen", "ist benutzbar"),
    ("Der Termin", "ist zu verschieben", "lässt sich verschieben", "ist verschiebbar"),
]

TEMPORAL_PP = ["am Montag", "am Dienstag", "am Wochenende", "am Abend",
               "am Morgen", "seit einer Woche", "seit drei Jahren", "vor dem Essen",
               "nach dem Unterricht", "während der Ferien", "während der Arbeit",
               "bis zum Abend", "gegen acht Uhr", "innerhalb einer Stunde",
               "außerhalb der Stadt", "vor drei Jahren", "nach der Arbeit",
               "in der Mittagspause", "im Sommer", "im Winter", "jeden Morgen",
               "jeden Abend", "zu dieser Zeit", "in letzter Zeit"]

PRAEP_VERBEN = [
    ("warten", ["auf den Bus", "auf die Antwort", "auf den Zug"]),
    ("hoffen", ["auf gutes Wetter", "auf eine Antwort", "auf den Sommer"]),
    ("denken", ["an den Termin", "an die Arbeit", "an den Urlaub"]),
    ("sprechen", ["über den Film", "über das Problem", "über die Arbeit"]),
    ("diskutieren", ["über das Projekt", "über die Politik", "über den Plan"]),
    ("bitten", ["um Hilfe", "um einen Termin", "um Geld"]),
    ("achten", ["auf die Zeit", "auf den Preis", "auf die Kinder"]),
    ("gehören", ["zu dem Team", "zu der Firma", "zu der Familie"]),
    ("protestieren", ["gegen den Plan", "gegen die Regel", "gegen die Entscheidung"]),
]

UM_ZU_ITEMS = [
    "um den Test zu bestehen", "um mehr zu verdienen", "um fit zu bleiben",
    "um Deutsch zu lernen", "um die Prüfung zu schaffen", "um früher anzukommen",
    "um Geld zu sparen", "um besser zu verstehen", "um Zeit zu gewinnen",
    "um schneller zu fahren", "um gesünder zu leben", "um mehr zu erfahren",
    "um die Arbeit zu beenden", "um Freunde zu treffen", "um Urlaub zu machen",
    "um den Vertrag zu unterschreiben", "um das Projekt zu beenden",
    "um neue Leute kennenzulernen", "um die Wohnung zu renovieren",
    "um im Ausland zu arbeiten",
]

PARTIZIP_STEMS = ["gebaut", "gekauft", "geöffnet", "geschlossen", "gemietet",
                  "verkauft", "repariert", "geputzt", "geschrieben", "gelesen",
                  "gekocht", "gebacken", "vorbereitet", "organisiert", "erledigt",
                  "gelöst", "geprüft", "geliefert", "benutzt", "gestrichen",
                  "verschoben", "übersetzt", "eingeladen", "besucht", "gesucht",
                  "gefunden", "gewaschen", "gezahlt", "geholt", "erklärt"]


def partizip_np_pool():
    out = []
    for art, noun, plural, akk, dat in NOUNS:
        g = gender_of(art)
        for stem in PARTIZIP_STEMS:
            end = ADJ_END["def"]["nom"][g]
            out.append({"NP": art + " " + stem + end + " " + noun,
                        "PL": "die " + stem + "en " + plural.split(" ", 1)[1]})
    return out

