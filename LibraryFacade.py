from Abstract import User, Book, Handler

class LibraryFacade:

    __instance = None
    

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, users: set[User], books: set[Book], bookHandler: Handler) -> None:
        self.libraryFacade: LibraryFacade = None
        self.__books: set[Book] = books
        self.__users: set[User] = users
        self.bookHandler: Handler = bookHandler
    
    def __selectPerName(allBooks: set[Book], nameSearch: str) -> set[Book]:
        specificBooks: set[Book] = set()
        for book in allBooks:
            if (book.getName().upper()).find(nameSearch.upper()) != -1: specificBooks.add(book)
            elif (book.getAuthor().upper()).find(nameSearch.upper()) != -1: specificBooks.add(book)
        return specificBooks
    
    def __selectPerAuthor():
        pass

    def __getAllBooks(self) -> set[Book]:
        allBooks: set[Book] = set()
        for book in self.__books:
            for unique in book.getBooks():
                allBooks.add(unique)
        return allBooks
    
    def __getAllBookAndCategorie(self) -> set[Book]:
        allCategoriesAndBook: set[Book] = set()
        for book in self.__books:
            for categorie in book.getAll():
                allCategoriesAndBook.add(categorie)
        return allCategoriesAndBook

    def __getBook(self, _id: int) -> Book|None:
        for book in self.__getAllBooks():
            if book.getId() == _id: return book
        print("Nenhum livro encontrado com esse id!")
        return None

    def __reservation(self, book: Book, user: User) -> None:
        user.reserveBook(book.getId())
        print("Reserva feita\n")
    
    def __loan(self, book: Book, user: User) -> None:
        book.removeAvaliable()
        user.loan(book.getId())
        print("Emprestimo Feito com sucesso\n")
        user.removeBook(book.getId())
    
    def __returnal(self, book: Book, user: User) -> None:
        user.returnal(book)
        book.addAvaliable()
        book.notifyReturn()
        print("Livro devolvido com sucesso\n")

    def searchBook(self, nameSearch: str):
        allBooks = self.__getAllBookAndCategorie()
        specificBooks = LibraryFacade.__select(allBooks, nameSearch)
        if (len(specificBooks)<1): print("Nenhum livro foi encontrado\n")
        else:
            specificBooks: list[Book] = list(specificBooks)
            specificBooks.sort(key = lambda book: book.getName())
            for i , book in enumerate(specificBooks, start= 1):
                print(f'{i}- {book}\n')

    def borrowBook(self, _id: int, user: User):
        book = self.__getBook(_id)
        if book is None: return 
        if self.bookHandler.eligible(book, user):
            self.__loan(book, user)
        else:
            wantReservation = int(input("Não foi possível realizar o emprestimo, gostaria de reservá-lo? Digite 1 para sim ou 0 para não: ")) #Caso ele não possa emprestar, dar a opção de reservar o livro (dica: função __reserva)
            match wantReservation:
                case 0:
                    print("Você irá retornar para o menu.\n")
                case 1:
                    self.__reservation(book, user)
                case _:
                    print("Opção inválida, você irá retornar para o menu.\n")

    def returnBook(self, _id: int, user: User):
        book = self.__getBook(_id)
        if _id in user.getLoan():
            self.__returnal(book, user)
        else:
            if book is None:
                print("Livro não encontrado na livraria!\n")
            else:
                print("Este livro não foi emprestado por você! Ele não está cadastrado no seu cpf!\n")

    def getInformationBook(self, _id: int):
        book = self.__getBook(_id)
        if not (book is None):
            print("Id:",_id)
            print("Título:",book.getName())
            print("Autor:", book.getAuthor())
            print("Quantidade de cópias disponíveis:",book.getAvaliabe().count(True))

    def presentation(self, user: User) -> None:
        userBooks = set()
        for _id in user.getLoan():
            book = self.__getBook(_id)
            userBooks.add(book)
        user.presentation(userBooks)
