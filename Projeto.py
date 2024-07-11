#Maria Clara Couto Lorena  RA 163941
#Thiago Cortez Cursino dos Santos  RA 163997
from LibraryFacade import LibraryFacade
from User import StudentUserType, TeacherUserType
from Book import Book

from csv import reader



class main():


    def teste():

        interface : LibraryFacade = ...


        while(True):
            print("Digite 1 para buscar um livro.\nDigite 2 para pegar um livro emprestado.")
            print("Digite 3 para devolver um livro.\nDigite 0 para sair do programa.\n\n")
            choice = int(input("O que deseja fazer?: "))
            
            match choice: #Incompleto!!!!!

                case 1:
                    interface.buscaLivros()

                case 2:
                    interface.emprestaLivros()
                        
                case 3:
                    interface.devolveLivros()
                
                case 4:
                    break
                
                case _:
                    print("Opção inválida\n")


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
    

    def start(self):
        ...

if __name__ == "__main__":
    main().teste()
