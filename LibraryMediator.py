from abc import ABC, abstractmethod
from Book import Book
from User import User



class Mediator(ABC):
    
    @abstractmethod
    def notify(self, book: Book) -> None:
        pass


class bookAvaliabilyNotifier(Mediator):

    def __init__(self, users: set[User]|None = None) -> None:
        self.__users: set[User] = users if users != None else set() 
    
    def notify(self, book: Book) -> None:
        for user in self.__users:
            if book in user.solicitarReserva:
                user.update(book)
    
    def addUsers(self, user: User) -> None:
        self.__users.add(user)
    
    def removeUser(self, user: User) -> None:
        self.__users.discard(user)