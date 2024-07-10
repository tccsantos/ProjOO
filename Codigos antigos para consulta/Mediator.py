#Thiago Cortez Cursino dos Santos  RA 163997

from abc import ABC, abstractmethod



class Mediator(ABC):

    @abstractmethod
    def alert():
        pass


class Observer(ABC):
    
    @abstractmethod
    def update():
        pass

    def set_mediator(self, media: Mediator):
        self.mediator: Mediator = media


class Observable(ABC):
    
    def __init__(self) -> None:
        self.observers: set[Observer] = set()

    
    def add(self, o: Observer):
        self.observers.add(o)
    

    def remove(self, o: Observer):
        self.observers.discard(o)


    def notify(self):
        for o in self.observers:
            o.update(self)
    

    def set_mediator(self, media: Mediator):
        self.mediator: Mediator = media


class Sensor(Observable):
    
    def __init__(self, nome) -> None:
        super().__init__()
        self.ph: int = 7
        self.temp: int = 28
        self.mediator: Mediator = None
        self.nome: str = nome
    

    def set_data(self, ph: int, temp: int):
        self.ph = ph
        self.temp = temp
        if (ph > 10 or ph < 3 or temp < 16 or temp > 40) and self.mediator:
            self.mediator.alert(self)
        else:
            self.notify()


class Universidade(Observer):
    
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.mediator = None


    def update(self, sensor: Observable):
        print(f'{self.nome} obteve os dados atualizados de {sensor.nome}:\nNovo PH é: {sensor.ph}\nNova temperatura é: {sensor.temp}\n')
    

class Alerta(Mediator):

    def __init__(self, sensores: list[Sensor], universidades: list[Universidade]) -> None:
        self.universidades: list[Universidade] = universidades
        #self.sensores: list[Sensor] = sensores
        for sensor in sensores:
            sensor.set_mediator(self)
        for universidade in universidades:
            universidade.set_mediator(self)
    
    def alert(self, distress: Sensor):
        print(f'Alerta para todas as universidades!! {distress.nome} está em situação crítica!!!\n')
        for universidade in self.universidades:
            universidade.update(distress)
        print('Fim de alerta')


class teste:

    def teste():

        #Criando sensores
        sensor1 = Sensor('Sensor 1')
        sensor2 = Sensor('Sensor 2')
        sensor3 = Sensor('Sensor 3')
        sensor4 = Sensor('Sensor 4')
        sensor5 = Sensor('Sensor 5')
        
        #Criando universidades
        universidade_observer1 = Universidade("Universidade 1")  
        universidade_observer2 = Universidade("Universidade 2")  
        universidade_observer3 = Universidade("Universidade 3")

        #Universidade que não está interessada em nenhum sensor
        universidade_indiferente = Universidade("Universidade indiferente")

        #Criando mediador
        Alerta([sensor1, sensor2, sensor3, sensor4, sensor5], [universidade_observer1, universidade_observer2, universidade_observer3, universidade_indiferente])
        
        #Executando testes
        sensor1.add(universidade_observer1)
        sensor2.add(universidade_observer2)
        sensor3.add(universidade_observer3)
        sensor4.add(universidade_observer2)
        sensor5.add(universidade_observer1)
        sensor2.add(universidade_observer1)
        sensor1.add(universidade_observer3)

        
        sensor1.set_data(6, 30)
        sensor2.set_data(7, 25)
        sensor3.set_data(5, 27)
        sensor4.set_data(6, 23)
        sensor5.set_data(4, 24)

        #Sensor em situação crítica
        sensor3.set_data(2, 27)



if __name__ == "__main__":
    teste.teste()
