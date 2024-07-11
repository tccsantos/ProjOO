from abc import ABC, abstractmethod
from User import User


class ConfigurationManager(ABC):

    @abstractmethod
    def getLoanLimit(self, user: User):
        pass

    @abstractmethod
    def getDelayLimit(self, user: User):
        pass


class PropertyManager(ConfigurationManager):

    def __init__(self, loanlimit: int, delayLimit: int) -> None:
        self.__studentLoanLimit = loanlimit
        self.__teacherLoanLimit = loanlimit *3
        self.__delayLimit = delayLimit
    
    def getLoanLimit(self, user: User) -> int|None:
        match user.isType():

            case "Student":
                return self.__studentLoanLimit

            case "Teacher":
                return self.__teacherLoanLimit
            
            case _:
                return None

    def getDelayLimit(self, user: User):
        match user.isType():

            case "Student":
                return self.__delayLimit

            case "Teacher":
                return self.__delayLimit
            
            case _:
                return None


    
