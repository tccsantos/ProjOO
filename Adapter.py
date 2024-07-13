from abc import ABC, abstractmethod
from User import User, TeacherUserType, StudentUserType
from Book import Book, SingleBook, CompositionBook

import csv


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


class csvReader(ExternalCatalogAdapter):
    
    def __init__(self, bookPath: str, userPath: str) -> None:
        self.bookPath: str = bookPath
        self.userPath: str = userPath

    def initialize(self) -> tuple[set[User], set[Book]]:
        with open("./Banco/Users.csv", "r", encoding="utf8") as arquivo:
            aba = csv.reader(arquivo, delimiter=";")
            next(aba, None)
            rawUsers = list(aba)
        
        with open("./Banco/Books.csv", "r", encoding="utf8") as arquivo:
            aba = csv.reader(arquivo, delimiter=";")
            next(aba, None)
            rawBooks = list(aba)


        users = set()
        books = set()


        for user in rawUsers:
            reserve = None if user[4] == "None" else set(user[4].split(","))
            loan = None if user[5] == "None" else user[5].split(",")
            
            if user[6] == "Teacher":
                sup = TeacherUserType(user[1], user[2], user[3], reserve, loan)
            elif user[6] == "Student":
                sup = StudentUserType(user[1], user[2], user[3], reserve, loan)
            else:
                raise KeyError
            
            users.add(sup)
            catalog = list()
            single: set[Book] = set()

        for book in rawBooks:

            if book[1] == "True":
                catalog.append(book)
                #sup = CompositionBook(book[2], int(book[0]), set(book[5].split()))
            elif book[1] == "False":
                sup = SingleBook(book[2], int(book[0]), book[4],int(book[3]))
            else:
                raise KeyError
            
            books.add(sup)
            single.add(sup)
        
        for book in catalog:
            ids = map(int, book[5].split(','))
            comp = set()
            for num in ids:
                for unique in single:
                    if num == unique.getId():
                        comp.add(unique)
            
            sup = CompositionBook(book[2], book[0], comp)
            books.add(sup)
        


        return users, books
    
    def addLoan(self, user: User, book: Book) -> None:
        return super().addLoan(user, book)
    
    def returnLoan(self, user: User, book: Book) -> None:
        return super().returnLoan(user, book)

