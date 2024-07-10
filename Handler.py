from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def eligible():
        pass


class BookAvaliabilityHandler(Handler):
    
    def __init__(self, suc: Handler|None = None) -> None:
        self.sucessor: Handler|None = suc
    
    def eligible(self):
        #code
        ...
        resultado: bool = True

        if self.sucessor and resultado:
            return self.sucessor.eligible()

        else:
            return resultado


class UserEligibilityHandler(Handler):
    
    def __init__(self, suc: Handler|None = None) -> None:
        self.sucessor: Handler|None = suc

    def eligible(self):
        #code
        ...
        resultado: bool = True

        if self.sucessor and resultado:
            return self.sucessor.eligible()

        else:
            return resultado


class LoanLimitHandler(Handler):
    
    def __init__(self, suc: Handler|None = None) -> None:
        self.sucessor: Handler|None = suc

    def eligible(self):
        #code
        ...
        resultado: bool = True

        if self.sucessor and resultado:
            return self.sucessor.eligible()

        else:
            return resultado

