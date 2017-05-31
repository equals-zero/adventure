
class Inventory(object):
    """
    Inventar - Kann Inventar von Spieler oder Objekt
    Initialisierung:
    InventarName = Inventory((int)Inventargroesse)
    """

    def __init__(self, maxsize):
        super(Inventory, self).__init__()
        self.__inventory = []
        self.MaxSpace = maxsize

    def showAll(self):
        if len(self.__inventory) == 0:
            print("Das Inventar ist leer.")
        else:
            print("Im Inventar befindet sich:")
            for Gegenstand in self.__inventory:
                print(Gegenstand.Name)

    def addToInventory(self, DasObjekt):
        self.__inventory.append(DasObjekt)
        print(DasObjekt.Name + " wurde zu Ihrem Inventar hinzugefügt!")

    def deleteFromInventory(self, Gegenstand):
        for Inventareintrag in self.__inventory:
            if Gegenstand == Inventareintrag:
                self.__inventory.remove(Inventareintrag)
                print(Gegenstand.Name + " wurde aus Ihrem Inventar entfernt!")


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

    def __init__(self, nameDesMoebelstuecks, beschreibungDesMoebelstuecks, inventarGroesse, verschlossen, schluessel):
        super(Moebelstueck, self).__init__()
        self.Name = nameDesMoebelstuecks
        self.Beschreibung = beschreibungDesMoebelstuecks
        self.__Inventargroesse = inventarGroesse
        self.Verschlossen = verschlossen
        self.__Schluessel = schluessel
        self.__Inhalt = []

    def ueberschreibeInventar(self, NeuesInventar):
        """ NeuesInventar = Array! """
        self.__Inhalt = NeuesInventar
        pass

    def gebeInhaltAus (self):
        if self.Verschlossen == True:
            print(self.Name + " ist verschlossen.")
        else:
            if len(self.__Inhalt) == 0:
                print(self.__Name + " ist leer.")
            else:
                for GegenstandAusInventar in self.__Inhalt:
                    print(GegenstandAusInventar.Name)

#