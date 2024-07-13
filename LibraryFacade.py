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
    
    def __select(allbBooks: set[Book], nameBook: str) -> set[Book]:
        specificBooks: set[Book] = set()
        for book in allbBooks:
            if (book.getName().upper()).includes(nameBook.upper()): specificBooks.add(book)

    def searchBook(self, nameBook):
        allBooks: set[Book] = set()
        for book in self.__books:
            allBooks.add(*book.getBooks())
        specificBooks = self.__select(allBooks, nameBook)
        if (len(specificBooks)<1): print("Nenhum livro foi encontrado\n")
        else:
            specificBooks = list(specificBooks)
            specificBooks.sort(key = lambda book: book.nome)
            for i , book in enumerate(specificBooks, start= 1):
                print(f'{i}- {book}\n')

    def borrowBook(self, book: Book, user: User):
        if self.bookHandler.eligible(user,book):
            self.__loan(book,user)
        else:
            wantReservation = int(input("Não foi possível realizar o emprestimo, gostaria de reservá-lo? Digite 1 para sim ou 0 para não: ")) #Caso ele não possa emprestar, dar a opção de reservar o livro (dica: função __reserva)
            match wantReservation:
                case 0:
                    print("Você irá retornar para o menu.\n")
                case 1:
                    self.__reservation(book, user)
                case _:
                    print("Opção inválida, você irá retornar para o menu.\n")

    def __reservation(self, book: Book, user: User) -> None:
        user.reservarLivro(book)
        print("Reserva feita\n")
    
    def __loan(self, book: Book, user: User) -> None:
        book.removeAvaliable()
        user.loan(book)
        print("Emprestimo Feito com sucesso\n")
    
    def __returnal(self, book: Book, user: User) -> None:
        user.returnal(book)
        book.addAvaliable()
        book.notifyReturn()
        print("Livro devolvido com sucesso\n")

    def returnBook(self, book: Book, user: User):
        if user.getLoan.includes(book):
            self.__returnal(book,user)
        else:
            print("O livro deve ser devolvido por quem o emprestou! Este não está cadastrado no seu cpf!")
