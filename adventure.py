#!/usr/bin/python3
from control import Steuerung
from props import *
from map import GameMap, GameGegenstaende, GameMoebelstuecke

# Ein bescheuertes Textadventure

Inventar = Inventory(3)  # Inventar des Spielers


# Fuege Gegenstaende in Moebelstueck ein.

Kont = Steuerung(GameMap, 0)

Kont.BeschreibeRaum(0)