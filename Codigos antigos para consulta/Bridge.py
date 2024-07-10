#Thiago Cortez Cursino dos Santos  RA 163997

from abc import ABC, abstractmethod


class Implementador(ABC):

    @abstractmethod
    def queue(self):
        pass

    @abstractmethod
    def add(self, num, pos: int):
        pass

    @abstractmethod
    def remove(self, pos):
            pass


class Queue(ABC):
    
    @abstractmethod
    def __init__(self, bridge) -> None:
        self.bridge = bridge

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def isEmpty(self):
        pass


class Fifo(Queue):

    def __init__(self, bridge) -> None:
        super().__init__(bridge)

    def size(self):
        return self.bridge.queue()
    
    def isEmpty(self):
        if self.size(): return False
        else: return True

    def enque(self, adi):
        self.bridge.add(adi, -1)
    
    def deque(self):
        return self.bridge.remove(0)


class Array(Implementador):

    def __init__(self) -> None:
        self.array = list()
    
    def queue(self):
        return len(self.array)

    def add(self, num, pos: int):
        if pos == -1:
            self.array.append(num)
        elif pos < len(self.array):
            self.array.insert(pos, num)
        else: print('posição inválida')
    
    def remove(self, pos):
        if pos < len(self.array): return self.array.pop(pos)
        else: print('posição inválida')
    

class LinkedList(Implementador):

    def __init__(self) -> None:
        self.link = list()
    
    def queue(self):
        return len(self.link)

    def add(self, num, pos: int):
        if pos == -1:
            self.link.append(num)
        elif pos < len(self.array):
            self.link.insert(pos, num)
        else: print('posição inválida')
    
    def remove(self, pos):
        if pos < len(self.link): return self.link.pop(pos)
        else: print('posição inválida')
    

class main():

    def teste():
        array_queue = Array()
        linked_list_queue = LinkedList()

        print('Array \n\n')

        fifo_array = Fifo(  )
        print(fifo_array.isEmpty())
        fifo_array.enque(5)  #Adicionando 5
        print(fifo_array.size())
        print(fifo_array.isEmpty())
        fifo_array.enque(7) #Adicionando 7
        fifo_array.enque(19) #Adicionando 19
        print(f'Removendo o primeiro da fila: {fifo_array.deque()}') #O 5 deve sair
        print(fifo_array.size())
        print(fifo_array.isEmpty())

        print('\nLinked List \n\n')

        fifo_linked_list = Fifo(linked_list_queue)
        print(fifo_linked_list.isEmpty())
        fifo_linked_list.enque(10) #Adicionando 10
        print(fifo_linked_list.size())
        print(fifo_linked_list.isEmpty())
        fifo_linked_list.enque(2) #Adicionando 2
        fifo_linked_list.enque(21) #Adicionando 21
        print(f'Removendo o primeiro da fila: {fifo_linked_list.deque()}') #O 10 deve sair
        print(fifo_linked_list.size())
        print(fifo_linked_list.isEmpty())


if __name__ == '__main__':
    main.teste()
