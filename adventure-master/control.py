class Steuerung(object):
    """ 
    Ueber diese Klasse wird die Steuerung uebernommen.
    """

    def __init__(self, Karte, Startraum):
        super(Steuerung, self).__init__()
        self.__Weltkarte = Karte
        self.__Startraum = Startraum

    def BeschreibeRaum(self, Id):
        print(
            self.__Weltkarte[Id].Name + " - " +
            self.__Weltkarte[Id].Beschreibung
        )
        self.ListeInhaltDesRaums(Id)

    def ListeInhaltDesRaums(self, Id):
        """ Gibt alle im Raum befindlichen Moebel aus. """
        if not self.__Weltkarte[Id].Rauminhalt:
            print("Der Raum ist leer.")
        else:
            print("Der Raum enthaelt ausserdem:")
            for Moebelstueck in self.__Weltkarte[Id].Rauminhalt:
                print(Moebelstueck.Name)

    # TODO: Liste die bekannten Ausgaenge
    def WelcheAusgaengeGibtEs(self):
        pass

    def ErhalteRaumNamenDurchId(self, Id):
        return self.__Weltkarte[Id].Name

    # TODO: Speichert Savegame-Datei
    def SpeicherSpeicherpunktInDatei(self, Dateipfad, Inhalt):
        pass

    # TODO: Laedt Savegame-Datei in Array
    def LadeSpeicherpunktVonDatei(self, Dateipfad):
        pass
