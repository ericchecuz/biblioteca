
from biblio.Piano import Piano


class Libro :
    def __init__(self, autore, titolo , ripiano ) :

        self.autore = autore
        self.titolo = titolo
        self.ripiano = ripiano

    def toString(self):
        stringalibro = str(self.autore,", ",self.titolo)
        return stringalibro


    def getRipiano(self):

        return print("il libro e' al ripiano", self.ripiano)

    def getPiano(self):

        return  print("il libro e al piano", self.ripiano.scaffale.piano)

    def getScaffale(self):

        return print("il libro e allo scaffale", self.ripiano.scaffale)