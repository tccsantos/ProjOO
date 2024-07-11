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

    def start(self):
        ...

if __name__ == "__main__":
    main().teste()
