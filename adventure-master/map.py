from props import Raum, Gegenstand, Moebelstueck


""" Hier werden die einzelnen Gegenstaende initialisiert. """
GameGegenstaende = [
    # Gegenstand("Name", "Beschreibung", "Typ", "Wert")
    Gegenstand("Seppelpracken", "Ein Habsburgischer Degen.", 1, 200),
    Gegenstand("Langbogen", "Ein klassischer, Englischer Langbogen.", 2, 120),
    Gegenstand("Rundschild", "Wodaaaaaaan!", 3, 999),
    Gegenstand("Flügelhelm", "Hergestellt in einem Gallischen Dorf...", 3, 300)
]

""" Hier werden die einzelnen Moebelstuecke initialisiert. """
GameMoebelstuecke = [
    # Moebelstueck("Name", "Beschreibung", "Inventargroesse", "Verschlossen", "Schluessel", "Inhalt"
    Moebelstueck("Alte Schachtel", "Links grün versifft, sonst wie neu.", 12,
                 [GameGegenstaende[0], GameGegenstaende[1]], False, False),
    Moebelstueck("Fass (verschlossen)", "Da machst doch gleich n Fass auf!", 1, [GameGegenstaende[2]], False, False)
]

""" Hier werden die einzelnen Reaume initialisiert und miteinander verknuepft. """
GameMap = [
    # Raum("Name", "Beschreibung", "Rauminhalt", "Verschlossen", "Ausgaenge", "Schluessel")
    Raum(
        "Gute Stube",
        "Eine aufgeraeumte Stube, hier wohnt wohl ein Autist.",
        False,
        [
            GameMoebelstuecke[0],
            GameMoebelstuecke[1]
        ],
        False,
        False
    ),
    Raum(
        "Badezimmer",
        "Der Putz broeckelt von den Waenden.",
        False,
        False,
        False,
        False
    )

]
