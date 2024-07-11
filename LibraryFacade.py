from abc import ABC, abstractmethod

from User import User
from Book import Book

class LibraryFacade():

    __instance = None
    

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance


    def __init__(self, users: set[User], books: set[Book]) -> None:
        self.libraryFacade: LibraryFacade = None
        self.__books: set[Book] = books
        self.__users: set[User] = users

    
    def __select():
        ...


    def buscaLivros(self, nomeLivro):
        allBooks: set[Book] = self.books.pegarLivros() #Errado, arrumar!!!!
        specificBooks = self.__select(allBooks, nomeLivro)
        if (len(specificBooks)<1): print("Nenhum livro foi encontrado\n")
        else:
            for i , book in enumerate(specificBooks, start= 1):
                print(f'{i}- {book}\n')


    def emprestaLivros(self):
        ...
        #Caso o livro não esteja disponível, dar a opção do usuário reservar!!!
    

    def __Reserva(self, book: Book, user: User) -> None:
        user.reservarLivro(book)
        print("Reserva feita\n")


    def devolveLivros(self):
        ...
