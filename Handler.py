from abc import ABC, abstractmethod
from Book import LivroUnico
from User import User
from Configuration import ConfigurationManager

from typing import Self


class Handler(ABC):

    def __init__(self, suc: Self|None = None, manager: ConfigurationManager = None) -> None:
        self.sucessor: Handler|None = suc
        self.manager: ConfigurationManager = manager

    @abstractmethod
    def eligible(self, book: LivroUnico, user: User):
        pass


class BookAvaliabilityHandler(Handler):
    
    def eligible(self, book: LivroUnico, user: User):
        #code
        if book.getQuantidade() > 0:
            resultado: bool = True
        else:
            resultado: bool = False

        if self.sucessor and resultado:
            return self.sucessor.eligible(book, user)

        else:
            return resultado


class UserEligibilityHandler(Handler):
        

    def eligible(self, book: LivroUnico, user: User):
        #code
        ...
        resultado: bool = True

        if self.sucessor and resultado:
            return self.sucessor.eligible(book, user)

        else:
            return resultado


class LoanLimitHandler(Handler):

    def eligible(self, book: LivroUnico, user: User):
        #code
        ...
        resultado: bool = True

        if self.sucessor and resultado:
            return self.sucessor.eligible(book, user)

        else:
            return resultado

