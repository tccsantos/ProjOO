from abc import ABC, abstractmethod
from LibraryMediator import Mediator
from User import User


class Book(ABC):

    def __init__(self, nome) -> None:
        self.nome = nome
        self.mediator = None

    def __repr__(self) -> str:
        return  self.__nome + ', ' + self.__autor if self.__autor else self.__nome 

    @abstractmethod
    def isComposite(self):
        pass

    @abstractmethod
    def pegarLivros(self):
        pass

    def getNome(self) -> str:
        return self.nome
    
    def setMediator(self, mediator: Mediator) -> None:
        self.mediator = mediator


class ColecaoLivro(Book):
    
    def __init__(self, nome: str, livros: set[Book]) -> None:
        super().__init__(nome)
        self.livros = livros

    def addElement(self, materia: Book):
        self.materias.add(materia)

    def removeElement(self, materia: Book):
        self.materias.discard(materia)

    def isComposite(self):
        return True

    def pegarLivros(self):
        allBooks: set[Book]
        for materia in self.materias:
            allBooks.add(*materia.pegarLivros())
        return allBooks
       

class LivroUnico(Book):
    
    def __init__(self, nome: str, autor: set[str], quantidade: int) -> None:
        super().__init__(nome)
        self.__autor = autor
        self.__quantidade = quantidade
        self.__avaliabe = [True] * quantidade
        self.__users = [None] * quantidade

    def isComposite(self):
        return False 

    def pegarLivros(self):
        return self
    
    def emprestimo(self, user: User) -> None:
        ...
    
    def getAvaliabe(self) -> list[bool]:
        return self.__avaliabe
