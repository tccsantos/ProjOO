from abc import ABC, abstractmethod
#from LibraryMediator import Mediator
#from User import User

from typing import Self


class Book(ABC):

    def __init__(self, name, _id) -> None:
        self.__name: str = name
        self.__id: int = _id
        self.__mediator = None

    def __repr__(self) -> str:
        return  self.__name + ', ' + self.getAuthor()

    def __eq__(self, __value: Self) -> bool:
        return  self.__name == __value.__name
    
    def __hash__(self) -> int:
        return hash(self.__name)

    @abstractmethod
    def isComposite(self) -> bool:
        pass

    @abstractmethod
    def getBooks(self) -> Self|set[Self]:
        pass

    @abstractmethod
    def getAuthor(self) -> str:
        pass

    def getName(self) -> str:
        return self.__name
        
    def setMediator(self, mediator) -> None:
        self.__mediator = mediator
    
    def getId(self)-> int:
        return self.__id


class CompositionBook(Book):
    
    def __init__(self, name: str, _id: int, books: set[Book]) -> None:
        super().__init__(name, _id)
        self.books = books

    def addElement(self, books: Book):
        self.books.add(books)

    def removeElement(self, books: Book):
        self.books.discard(books)

    def isComposite(self) -> bool:
        return True

    def getBooks(self):
        allBooks: set[Book] = set()
        for book in self.books:
            childs = book.getBooks()
            allBooks.add(*childs) if type(childs) == set else allBooks.add(childs)
        return allBooks
       
    def getAuthor(self) -> str:
        return ''


class SingleBook(Book):
    
    def __init__(self, name: str, _id: int, author: set[str], quantity: int) -> None:
        super().__init__(name, _id)
        self.__author = author
        self.__quantity = quantity
        self.__avaliabe = [True] * quantity
        self.__users = [None] * quantity

    def isComposite(self) -> bool:
        return False 

    def getBooks(self):
        return self
    
    def getAvaliabe(self) -> list[bool]:
        return self.__avaliabe
    
    def addAvaliable(self):
        try:
            self.__avaliabe[self.__avaliabe.index(False)] = True
        except:
            print("Erro! Você está tentando deixar um livro disponível, mas todos já estão disponíveis")

    def removeAvaliable(self):
        try:
            self.__avaliabe[self.__avaliabe.index(True)] = False
        except:
            print("Erro! Você está tentando pegar um livro, mas todos já estão emprestados")

    
    def getQuantity(self) -> list[bool]:
        return self.__quantity
    
    def notifyReturn(self):
        self.__mediator.notify(self)
    
    def getAuthor(self) -> str:
        return self.__author
