#from abc import ABC, abstractmethod
from csv import reader

from User import StudentUserType, TeacherUserType
from Book import Book



class ConfigurationManager():

    def __init__(self) -> None:
        pass


    def read(self):
        with open("./Banco/Users.csv", "r", encoding="utf8") as arquivo:
            aba = reader(arquivo)
            next(aba, None)
            users = list[aba]
        
        with open("./Banco/Books.csv", "r", encoding="utf8") as arquivo:
            aba = reader(arquivo)
            next(aba, None)
            books = list[aba]
        
        return users, books


    def classify(self):

        u, b = self.read()

        users = set()
        books = set()

        for user in u:
            if user[3] == "Teacher":
                sup = TeacherUserType(user[0], user[1], user[2])
            elif user[3] == "Student":
                sup = StudentUserType(user[0], user[1], user[2])
            else:
                raise KeyError
            users.add(sup)

        for book in b:
            sup = Book(book)
            books.add(sup)

        return users, books
        
