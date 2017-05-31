#!/usr/bin/python3

# Ein bescheuertes Textadventure

class Gegenstand(object):

    def __init__(self, nameDesGegenstands, typDesGegenstands, wertDesGegenstands):
        super(Gegenstand,self).__init__()
        self.Name = nameDesGegenstands
        self.Typ = typDesGegenstands
        self.Wert = wertDesGegenstands

class Inventory(object):
    """Diese Klasse stellt ein Inventar dar."""

    def __init__(self):
        super(Inventory, self).__init__()
        self.__inventory = []

    def showAll(self):
        if len(self.__inventory) == 0:
            print("Das Inventar ist leer.")
        else:
            for Gegenstand in __inventory:
                print(Gegenstand.Name)

    def addToInventory(self, Objekt):
        self.__inventory.append(Objekt)
        print(Objekt.Name + " wurde zu Ihrem Inventar hinzugefügt!")

    def deleteFromInventory(self, Gegenstand):
        print(Gegenstand.Name + " wurde aus Ihrem Inventar entfernt!")


Inventar = Inventory # Inventar des Spielers
Schwert = Gegenstand("Superschwinger",1,200) # Erzeuge Schwert "Superschwinger"

Inventar.addToInventory(Schwert)
