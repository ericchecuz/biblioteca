from biblio.Biblioteca import Biblioteca
from biblio.Libro import Libro
from biblio.Piano import Piano
from biblio.Ripiano import Ripiano
from biblio.Scaffale import Scaffale


biblioteca = Biblioteca()



biblioteca.addLibro( 1,"SC1",2,"ciao", "eric")
biblioteca.contiene(1,"SC1",2)
biblioteca.getLibri(1,"SC1")

libro = biblioteca.piani[0].lista_scaffali["SC1"].lista_ripiani[1].lista_libri[0]
libro.getRipiano()
libro.getPiano()
libro.getScaffale()

libro = biblioteca.cercaLibro("ciao","eric")
print(str(libro))





