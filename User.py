from abc import ABC, abstractmethod
from Book import Book
#from Adapter import ExternalCatalogAdapter
import time


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
        self.connection.addLoan(self, book)

    def returnal(self, book: Book) -> None:
        self.__loan.remove(book)
        self.connection.returnLoan(self, book)
    
    def reserveBook(self, book: Book) -> None:
        self.__reservation.add(book)



class StudentUserType(User):
    def __init__(self, name: str, cpf: str, ageOfBirth: str, connection, reservation: set[Book] | None = None, loan: list[Book] | None = None):
        super().__init__(name, cpf, ageOfBirth, connection, reservation, loan)
    
    def isType(self) -> str:
        return "Student"


class TeacherUserType(User):
    def __init__(self, name: str, cpf: str, ageOfBirth: str, connection, reservation: set[Book] | None = None, loan: list[Book] | None = None):
        super().__init__(name, cpf, ageOfBirth, connection, reservation, loan)
    
    def isType(self) -> str:
        return "Teacher"