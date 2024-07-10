from abc import ABC, abstractmethod



class Observer(ABC):
    
    @abstractmethod
    def update():
        pass


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


class Sensor(Observable):
    
    def __init__(self) -> None:
        super().__init__()
        self.ph: int = 7
        self.temp: int = 28
    

    def set_data(self, ph: int, temp: int):
        self.ph = ph
        self.temp = temp
        self.notify()


class universidade(Observer):
    
    def __init__(self, nome: str) -> None:
        self.nome = nome


    def update(self, sensor: Observable):
        print(f'Universidade {self.nome}:\nNovo PH é: {sensor.ph}\nNova temperatura é: {sensor.temp}\n')


class teste():

    def teste():

        #Criando sensores
        sensor1 = Sensor()
        sensor2 = Sensor()
        sensor3 = Sensor()
        sensor4 = Sensor()
        sensor5 = Sensor()
        
        #Criando universidades
        universidade_observer1 = universidade("Universidade 1")  
        universidade_observer2 = universidade("Universidade 2")  
        universidade_observer3 = universidade("Universidade 3")
        
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



if __name__ == "__main__":
    teste.teste()
