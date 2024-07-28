from abc import ABC, abstractmethod

from typing import Self
import time

#Na interface Mediator pode-se observar o princípio da Segregação de Interfaces 
class Mediator(ABC):
    
    @abstractmethod
    def notify(self, book) -> None:
        pass


#A classe Book foi feita baseando-se no Design pattern Composite
class Book(ABC):

    def __init__(self, name, _id) -> None:
        self.__name: str = name
        self.__id: int = _id
        self.__mediator = None

    def __repr__(self) -> str:
        return  f"nome: {self.__name}\nAutor: {self.getAuthor()}\nid: {str(self.getId())}"

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
    def getCompositions(self) -> set[Self]:
        pass

    @abstractmethod
    def getAuthor(self) -> str:
        pass

    def getName(self) -> str:
        return self.__name
        
    def setMediator(self, mediator: Mediator) -> None:
        self.__mediator = mediator
    
    def getMediator(self) -> Mediator:
        return self.__mediator
    
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
        self.__ageOfBirth: str = ageOfBirth 
        self.__reservation: set[int] = set() if reservation == None else reservation
        self.__loan: list[int] = list() if loan == None else loan
        self.connection: ExternalCatalogAdapter = connection #Aqui nós temos um exemplo de Inversão de Dependências
        self.__history: list[Book] = list()
    
    def __repr__(self) -> str:
        if self.isType() == "Teacher": return f'Professor {self.__name}'
        else: return f'Aluno {self.__name}'

    @abstractmethod
    def isType(self) -> str:
        pass
    
    @abstractmethod
    def presentation(self, books: set[Book]) -> None:
        pass

    def getName(self) -> str:
        return self.__name
    
    def getCpf(self) -> str:
        return self.__cpf
    
    def getAge(self) -> int:
        return int(time.gmtime().tm_year) - int(self.__ageOfBirth[-4:])

    def getReservation(self) -> set[int]:
        return self.__reservation
    
    def waitBook(self, book: Book) -> None:
        self.__reservation.add(book)

    def removeBook(self, idBook: int) -> None:
        if idBook in self.__reservation:
            self.__reservation.remove(idBook)
            self.connection.removeReserve(self,idBook)
    
    def update(self, book: Book) -> None:
        if book.getId() in self.__reservation:
            print(f'O aluno {self.__name} foi notificado da disponibilidade do livro {book.getName()}')
    
    def getLoan(self) -> list[int]:
        return self.__loan
    
    def loan(self, idBook: int) -> None:
        self.__loan.append(idBook)
        self.connection.addLoan(self, idBook)

    def returnal(self, book: Book) -> None:
        self.__loan.remove(book.getId())
        self.connection.returnLoan(self, book.getId())
        self.__history.append(book)
    
    def reserveBook(self, idBook: int) -> None:
        if not idBook in self.__reservation:
            self.__reservation.add(idBook)
            self.connection.addReserve(self,idBook)

    def getHistory(self) -> list[int]:
        return self.__history


#A classe ConfigurationManager segue o princípio da responsabilidade única
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


#Na interface Handler pode-se observar o princípio da Segregação de Interfaces 
class Handler(ABC):

    def __init__(self, suc: Self|None = None, manager: ConfigurationManager = None) -> None:
        self.successor: Handler|None = suc
        self.manager: ConfigurationManager = manager

    @abstractmethod
    def eligible(self, book: Book, user: User):
        pass


#Baseando-se no Design Pattern Adapter, essa classe seria o Alvo, aqui nós implementamos o Object Adapter
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
