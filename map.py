"""
Contains the Map of Rooms.
Hier werden die einzelnen Reaume initialisiert und miteinander verknuepft.
"""

from props import Raum, Gegenstand, Moebelstueck

GameMap = [
    Raum("Gute Stube", "Eine aufgeraeumte Stube, hier wohnt wohl ein Autist.", [2, 3, 7], False, False, False),
    Raum("Badezimmer", "Der Putz broeckelt von den Waenden.", [1], False, False, False)
]

GameGegenstaende = [
    Gegenstand("Superschwinger", "Ein Habsburgerischer Degen.", 1, 200),
    Gegenstand("Langbogen", "Ein klassischer, Englischer Langbogen.", 2, 120)
]

GameMoebelstuecke = [
    Moebelstueck("Alte Schachtel", "Links grün versifft, sonst wie neu.", 12, [GameGegenstaende[0], GameGegenstaende[1]], False, False)
]