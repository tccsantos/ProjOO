from Abstract import Book


#Baseando-se no Design Pattern Composite, esta é a classe composta
class CompositionBook(Book):
    
    def __init__(self, name: str, _id: int, books: set[Book]) -> None:
        super().__init__(name, _id)
        self.books = books

    def addElement(self, books: Book):
        self.books.add(books)

    def removeElement(self, books: Book):
        self.books.discard(books)

    def isComposite(self) -> bool:
        return True

    def getBooks(self):
        allBooks: set[Book] = set()
        for book in self.books:
            childs = book.getBooks()
            if isinstance(childs, set):
                for child in childs: allBooks.add(child)
            else:
                allBooks.add(childs)

        return allBooks
    
    def getCompositions(self):
        allCompositions: set[Book] = set()
        allCompositions.add(self)
        for book in self.books:
            childs = book.getCompositions()
            if isinstance(childs, set):
                for child in childs: allCompositions.add(child)
            else:
                allCompositions.add(childs)

        return allCompositions
       
    def getAuthor(self) -> str:
        return ''


#Baseando-se no Design Pattern Composite, esta é a classe folha
class SingleBook(Book):
    
    def __init__(self, name: str, _id: int, author: set[str], quantity: int) -> None:
        super().__init__(name, _id)
        self.__author = author
        self.__quantity = quantity
        self.__avaliabe = [True] * quantity

    def isComposite(self) -> bool:
        return False 

    def getBooks(self):
        return self
    
    def getCompositions(self):
        return set()
    
    def getAvaliabe(self) -> list[bool]:
        return self.__avaliabe
    
    def addAvaliable(self):
        try:
            self.__avaliabe[self.__avaliabe.index(False)] = True
        except:
            print("Erro! Você está tentando deixar um livro disponível, mas todos já estão disponíveis")

    def removeAvaliable(self):
        try:
            self.__avaliabe[self.__avaliabe.index(True)] = False
        except:
            print("Erro! Você está tentando pegar um livro, mas todos já estão emprestados")
    
    def getQuantity(self) -> list[bool]:
        return self.__quantity
    
    def notifyReturn(self):
        self.getMediator().notify(self)
    
    def getAuthor(self) -> str:
        return self.__author
