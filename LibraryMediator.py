from abc import ABC, abstractmethod
from Book import Book
from User import User



class Mediator(ABC):
    
    @abstractmethod
    def notify(self, book: Book) -> None:
        pass


class bookAvaliabilyNotifier(Mediator):

    def __init__(self, users: set|None = None) -> None:
        self.__users = users if users != None else set() 
    
    def notify(self, book: Book) -> None:
        ...
    
    def addUsers(self, user: User) -> None:
        self.__users.add(user)
    
    def removeUser(self, user: User) -> None:
        self.__users.discard(user)