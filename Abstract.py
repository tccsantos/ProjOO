from abc import ABC, abstractmethod

from typing import Self
import time


class Mediator(ABC):
    
    @abstractmethod
    def notify(self, book) -> None:
        pass


class Book(ABC):

    def __init__(self, name, _id) -> None:
        self.__name: str = name
        self.__id: int = _id
        self.__mediator = None

    def __repr__(self) -> str:
        return  self.__name + ', ' + self.getAuthor()

    def __eq__(self, __value: Self) -> bool:
        return  self.getId() == __value.getId()
    
    def __hash__(self) -> int:
        return self.getId()

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
        
    def setMediator(self, mediator: Mediator) -> None:
        self.__mediator = mediator
    
    def getId(self)-> int:
        return self.__id
    
    def getQuantity(self) -> list[bool]:
        pass

    def notifyReturn(self):
        pass

    def addAvaliable(self):
        pass

    def removeAvaliable(self):
        pass

    def getAvaliabe(self) -> list[bool]:
        pass

    def addElement(self):
        pass

    def removeElement(self):
        pass


class User(ABC):

    def __init__(self,name: str, cpf: str, ageOfBirth: str, connection, reservation: set[Book]|None = None, loan: list[Book]|None = None):
        self.__name: str = name
        self.__cpf: str = cpf
        self.__ageOfBirth: str = ageOfBirth #"08062004"
        self.__reservation: set[Book] = set() if reservation == None else reservation
        self.__loan: list[Book] = list() if loan == None else loan
        self.connection = connection
    
    def __repr__(self) -> str:
        return f'{self.__name}, {self.__cpf}, {self.__ageOfBirth}'

    @abstractmethod
    def isType(self) -> str:
        pass

    def getName(self) -> str:
        return self.__name
    
    def getCpf(self) -> str:
        return self.__cpf
    
    def getAge(self) -> int:
        return int(time.gmtime().tm_year) - int(self.__ageOfBirth[-4:])

    def getReservation(self) -> set[Book]:
        return self.__reservation
    
    def waitBook(self, book: Book) -> None:
        self.__reservation.add(book)

    def removeBook(self, book: Book) -> None:
        self.__reservation.discard(book)
    
    def update(self, book: Book) -> None:
        if book in self.__reservation:
            print(f'O aluno {self.__name} foi notificado da disponibilidade do livro {book.getName()}')
    
    def getLoan(self) -> list[Book]:
        return self.__loan
    
    def loan(self, book: Book) -> None:
        self.__loan.append(book)
        #self.connection.addLoan(self, book)

    def returnal(self, book: Book) -> None:
        self.__loan.remove(book)
        #self.connection.returnLoan(self, book)
    
    def reserveBook(self, book: Book) -> None:
        self.__reservation.add(book)


class ConfigurationManager(ABC):

    @abstractmethod
    def getLoanLimit(self, user: User):
        pass

    @abstractmethod
    def getMultipleLimit(self, user: User):
        pass

    @abstractmethod
    def setLoanLimit(self, userType: str, newLimit: int, newUserType: bool) -> None:
        pass

    @abstractmethod
    def setMultipleLimit(self, userType: str, newLimit: int, newUserType: bool) -> None:
        pass


class Handler(ABC):

    def __init__(self, suc: Self|None = None, manager: ConfigurationManager = None) -> None:
        self.successor: Handler|None = suc
        self.manager: ConfigurationManager = manager

    @abstractmethod
    def eligible(self, book: Book, user: User):
        pass


class ExternalCatalogAdapter(ABC):
    
    @abstractmethod
    def addLoan(self, user: User, book: Book) -> None:
        pass

    @abstractmethod
    def returnLoan(self, user: User, book: Book) -> None:
        pass

    @abstractmethod
    def initialize(self) -> tuple[set[User], set[Book]]:
        pass

    @abstractmethod
    def addReserve(self, user: User, book: Book) -> None:
        pass

    @abstractmethod
    def removeReserve(self, user: User, book: Book) -> None:
        pass
