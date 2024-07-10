#Thiago Cortez Cursino dos Santos  RA 163997

from abc import ABC, abstractmethod



class Sujeito(ABC):
    
    @abstractmethod
    def operacao():
        pass


class Cliente:

    def __init__(self, operador: Sujeito) -> None:
        self.operador: Sujeito = operador

    def method(self):
        print("Inicializando operação!")
        self.operador.operacao()


class Intermediario(Sujeito):

    def __init__(self, proxy) -> None:
        self.proxy: Sujeito = proxy

    def operacao(self):
        self.proxy.operacao()


class SujeitoReal(Sujeito):

    def __init__(self) -> None:
        pass

    def operacao(self):
        print("Operação feita com Sucesso!!")


class teste:

    def teste():

        #Instaciamento das classes
        real: Sujeito = SujeitoReal()
        proxy: Sujeito = Intermediario(real)
        cliente: Cliente = Cliente(proxy)


        #Teste do proxy
        cliente.method()


if __name__ == "__main__":
    teste.teste()
