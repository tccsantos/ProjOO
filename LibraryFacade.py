from abc import ABC, abstractmethod

from User import User
from Book import Book

class LibraryMediator(ABC):
    @abstractmethod
    def buscaLivros(self):
        pass
    @abstractmethod
    def emprestaLivro(self):
        pass
    @abstractmethod
    def devolverLivros(self):
        pass

class LibraryFacade(LibraryMediator):

    __instance = None
    
    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instances

    def __init__(self) -> None:
        self.libraryFacade: LibraryFacade = None
        self.books: set[Book] = []
        self.users: set[User] = []

    def buscaLivros(self):
        ...

    def emprestaLivros(self):
        ...

    def devolveLivros(self):
        ...

