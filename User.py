from abc import ABC, abstractmethod
import time


class User(ABC):

    def __init__(self,nome: str, cpf: str, nascimento: str):
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__nascimento: str = nascimento #"08062004"

    def solicitarNome(self) -> str:
        return self.__nome
    
    def solicitarCpf(self) -> str:
        return self.__cpf
    
    def solicitarIdade(self) -> int:
        return int(time.gmtime().tm_year) - int(self.__nascimento[-4:])
    
    # @abstractmethod
    # def pegarEmprestimo():
    #     pass



class StudentUserType(User):
    def __init__(self, nome, cpf, nascimento):
        super().__init__(nome, cpf, nascimento)


class TeacherUserType(User):
    def __init__(self, nome, cpf, nascimento):
        super().__init__(nome, cpf, nascimento)