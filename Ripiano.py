
class Ripiano :
    def __init__(self, scaffale) :
        self.lista_libri = []
        self.scaffale = scaffale

    def addLibro(self,  libro):
        libro.ripiano = self
        self.lista_libri.append(libro)

    def getLibri(self, scaffale, piano):
        for libri in piano.lista_scaffali[piano - 1] and scaffale in scaffale.lista_ripiani:
            print(str(libri))



