#!/usr/bin/python3
from props import *
from map import GameMap, GameGegenstaende, GameMoebelstuecke

# Ein bescheuertes Textadventure

Inventar = Inventory(132) # Inventar des Spielers


# Fuege Gegenstaende in Moebelstueck ein.

print(GameMap[0].Name + " - " + GameMap[0].Beschreibung)
