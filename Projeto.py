"""
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
*                                                                                                                                                                                                        *
*                                                                                   "Library System"                                                                                                     *
*                                                                                  ******************                                                                                                    *
*                 Este projeto compõe o sistema de avaliação da Unidade Curricular Projeto Orientado a Objetos do 1º semestre de 2024, ofertada pela UNIFESP ICT pelo docente Fábio Fagundes.            *
*                                          Ele simula o funcionamento básico de um sistema de empréstimos e devoluções de uma biblioteca.                                                                *               
*                *****************************************************************************************************************************************************************************           *
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

    def __start() -> tuple[LibraryFacade, set[User]]:
        
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

    def __unscramble(teacher: User, student: User) -> tuple[User]:
        
        if teacher.isType() != "Teacher":
            return student, teacher
        else: return teacher, student

    def teste():

        '''
        Essa função é para testar
        o sistema da maneira que quiser
        '''

        interface, users = main.__start()

        teacher, student = main.__unscramble(*tuple(users))
        
        while(True):
            
            try:
                op = int(input("Digite 0 para aluno, 1 para professor: "))

                if op == 0: user = student
                elif op == 1: user = teacher
                else: print("Opção inválida")
            
            except Exception:
                print("Opção inválida")
                return

            print()


            print("Bem vindo, ", end='')
            print(user, end='')
            print("\n")

            while(True):

                print("Digite 1 para buscar um livro.\nDigite 2 para pegar um livro emprestado.")
                print("Digite 3 para devolver um livro.\nDigite 4 para consultar a informação de um livro.")
                print("Digite 5 para consultar o seu perfil de usuário.\nDigite 0 para sair do programa.\n\n")

                choice = int(input("O que deseja fazer?: "))
                print()
                
                match choice:

                    case 1:
                        print("Métodos de pesquisa:\n1. Por título\n2. Por autor\n3. Por categoria")
                        try:
                            method: int = int(input("Digite a opção de pesquisa: "))
                        except:
                            print("Opção inválida, você irá retornar para o menu.\n")
                            return
                        match(method):
                            case(1):
                                busca: str = input("Digite o título que gostaria de pesquisar: ")
                            case(2):
                                busca: str = input("Digite o autor que gostaria de pesquisar: ")
                            case(3):
                                busca: str = input("Digite a categória que gostaria de pesquisar: ")
                            case _:
                                print("Opção inválida, você irá retornar para o menu.\n")
                        
                        interface.searchBook(method, busca)

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
                        interface.getInformationBook(_id=_id)
                            
                    case 5:
                        interface.presentation(user=user)
                    
                    case 0:
                        break
                    
                    case _:
                        print("Opção inválida\n")

            choice = input("Você deseja testar novamente? (y/n) ")

            if choice == 'y': continue
            elif choice == 'n': break
            else:
                print("Opção inválida, mas ok neh, saindo")
                break

    def show():
        
        '''
        Essa função demonstra alguns
        exemplos do sistema funcionando.

        A apresentação pode não funcionar
        corretamente caso o banco de dados
        já tenha valores salvos.
        '''
        
        interface, users = main.__start()

        teacher, student = main.__unscramble(*tuple(users))

        print("Primeiro, faremos as apresentações dos usuários: \n")

        print("Usuário Professor: ")
        interface.presentation(teacher)

        print("Usuário Aluno")
        interface.presentation(student)  
        print()


        print("Vamos buscar por livros pelas três maneiras possíveis: \n")

        print("Por nome:\t o termo de busca foi 'Calculo'")
        interface.searchBook(1, "Calculo")

        print("Por autor:\t o termo de busca foi 'Sanderson'")
        interface.searchBook(2, "Sanderson")

        print("Por categoria:\t o termo de busca foi 'Programação'")
        interface.searchBook(3, "Programação")
        print()


        print("Pesquisaremos sobre o Livro 'Algoritimos e seus fundamentos': \n")
        interface.getInformationBook(7)

        print("Vale lembrar que tivemos que usar o id do livro para tal, isso será necessário para todos os métodos a seguir.")
        print()


        print("Faremos alguns empréstimos agora: \n")

        print("Com o professor, pegaremos emprestado o livro 'Algoritimos e seus fundamentos': \n")

        interface.borrowBook(7, teacher)

        interface.presentation(teacher)
        print()


        print("Com o aluno, pegaremos emprestado o livro 'Algoritimos e estruturas de dados': \n")

        interface.borrowBook(6, student)

        interface.presentation(student)
        print()


        print("Agora, com o aluno, tentaremos pegar emprestado o livro'Algoritimos e seus fundamentos' e depois o livro 'Algoritimos e estruturas de dados' novamente: \n")

        interface.borrowBook(7, student, 1)
        print()
        interface.borrowBook(6, student, 0)

        print('O primeiro não deu certo pois não havia livros disponíveis, o segundo pois estudantes não podem pegar mais de um livro do mesmo emprestado.')
        print()


        print("Pesquisaremos sobre o Livro 'Algoritimos e seus fundamentos' novamente, para ver a quantidade disponível: \n")
        interface.getInformationBook(7)


        print("Veremos então o professor retornando o livro 'Algoritimos e seus fundamentos': \n")

        interface.returnBook(7, teacher)
        
        print("E agora, o aluno poderá pegar emprestado o Livro")

        interface.borrowBook(7, student, 0)
        print()


        print("Por último, farei a apresentação dos usuários antes e depois do aluno devolver o livro 'Algoritimos e seus fundamentos'. \n")

        interface.presentation(teacher)
        interface.presentation(student)

        interface.returnBook(7, student)
        interface.returnBook(6, student)

        interface.presentation(teacher)
        interface.presentation(student)
        
        print("\nAqui termina a apresentação inicial do sistema, tenha em mente que os históricos não são salvos no banco de dados, somente os ", end = '')
        print("empréstimos e reservas. Sinta-se a vontade a usar o método de teste para avaliar todas as funções do sistema por si mesmo.")
        print("\nMuito obrigado pela atenção.")


if __name__ == "__main__":
    try:
        choice = int(input("Digite 0 para ver a apresentação do sistema, digite 1 para testar por si mesmo. "))

        if choice == 0: main.show()
        elif choice == 1: main.teste()
        else: print("Opção inválida")
    
    except Exception:
        print("Opção inválida")
