#!/usr/bin/python3
from props import *
from map import GameMap

# Ein bescheuertes Textadventure

Inventar = Inventory(132) # Inventar des Spielers
Schwert = Gegenstand("Superschwinger", "Ein Habsburgerischer Degen.", 1, 200)  # Erzeuge Schwert "Superschwinger"
Bogen = Gegenstand("Langbogen", "Ein klassischer, Englischer Langbogen.", 2, 120)  # Erzeuge Bogen "Langbogen"

# Fuege Gegenstaende in Moebelstueck ein.
Schachtel = Moebelstueck("Alte Schachtel", "Links grün versifft, sonst wie neu.", 12, [Schwert, Bogen], False, False)

Schachtel.showAllContents()

print(GameMap[0].Name + " - " + GameMap[0].Beschreibung)