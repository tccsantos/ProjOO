from abc import ABC, abstractmethod


class Book(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def pegarLivros(self):
        pass

class ColecaoArea(Book):
    def __init__(self, nome: str, materias: set[Book]) -> None:
        self.nome = nome
        self.materias = materias


class ColecaoMateria(Book):
    def __init__(self, nome: str, livros: set[Book]) -> None:
        self.nome = nome
        self.livros = livros


class LivroUnico(Book):
    def __init__(self, nome: str, autor: set[str]) -> None:
        self.nome = nome
        self.autor = autor

