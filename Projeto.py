#Maria Clara Couto Lorena  RA 163941
#Thiago Cortez Cursino dos Santos  RA 163997
from LibraryFacade import LibraryFacade
from Adapter import csvReader
from Handler import BookAvaliabilityHandler, UserEligibilityHandler, LoanLimitHandler
from Configuration import LibraryManager




class main():


    def teste():

        interface: LibraryFacade = main.start()


        while(True):
            print("Digite 1 para buscar um livro.\nDigite 2 para pegar um livro emprestado.")
            print("Digite 3 para devolver um livro.\nDigite 0 para sair do programa.\n\n")
            choice = int(input("O que deseja fazer?: "))
            
            match choice: #Incompleto!!!!!

                case 1:
                    interface.searchBook()

                case 2:
                    interface.borrowBook()
                        
                case 3:
                    interface.returnBook()
                
                case 4:
                    break
                
                case _:
                    print("Opção inválida\n")

    def start() -> LibraryFacade:
        
        init = csvReader("./Banco/Books.csv", "./Banco/Users.csv")
        users, books = init.initialize()

        loan = {"Teacher": 30, "Student": 10}
        Multiply = {"Teacher": 10, "Student": 1}

        manager = LibraryManager(loan, Multiply)

        handler3 = LoanLimitHandler(manager=manager)
        handler2 = BookAvaliabilityHandler(handler3, manager)
        handler1 = UserEligibilityHandler(handler2, manager)


        fachada = LibraryFacade(users, books, handler1)

        return fachada


if __name__ == "__main__":
    main().teste()
