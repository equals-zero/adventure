
class Inventory(object):
    """
    Inventar - Kann Inventar von Spieler oder Objekt
    Initialisierung:
    InventarName = Inventory((int)Inventargroesse)
    """

    def __init__(self, maxsize):
        super(Inventory, self).__init__()
        self.Inventory = []
        self.MaxSpace = maxsize

    def showAllContents(self):
        if len(self.Inventory) == 0:
            print("Das Inventar ist leer.")
        else:
            print("Im Inventar befindet sich:")
            for Gegenstand in self.Inventory:
                print(Gegenstand.Name)

    def addToInventory(self, DasObjekt):
        if len(self.Inventory) >= self.MaxSpace:
            print(DasObjekt.Name + " konnte nicht hinzugefügt werden. "
                                   "Inventar voll ("+str(len(self.Inventory))+"/"+str(self.MaxSpace)+")!")
        self.Inventory.append(DasObjekt)
        print(DasObjekt.Name + " wurde zu Ihrem Inventar hinzugefügt!")

    def deleteFromInventory(self, Gegenstand):
        for Inventareintrag in self.Inventory:
            if Gegenstand == Inventareintrag:
                self.Inventory.remove(Inventareintrag)
                print(Gegenstand.Name + " wurde aus Ihrem Inventar entfernt!")

    # TODO: Liest die uebergebene Variable als Inventar ein
    def readInventoryFromSave (self, Savegame):
        pass

class Gegenstand(object):
    """ 
    Initialisiert einen Gegenstand - Bitte nicht fuer Moebel nutzen!
    JEDER GEGENSTAND DARF NUR EINMAL INITIALISIERT WERDEN!
    
    Initialisierung:
    derGegenstand = Gegenstand((str)"Name des Gegenstands",(int)TypDesGegenstands,(int)WertDesGegestands)
    
    Typ = Schwert, Schild, Ruestung, was auch immer ABER(!) ueber die ID
    Wert = Abhaengig von Typ, z.B. Verteidigungspunkte, Angriffspunkte... was auch immer
    """

    def __init__(self, nameDesGegenstands, beschreibungDesGegenstands, typDesGegenstands, wertDesGegenstands):
        super(Gegenstand, self).__init__()
        self.Name = nameDesGegenstands
        self.Beschreibung = beschreibungDesGegenstands
        self.Typ = typDesGegenstands
        self.Wert = wertDesGegenstands


class Moebelstueck(object):
    """ 
    Initialisiert ein Moebelstueck, z.B. eine Truhe oder eine Schachtel
    JEDES MOEBELSTUECK DARF NUR EINMAL INITIALISIERT WERDEN!
    """

    def __init__(self, nameDesMoebelstuecks, beschreibungDesMoebelstuecks,
                 inventarGroesse, inventarInhalt, verschlossen, schluessel):
        super(Moebelstueck, self).__init__()
        self.Name = nameDesMoebelstuecks
        self.Beschreibung = beschreibungDesMoebelstuecks
        self.__Inventargroesse = inventarGroesse
        self.Verschlossen = verschlossen
        self.__Schluessel = schluessel
        self.__Inhalt = inventarInhalt

    def overwriteInventory(self, NeuesInventar):
        """ NeuesInventar = Array! """
        self.__Inhalt = NeuesInventar
        pass

    def showAllContents (self):
        if self.Verschlossen:
            print(self.Name + " ist verschlossen.")
        else:
            if len(self.__Inhalt) == 0:
                print(self.Name + " ist leer.")
            else:
                print(self.Name + " enthält:")
                for GegenstandAusInventar in self.__Inhalt:
                    print(GegenstandAusInventar.Name)


class Raum (object):
    """
    Raeume werden untereinander verbunden und enthalten Moebelstuecke und Gegenstaende.
    Der Spieler bewegt sich durch die einzelnen Raeume.
    
    ausgaengeDesRaumes = Array aus Int. Werten! Jeder Eintrag muss auf Key des GameMap-Arrays zeigen!
    """

    def __init__(self, idDesRaumes, beschreibungDesRaumes, ausgaengeDesRaumes,
                 inhaltDesRaumes, verschlossen, schluessel):
        super(Raum, self).__init__()
        self.Name = idDesRaumes
        self.Beschreibung = beschreibungDesRaumes
        self.Rauminhalt = inhaltDesRaumes
        self.Verschlossen = verschlossen
        self.Ausgaenge = ausgaengeDesRaumes
        self.__Schluessel = schluessel


#