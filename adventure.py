#!/usr/bin/python3
from props import *

# Ein bescheuertes Textadventure

"""
Inventar = Inventory(132) # Inventar des Spielers
Schwert = Gegenstand("Superschwinger", "Ein Habsburgerischer Degen.", 1, 200)  # Erzeuge Schwert "Superschwinger"
Bogen = Gegenstand("Langbogen","Ein klassischer, Englischer Langbogen.", 2, 120)  # Erzeuge Bogen "Langbogen"

Inventar.addToInventory(Schwert)
Inventar.addToInventory(Bogen)

Inventar.deleteFromInventory(Schwert)

Inventar.showAll()
"""

Moebelstueck("Alte Schachtel","Links grün versifft, aber sonst wie neu.",12,False,False)

Moebelstueck.gebeInhaltAus()