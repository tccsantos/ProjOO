from Abstract import Mediator, User, Book


class bookAvaliabilityNotifier(Mediator):

    def __init__(self, users: set[User]|None = None) -> None:
        self.__users: set[User] = users if users != None else set() 
    
    def notify(self, book: Book) -> None:
        for user in self.__users:
            if book.getId() in user.getReservation():
                user.update(book)
    
    def addUsers(self, user: User) -> None:
        self.__users.add(user)
    
    def removeUser(self, user: User) -> None:
        self.__users.discard(user)
