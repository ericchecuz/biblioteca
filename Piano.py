
from biblio.Scaffale import Scaffale


class Piano:
    def __init__(self):
        self.lista_scaffali = {}
        for val in range(1,31) :
            scaffale = Scaffale(self)
            self.lista_scaffali["SC" + str(val)] = scaffale


    def addLibro(self, scaffale, ripiano, libro):
        self.lista_scaffali[scaffale].addLibro(ripiano,libro)

