from abc import ABC, abstractmethod
from Book import Book
from Adapter import ExternalCatalogAdapter
import time


class User(ABC):

    def __init__(self,nome: str, cpf: str, nascimento: str, conexao: ExternalCatalogAdapter, reserva: set[Book]|None = None, emprestimo: list[Book]|None = None):
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__nascimento: str = nascimento #"08062004"
        self.__reserva: set[Book] = set() if reserva == None else reserva
        self.__emprestimo: list[Book] = list() if emprestimo == None else emprestimo
        self.conexao: ExternalCatalogAdapter = conexao

    @abstractmethod
    def isType(self) -> str:
        pass

    def solicitarNome(self) -> str:
        return self.__nome
    
    def solicitarCpf(self) -> str:
        return self.__cpf
    
    def solicitarIdade(self) -> int:
        return int(time.gmtime().tm_year) - int(self.__nascimento[-4:])

    def solicitarReserva(self) -> set[Book]:
        return self.__reserva
    
    def esperarLivro(self, book: Book) -> None:
        self.__reserva.add(book)

    def removerLivro(self, book: Book) -> None:
        self.__reserva.discard(book)
    
    def update(self, book: Book) -> None:
        if book in self.__reserva:
            print(f'O aluno {self.__nome} foi notificado da disponibilidade do livro {book.getNome()}')
    
    def solicitarEmprestimo(self) -> list[Book]:
        return self.__emprestimo
    
    def emprestimo(self, book: Book) -> None:
        self.__emprestimo.append(book)
        self.conexao.adicionaEmprestimo(self, book)

    def devolucao(self, book: Book) -> None:
        self.__emprestimo.remove(book)
        self.conexao.devolveEmprestimo(self, book)
    
    def reservarLivro(self, book: Book) -> None:
        self.__reserva.add(book)



class StudentUserType(User):
    def __init__(self, nome: str, cpf: str, nascimento: str, conexao: ExternalCatalogAdapter, reserva: set[Book] | None = None, emprestimo: list[Book] | None = None):
        super().__init__(nome, cpf, nascimento, conexao, reserva, emprestimo)
    
    def isType(self) -> str:
        return "Student"


class TeacherUserType(User):
    def __init__(self, nome: str, cpf: str, nascimento: str, conexao: ExternalCatalogAdapter, reserva: set[Book] | None = None, emprestimo: list[Book] | None = None):
        super().__init__(nome, cpf, nascimento, conexao, reserva, emprestimo)
    
    def isType(self) -> str:
        return "Teacher"