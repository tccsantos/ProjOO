#Thiago Cortez Cursino dos Santos  RA 163997

from abc import ABC, abstractmethod



class Processor(ABC):

    @abstractmethod
    def statistic():
        pass


class Spaces(Processor):

    def __init__(self, successor: Processor = None) -> None:
        self.successor: Processor = successor

    def statistic(self, string: str):
        print(f"Quantidade de espaços: {string.count(' ')}")
        self.successor.statistic(string)


class Letras_a(Processor):

    def __init__(self, successor: Processor = None) -> None:
        self.successor: Processor = successor

    def statistic(self, string: str):
        print(f"Quantidade de letras a: {string.count('a')}")
        self.successor.statistic(string)


class Pontos(Processor):

    def __init__(self, successor: Processor = None) -> None:
        self.successor: Processor = successor

    def statistic(self, string: str):
        print(f"Quantidade de pontos: {string.count('.')}")


class cliente:

    def teste():

        #Instaciamento da cadeia de responsabilidades
        pontos: Processor = Pontos()
        letras: Processor = Letras_a(pontos)
        processor: Processor = Spaces(letras)

        #Criação de alguns testes
        teste1: str = 'Hello World'
        teste2: str = 'Projeto orientado a objetos'
        teste3: str = 'No meio do caminho tinha uma pedra. Tinha uma pedra no meio do caminho. Tinha uma pedra. No meio do caminho tinha uma pedra. Nunca me esquecerei desse acontecimento. Na vida de minhas retinas tão fatigadas. Nunca me esquecerei que no meio do caminho. Tinha uma pedra. Tinha uma pedra no meio do caminho. No meio do caminho tinha uma pedra.'

        #Teste da cadeia de responsabilidades
        processor.statistic(teste1)
        print()
        processor.statistic(teste2)
        print()
        processor.statistic(teste3)



if __name__ == '__main__':
    cliente.teste()
