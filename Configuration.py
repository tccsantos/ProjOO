from Abstract import ConfigurationManager, User



class LibraryManager(ConfigurationManager):

    def __init__(self, loanlimit: dict[str, int], MultipleLimit: dict[str, int]) -> None:
        self.__LoanLimit = loanlimit
        self.__MultipleLimit = MultipleLimit

    def getLoanLimit(self, user: User) -> int|None:
        return self.__LoanLimit.get(user.isType())
    
    def getMultipleLimit(self, user: User) -> int|None:
        return self.__MultipleLimit.get(user.isType())
    
    def setLoanLimit(self, userType: str, newLimit: int, newUserType: bool = False) -> None:
        if self.__LoanLimit.get(userType) != None:
            self.__LoanLimit[userType] = newLimit
        elif newUserType:
            self.__LoanLimit[userType] = newLimit
        else:
            print("Verifique as informações enviadas!\n")

    def setMultipleLimit(self, userType: str, newLimit: int, newUserType: bool = False) -> None:
        if self.__MultipleLimit.get(userType) != None:
            self.__MultipleLimit[userType] = newLimit
        elif newUserType:
            self.__MultipleLimit[userType] = newLimit
        else:
            print("Verifique as informações enviadas!\n")
    