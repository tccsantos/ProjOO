


class animal:

    def __init__(self, nome, id, vacina, tipo, tamanho, raca, vaga, adotado = False) -> None:
        self.__nome = nome
        self.__id = id
        self.__vacinado: dict = vacina
        self.__tipo = tipo
        self.__tamanho = tamanho
        self.__raca = raca
        self.__adotado = adotado
        self.__cela: cela = vaga

    
    def __vacina(self, vacina: str, new):
        self.__vacinado[vacina.lower()] = new
        

    def atualiza_vacina(self, vacina, new):
        self.__vacina(vacina, new)

    
    def adotar(self, op: bool):
        if self.__adocao(op):
            return True
        else: return False

    
    def __adocao(self, op):
        self.__adotado = op
        if self.__adotado == op: return True
        else: return False


    def adocao(self):
        return self.__adotado


class Adocao:

    def __init__(self, data, protocolo, cliente, animais: list[animal]) -> None:
        self.__data = data
        self.__protocolo = protocolo
        self.__cliente = cliente
        self.__animal: list[animal] = animais
        for criat in animais:
            if not criat.adocao():
                criat.adotado = True
            else:
                raise ValueError
        self.__retorno = False

    def devolucao(self):
        if not self.__devolver():
            raise SystemError
        return
    

    def __devolver(self):
        self.__retorno = True
        if self.__animal.adotar(False) and self.__retorno: return False
        else: return True

class cela:


    def __init__(self, numero, tamanho, ocupa = 0) -> None:
        self.__numero = numero
        self.__tamanho = tamanho
        self.__qnt_ocupa = ocupa


    def __lotado(self):
        if self.__qnt_ocupa >= self.__tamanho:
            return True
        else: return False
    
# I Segregação de interfaces: Método público com única responsabilidade de retornar a lotação, não
#   importando como é implementado
    def lotacao(self):
        return self.__lotado()
    

    def __adicionar(self):
        if not self.__lotado():
            self.__qnt_ocupa += 1
        else:
            print('lotado')
            return 
    

    def adicao(self):
        self.__adicionar()

    
# S Responsabilidade única: classe somente guarda os dados de cada cliente e os atualiza se necessário
class pessoa:


    def __init__(self, nome, cpf, data_nasc, telefone) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nasc = data_nasc
        self.__telefone = telefone

    
    def atualiza_dados(self, nome = None, cpf = None, data_nasc = None, telefone = None):
        self.__atualiza(nome, cpf, data_nasc, telefone)
    

    def __atualiza(self, nome, cpf, data_nasc, telefone):
        if nome: self.__nome = nome
        if cpf: self.__cpf = cpf
        if data_nasc: self.__data_nasc = data_nasc
        if telefone: self.__telefone = telefone


    def dados(self):
        print(f'nome: {self.__nome}')
        print(f'cpf: {self.__cpf}')
        print(f'data de nascimento: {self.__data_nasc}')
        print(f'telefone: {self.__telefone}')