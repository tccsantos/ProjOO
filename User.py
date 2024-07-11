from abc import ABC, abstractmethod
from Book import Book
import time


class User(ABC):

    def __init__(self,nome: str, cpf: str, nascimento: str):
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__nascimento: str = nascimento #"08062004"
        self.__reserva: set[Book] = set()

    def solicitarNome(self) -> str:
        return self.__nome
    
    def solicitarCpf(self) -> str:
        return self.__cpf
    
    def solicitarIdade(self) -> int:
        return int(time.gmtime().tm_year) - int(self.__nascimento[-4:])
    
    def esperarLivro(self, book: Book) -> None:
        self.__reserva.add(book)

    def removerLivro(self, book: Book) -> None:
        self.__reserva.discard(book)
    
    def update(self, book: Book) -> None:
        if book in self.__reserva:
            print(f'O aluno {self.__nome} foi notificado da disponibilidade do livro {book.getNome()}')



class StudentUserType(User):
    def __init__(self, nome, cpf, nascimento):
        super().__init__(nome, cpf, nascimento)


class TeacherUserType(User):
    def __init__(self, nome, cpf, nascimento):
        super().__init__(nome, cpf, nascimento)