from abc import ABC, abstractmethod
from User import User, TeacherUserType, StudentUserType
from Book import Book, LivroUnico, ColecaoLivro

import csv


class ExternalCatalogAdapter(ABC):
    
    @abstractmethod
    def adicionaEmprestimo(self, user: User, book: Book) -> None:
        pass

    @abstractmethod
    def devolveEmprestimo(self, user: User, book: Book) -> None:
        pass

    @abstractmethod
    def inicializa(self) -> tuple[set[User], set[Book]]:
        pass


class csvReader(ExternalCatalogAdapter):
    
    def __init__(self, bookPath: str, userPath: str) -> None:
        self.bookPath: str = bookPath
        self.userPath: str = userPath

    def inicializa(self) -> tuple[set[User], set[Book]]:
        with open("./Banco/Users.csv", "r", encoding="utf8") as arquivo:
            aba = csv.reader(arquivo)
            next(aba, None)
            rawUsers = list[aba]
        
        with open("./Banco/Books.csv", "r", encoding="utf8") as arquivo:
            aba = csv.reader(arquivo)
            next(aba, None)
            rawBooks = list[aba]

        users = set()
        books = set()

        #Incompleto!!!!

        # for user in rawUsers:
        #     if user[3] == "Teacher":
        #         sup = TeacherUserType(user[0], user[1], user[2])
        #     elif user[3] == "Student":
        #         sup = StudentUserType(user[0], user[1], user[2])
        #     else:
        #         raise KeyError
        #     users.add(sup)

        # for book in rawBooks:
        #     sup = Book(book)
        #     books.add(sup)

        return users, books
    