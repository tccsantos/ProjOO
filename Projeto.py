"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
*                                                                                                                                                                                                        *
*                                                                                   "Library System"                                                                                                     *
*                                                                                  ******************                                                                                                    *
*                 Este projeto compõe o sistema de avaliação da Unidade Curricular Projeto Orientado a Objetos do 1º semestre de 2024, ofertada pela UNIFESP ICT pelo docente Fábio Fagundes.            *
*                                          Ele simula o funcionamento básico de um sistema de empréstimos e devoluções de uma biblioteca.                                                                *               
*                ******************************************************************************************************************************************************************************          *
*                                                                                                                                                                                                        *
*                                              Desenvolvido por: Maria Clara Couto Lorena  RA 163941 e Thiago Cortez Cursino dos Santos  RA 163997                                                       *
*                                                                                                                                                                                                        *
*                                    UML disponível em: https://www.figma.com/design/MoJ2j7rh06FFnWQQm3v3GK/Sistema-de-Biblioteca?node-id=0-1&t=8HoB8VGWEhJrnpX5-1                                       *
*                                                                                                                                                                                                        *
*                                                                                                                                                                                                        *
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
"""

from LibraryFacade import LibraryFacade
from Adapter import csvReader
from Handler import BookAvaliabilityHandler, UserEligibilityHandler, LoanLimitHandler
from Configuration import LibraryManager
from bookAvaliabilityNotifier import bookAvaliabilityNotifier
from Abstract import User



class main:

    def teste():

        interface, users = main.start()
        
        for user in users:

            print("Bem vindo, ", end='')
            print(user, end='')
            print("\n")

            while(True):

                print("Digite 1 para buscar um livro.\nDigite 2 para pegar um livro emprestado.")
                print("Digite 3 para devolver um livro.\nDigite 4 para consultar a informação de um livro.")
                print("Digite 5 para consultar a o seu perfil de usuário .\nDigite 0 para sair do programa.\n\n")

                choice = int(input("O que deseja fazer?: "))
                print()
                
                match choice:

                    case 1:
                        name = input("Digite o nome do livro que deseja buscar: ")
                        print()
                        interface.searchBook(name)

                    case 2:
                        _id = int(input("Digite o id do livro que deseja emprestar: "))
                        print()
                        interface.borrowBook(_id=_id, user=user)
                    
                    case 3:
                        _id = int(input("Digite o id do livro que deseja retornar: "))
                        print()
                        interface.returnBook(_id=_id, user=user)
                    
                    case 4:
                        _id = int(input("Digite o id do livro que deseja consultar: "))
                        print()
                        interface.borrowBook(_id=_id, user=user) # Errado
                            
                    case 5:
                        interface.presentation(user=user)
                    
                    case 0:
                        break
                    
                    case _:
                        print("Opção inválida\n")

    def start() -> tuple[LibraryFacade, set[User]]:
        
        init = csvReader("./Banco/Books.csv", "./Banco/Users.csv")
        users, books = init.initialize()

        loan = {"Teacher": 30, "Student": 10}
        Multiply = {"Teacher": 10, "Student": 1}

        manager = LibraryManager(loan, Multiply)

        handler3 = LoanLimitHandler(manager=manager)
        handler2 = BookAvaliabilityHandler(handler3, manager)
        handler1 = UserEligibilityHandler(handler2, manager)

        notifier = bookAvaliabilityNotifier(users)

        for book in books:
            if book.isComposite():
                for one in book.getBooks():
                    one.setMediator(notifier)
            else: book.setMediator(notifier)


        fachada = LibraryFacade(users, books, handler1)

        return fachada, users


if __name__ == "__main__":
    main.teste()
