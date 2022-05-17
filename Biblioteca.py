
from biblio.Libro import Libro
from biblio.Piano import Piano
from biblio.Ripiano import Ripiano
from biblio.Scaffale import Scaffale



class Biblioteca() :
    def __init__(self):
        piano1 = Piano()
        piano2 = Piano()
        piano3 = Piano()
        self.piani = [piano1, piano2 , piano3]


    def addLibro(self, piano , scaffale, ripiano, titolo , autore ):
        add_libro = Libro(titolo, autore, ripiano)
        scaffale = str(scaffale)
        ripiano = int(ripiano)

        self.piani[piano - 1].addLibro(scaffale, ripiano, add_libro)

    def contiene(self, piano, scaffale  , ripiano ):
        _piano = self.piani[piano-1]
        _scaffale = _piano.lista_scaffali[scaffale]
        _ripiano = _scaffale.lista_ripiani[ripiano]

        for piano in self.piani:
            for scaffale in piano.lista_scaffali:
                for ripiano in piano.lista_scaffali[scaffale].lista_ripiani:
                    for libro in ripiano.lista_libri:
                        if len(libro.titolo) > 0 :
                             print("C e libro")

                        else :
                             print( "non ce")

    def getLibri(self, piano , scaffale):
        _piano = self.piani[piano -1]
        _scaffale = _piano.lista_scaffali[scaffale]
        for x in _scaffale.lista_ripiani:
            if len(x.lista_libri) > 0:
                for y in x.lista_libri:
                    print(y.titolo, y.autore)

    def cercaLibro(self, autore , titolo ):
        for piano in self.piani:
            for scaffale in piano.lista_scaffali:
                for ripiano in piano.lista_scaffali[scaffale].lista_ripiani:
                    for libro in ripiano.lista_libri:
                        if libro.titolo == titolo and libro.autore == autore:
                            return (libro.titolo, libro.autore)









