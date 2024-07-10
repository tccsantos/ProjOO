#Thiago Cortez Cursino dos Santos  RA 163997

from abc import ABC, abstractmethod



class Publicacao(ABC):

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def getArtigos(self):
        pass

    @abstractmethod
    def getAll(self):
        pass


class Jornal(Publicacao):


    def __init__(self, nome: str, artigos: set[Publicacao]) -> None:
        self.nome = nome
        self.artigos = artigos

    def __str__(self):
        return self.nome

    def getArtigos(self):
        artigos = 0
        for artigo in self.artigos:
            artigos += artigo.getArtigos()
        return artigos

    def getAll(self):
        artigos = 1
        for artigo in self.artigos:
            artigos += artigo.getAll()
        return artigos


class Caderno(Publicacao):

    def __init__(self, nome: str, artigos: set[Publicacao]) -> None:
        self.nome = nome
        self.artigos = artigos

    def __str__(self):
        return self.nome

    def getArtigos(self):
        artigos = 0
        for artigo in self.artigos:
            artigos += artigo.getArtigos()
        return artigos

    def getAll(self):
        artigos = 1
        for artigo in self.artigos:
            artigos += artigo.getAll()
        return artigos


class Revista(Publicacao):

    def __init__(self, nome: str, artigos: set[Publicacao]) -> None:
        self.nome = nome
        self.artigos = artigos

    def __str__(self):
        return self.nome

    def getArtigos(self):
        artigos = 0
        for artigo in self.artigos:
            artigos += artigo.getArtigos()
        return artigos

    def getAll(self):
        artigos = 1
        for artigo in self.artigos:
            artigos += artigo.getAll()
        return artigos


class Artigo(Publicacao):

    def __init__(self, nome: str, autor: set[str]) -> None:
        self.nome = nome
        self.autor = autor

    def __str__(self):
        return f'Artigo: {self.nome}\nAutores: {", ".join(self.autor)}\n'
        

    def getArtigos(self):
        return 1

    def getAll(self):
        return 1


def teste():
    # Criando alguns artigos
    artigo1 = Artigo("Artigo 1", {"Autor 1", "Autor 2"})
    artigo2 = Artigo("Artigo 2", {"Autor 3"})
    artigo3 = Artigo("Artigo 3", {"Autor 1", "Autor 4"})
    artigo4 = Artigo("Artigo 4", {"Autor 2", "Autor 3"})
    artigo5 = Artigo("Artigo 5", {"Autor 5"})
    artigo6 = Artigo("Artigo 6", {"Autor 6", "Autor 7", "Autor 8"})
    artigo7 = Artigo("Artigo 7", {"Autor 2", "Autor 8"})
    artigo8 = Artigo("Artigo 8", {"Autor 5", "Autor 9"})
    artigo9 = Artigo("Artigo 9", {"Autor 2", "Autor 6", "Autor 9"})
    artigo10 = Artigo("Artigo 10", {"Autor 1", "Autor 8"})

    # Criando jornal, caderno e revista com os artigos
    revista1 = Revista("Revista Z", {artigo1, artigo2, artigo3})
    revista2 = Revista("Revista W", {artigo4, artigo5, artigo6})
    caderno = Caderno("Caderno Y", {artigo7, artigo8, revista1, revista2})
    jornal = Jornal("Jornal X", {artigo9, artigo10, caderno})

    print(revista1)
    print(revista2)
    print(caderno)
    print(jornal, end='\n\n')

    print(artigo1)
    print(artigo2, end='\n\n')

    print(jornal.getArtigos())
    print(jornal.getAll())



if __name__ == '__main__':
    teste()
