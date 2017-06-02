class Steuerung(object):
    """ 
    Ueber diese Klasse wird die Steuerung uebernommen.
    """
    def __init__(self, Karte, Startraum):
        super(Steuerung, self).__init__()
        self.__Weltkarte = Karte
        self.__Startraum = Startraum

    def BeschreibeRaum (self, Id):
        print(
            self.__Weltkarte[Id].Name + " - " +
            self.__Weltkarte[Id].Beschreibung +
            self.ListeInhaltDesRaums(Id)
        )

    def ListeInhaltDesRaums (self, Id):
        """ Gibt alle im Raum befindlichen Moebel aus. """
        if self.__Weltkarte[Id].Rauminhalt == False:
            print("Der Raum ist leer.")
        else:
            print("Der Raum enthaelt ausserdem:")
            for Moebelstueck in self.__Weltkarte[Id].Rauminhalt:
                print(Moebelstueck.Name)

    def WelcheAusgaengeGibtEs (self):
        print()

    def ErhalteRaumNamenDurchId (self, Id):
        return self.__Weltkarte[Id].Name
