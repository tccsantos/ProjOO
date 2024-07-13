from abc import ABC, abstractmethod
from Book import SingleBook
from User import User
from Configuration import ConfigurationManager

from typing import Self


class Handler(ABC):

    def __init__(self, suc: Self|None = None, manager: ConfigurationManager = None) -> None:
        self.successor: Handler|None = suc
        self.manager: ConfigurationManager = manager

    @abstractmethod
    def eligible(self, book: SingleBook, user: User):
        pass


class BookAvaliabilityHandler(Handler):
    
    def eligible(self, book: SingleBook, user: User):
        #code
        if book.getQuantity() > 0:
            result: bool = True
        else:
            result: bool = False

        if self.sucsessor and result:
            return self.suscessor.eligible(book, user)

        else:
            return result


class UserEligibilityHandler(Handler):
        

    def eligible(self, book: SingleBook, user: User):
        #code
        total = self.manager.getMultipleLimit(user)
        i = 0
        for item in user.getLoan():
            if item == book:
                i +=1
        if i >= total:
            result: bool = False
        else:
            result: bool = True

        if self.successor and result:
            return self.successor.eligible(book, user)

        else:
            return result


class LoanLimitHandler(Handler):

    def eligible(self, book: SingleBook, user: User):
        #code
        total = self.manager.getLoanLimit(user)
        if len(user.getLoan()) >= total:
            result: bool = False
        else:
            result: bool = True

        if self.successor and result:
            return self.successor.eligible(book, user)

        else:
            return result
