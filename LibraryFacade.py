from Abstract import User, Book, Handler
from unidecode import unidecode


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

    def __getAllBooks(self) -> set[Book]:
        allBooks: set[Book] = set()
        for book in self.__books:
            for unique in book.getBooks():
                allBooks.add(unique)
        return allBooks
    
    def __getAllCategories(self) -> set[Book]:
        allCategories: set[Book] = set()
        for book in self.__books:
            for categorie in book.getCompositions():
                allCategories.add(categorie)
        return allCategories

    def __getBook(self, _id: int) -> Book|None:
        for book in self.__getAllBooks():
            if book.getId() == _id: return book
        return None
    
    def __getCategory(self, _id: int) -> Book|None:
        for category in self.__getAllCategories():
            if category.getId() == _id: return category
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

    def __selectPerName(allBooks: set[Book], nameSearch: str) -> set[Book]:
        specificBooks: set[Book] = set()
        for book in allBooks:
            if (book.getName().upper()).find(nameSearch.upper()) != -1: specificBooks.add(book)
        return specificBooks
    
    def __selectPerAuthor(allBooks: set[Book], nameSearch: str) -> set[Book]:
        specificBooks: set[Book] = set()
        for book in allBooks:
            if (unidecode(book.getAuthor().upper())).find(unidecode(nameSearch.upper())) != -1: specificBooks.add(book)
        return specificBooks
    
    def __selectPerCategory(allCategories: set[Book], nameSearch: str) -> set[Book]:
        specificCategories: set[Book] = set()
        for book in allCategories:
            if (unidecode(book.getName().upper())).find(unidecode(nameSearch.upper())) != -1: specificCategories.add(book)
        return specificCategories

    def __searchBookPerName(self, nameSearch: str):
        allBooks = self.__getAllBooks()
        specificBooks = LibraryFacade.__selectPerName(allBooks, nameSearch)
        if (len(specificBooks)<1): print("Nenhum livro foi encontrado\n")
        else:
            specificBooks: list[Book] = list(specificBooks)
            specificBooks.sort(key = lambda book: book.getName())
            for i , book in enumerate(specificBooks, start= 1):
                print(f'\n{i}- {book}\n')
    
    def __searchBookPerAuthor(self, nameSearch: str):
        allBooks = self.__getAllBooks()
        specificBooks = LibraryFacade.__selectPerAuthor(allBooks, nameSearch)
        if (len(specificBooks)<1): print("Nenhum livro foi encontrado\n")
        else:
            specificBooks: list[Book] = list(specificBooks)
            specificBooks.sort(key = lambda book: book.getName())
            for i , book in enumerate(specificBooks, start= 1):
                print(f'\n{i}- {book}\n')

    def __searchBookPerCategory(self, nameSearch: str):
        allCategories = self.__getAllCategories()
        specificCategories = LibraryFacade.__selectPerCategory(allCategories, nameSearch)
        if (len(specificCategories)<1): print("Não existe nenhuma categoria com esse nome.\n")
        else:
            specificCategories: list[Book] = list(specificCategories)
            specificCategories.sort(key = lambda book: book.getName())
            for i , categorie in enumerate(specificCategories, start= 1):
                print(f'\n{i}- {categorie.getName()}:\n')
                books: set[Book] = categorie.getBooks()
                if(len(books)<1): 
                    print("\tNenhum livro registrado nessa categoria.\n")
                    continue
                books: list[Book] = list(books)
                books.sort(key = lambda book: book.getName())
                for j, book in enumerate(books, start=1):
                    print(f'\t{j}- {book.getName()}\n\tAutor: {book.getAuthor()}\n\tid: {book.getId()}\n')
      
    def searchBook(self):
        print("Métodos de pesquisa:\n1. Por título\n2. Por autor\n3. Por categoria")
        try:
            method: int = int(input("Digite a opção de pesquisa: "))
        except:
            print("Opção inválida, você irá retornar para o menu.\n")
            return
        match(method):
            case(1):
                name: str = input("Digite o título que gostaria de pesquisar: ")
                self.__searchBookPerName(name)
            case(2):
                author: str = input("Digite o autor que gostaria de pesquisar: ")
                self.__searchBookPerAuthor(author)
            case(3):
                categorie: str = input("Digite a categória que gostaria de pesquisar: ")
                self.__searchBookPerCategory(categorie)
            case _:
                print("Opção inválida, você irá retornar para o menu.\n")

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
        book: Book|None = self.__getBook(_id)
        category: Book|None = self.__getCategory(_id)
        if book is None and category is None:
            print("id não existe no banco de dados!\n")
            return
        print("Id:",_id)
        if book is None:
            print("Título:",category.getName())
            if (livros := len(category.getBooks())) < 2:
                print(f'Catálogo com 1 livro.')
            else:
                print(f'Catálogo com {livros} livros.')
        else:
            print("Título:",book.getName())
            print("Autor:", book.getAuthor())
            print("Quantidade de cópias disponíveis:",book.getAvaliabe().count(True))
        print()

    def presentation(self, user: User) -> None:
        userBooks = set()
        for _id in user.getLoan():
            book = self.__getBook(_id)
            userBooks.add(book)
        user.presentation(userBooks)
