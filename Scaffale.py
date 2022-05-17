
from biblio.Ripiano import Ripiano
class Scaffale:
    def __init__(self, piano):
        self.lista_ripiani = []
        self.piano = piano
        for val in range(1,7):
            ripiano = Ripiano(self)
            self.lista_ripiani.append(ripiano)



    def addLibro(self,  ripiano, libro):
        self.lista_ripiani[ripiano - 1].addLibro(libro)






