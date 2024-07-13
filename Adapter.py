from Abstract import ExternalCatalogAdapter, User, Book
from Book import SingleBook, CompositionBook
from User import TeacherUserType, StudentUserType
import pandas as pd
import csv



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
                sup = TeacherUserType(user[1], user[2], user[3], self,reserve, loan)
            elif user[6] == "Student":
                sup = StudentUserType(user[1], user[2], user[3], self, reserve, loan)
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
            
            #books.add(sup)
            single.add(sup)
        
        for book in catalog:
            ids = map(int, book[5].split(','))
            comp = set()
            for num in ids:
                for unique in single:
                    if num == unique.getId():
                        comp.add(unique)
            
            sup = CompositionBook(book[2], int(book[0]), comp)
            books.add(sup)
        


        return users, books
    
    def addLoan(self, user: User, book: Book) -> None:
        with open("./Banco/Users.csv", "wr", encoding="utf8") as arquivo:
            aba = csv.reader(arquivo, delimiter=";")
            
            for line in aba:
                if(line.includes(user.getName())):
                    new_line = []
                    return None
        return KeyError
    
    def returnLoan(self, user: User, book: Book) -> None:
        return None

    def addReserve(self, user: User, book: Book) -> None:
        return super().addReserve(user, book)
    
    def removeReserve(self, user: User, book: Book) -> None:
        return super().removeReserve(user, book)
