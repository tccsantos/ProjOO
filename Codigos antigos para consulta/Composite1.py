#Thiago Cortez Cursino dos Santos  RA 163997

from abc import ABC, abstractmethod



class Participante(ABC):

    @abstractmethod
    def getAssento(self):
        pass

    @abstractmethod
    def getMembros(self):
        pass


class Individuo(Participante):
    
    def __init__(self, nome: str, presencial: bool) -> None:
        self.nome = nome
        self.presencial = presencial
    
    def getAssento(self):
        if self.presencial: return 1
        else: return 0
    
    def getMembros(self):
        return 1


class Instituicao(Participante):
    
    def __init__(self, membros: set[Participante], nome: str) -> None:
        self.nome = nome
        self.membros = membros
    
    def getAssento(self):
        assentos = 0
        for membro in self.membros:
            assentos += membro.getAssento()
        return assentos
    
    def getMembros(self):
        membros = 0
        for membro in self.membros:
            membros += membro.getMembros()
        return membros


class Congresso():

    def __init__(self, participantes: set[Participante] | None = None) -> None:
        self.participantes = participantes
    
    def totalParticipantes(self):
        participantes = 0
        for participante in self.participantes:
            participantes += participante.getMembros()
        return participantes

    def totalAssentos(self):
        assentos = 0
        for participante in self.participantes:
            assentos += participante.getAssento()
        return assentos
    
    def addParticipante(self, participante: Participante):
       if self.participantes != None: self.participantes.add(participante)
       else: self.participantes = {participante}


class main():

    def teste():
        # Criando Individuos
        individuo1 = Individuo("João", presencial=True)
        individuo2 = Individuo("Maria", presencial=False)
        individuo3 = Individuo("Pedro", presencial=True)
        individuo4 = Individuo("Ana", presencial=True)
        individuo5 = Individuo("Carlos", presencial=False)
        individuo6 = Individuo("Julia", presencial=True)
        
        # Criando instituições
        instituicao1 = Instituicao({individuo1, individuo2}, "Empresa X")
        instituicao2 = Instituicao({individuo3, individuo4}, "Empresa Y")
        
        # Criando o congresso e adicionando os participantes
        congresso = Congresso()
        congresso.addParticipante(individuo6)
        congresso.addParticipante(instituicao1)
        congresso.addParticipante(instituicao2)
        congresso.addParticipante(individuo5)

        print(congresso.totalParticipantes())
        print(congresso.totalAssentos())



if __name__ == '__main__':
    main.teste()
