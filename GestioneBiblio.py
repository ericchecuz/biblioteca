from biblio.Biblioteca import Biblioteca
from main import biblioteca


class GestioneBiblio:

    def start(self):

            x = True
            while x:
                comando = input("""
                 1: '"add": inserimento libro, seguito dai parametri autore, titolo, piano, scaffale e ripiano',
                 2: '"list": stampa contenuto scaffale, seguito dai parametri piano e scaffale',
                 3: '"libro": ricerca un libro e stampa la posizione: seguito dai parametri autore e titolo',
                 4: 'quit',""")

                if comando == "1":
                    piano = input("inserisci Piano: ")
                    scaffale = input("inserisci Scaffale: ")
                    ripiano = input("inserisci Ripiano: ")
                    titolo = input("inserisci the book Titolo")
                    autore = input("inserisci the book Authore")
                    biblioteca.addLibro(int(piano), int(scaffale), int(ripiano), titolo, autore)

                if comando == "2":
                    piano = input("inserisci Piano: ")
                    scaffale = input("inserisci Scaffale: ")
                    biblioteca.getLibri(int(piano), int(scaffale))

                if comando == "3":
                    titolo = input("inserisci il titolo del libro")
                    authore = input("inserisci l'autore del libro")
                    biblioteca.cerca(titolo, authore)

                if comando == "4":
                    return
                else:
                    print("devi in inserire uno di quest comandi 1, 2, 3, 4")
                    print("Riprova")
