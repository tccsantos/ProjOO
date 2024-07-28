from Abstract import ExternalCatalogAdapter, User, Book
from Book import SingleBook, CompositionBook
from User import TeacherUserType, StudentUserType
import pandas as pd
import csv


#Baseando-se no Design Pattern Adapter, essa classe seria o Adapter, aqui nós implementamos o Object Adapter
class csvReader(ExternalCatalogAdapter):
    
    def __init__(self, bookPath: str, userPath: str) -> None:
        self.bookPath: str = bookPath
        self.userPath: str = userPath

    def __transformaInt(_value: str) -> int:
        return(int(float(_value)))
            
    def initialize(self) -> tuple[set[User], set[Book]]:
        with open(self.userPath, "r", encoding="utf8") as arquivo:
            aba = csv.reader(arquivo, delimiter=";")
            next(aba, None)
            rawUsers = list(aba)
        
        with open(self.bookPath, "r", encoding="utf8") as arquivo:
            aba = csv.reader(arquivo, delimiter=";")
            next(aba, None)
            rawBooks = list(aba)

        users = set()
        books = set()

        _ids = {}
        for i in range(len(rawBooks)):
            _ids[i+1] = 0
        

        for user in rawUsers:
            reserve = None if user[4] == "None" or user[4] == "" else set(map(csvReader.__transformaInt, user[4].split(",")))
            loan = None if user[5] == "None" or user[5] == "" else list(map(csvReader.__transformaInt, user[5].split(",")))
            if loan!=None:
                for _id in loan:
                    _ids[_id] += 1
                
            if user[6] == "Teacher":
                sup = TeacherUserType(user[1], user[2], user[3], self,reserve, loan)
            elif user[6] == "Student":
                sup = StudentUserType(user[1], user[2], user[3], self, reserve, loan)
            else:
                raise KeyError
            
            users.add(sup)

        catalog = list()
        single: set[Book] = set()

        for book in rawBooks:

            if book[1] == "True":
                catalog.append(book)
                #sup = CompositionBook(book[2], int(book[0]), set(book[5].split()))
            elif book[1] == "False":
                sup = SingleBook(book[2], int(book[0]), book[4],int(book[3]))
                for i in range(_ids[int(book[0])]):
                    sup.removeAvaliable()
            else:
                raise KeyError
            
            #books.add(sup)
            single.add(sup)
        
        for book in catalog:
            ids = map(int, book[5].split(','))
            comp = set()
            for num in ids:
                for unique in single:
                    if num == unique.getId():
                        comp.add(unique)
            
            sup = CompositionBook(book[2], int(book[0]), comp)
            books.add(sup)
        
            


        return users, books
    
    def addLoan(self, user: User, idBook: int) -> None:
        _data = pd.read_csv(self.userPath, delimiter=";")


        _data["Emprestimos"] = _data.apply(lambda row: (str(idBook) if str(row["Emprestimos"])=="nan" else str(row["Emprestimos"] if type(row["Emprestimos"])!=float else int(row["Emprestimos"]))+","+str(idBook)) if str(row["cpf"]) == user.getCpf() else row["Emprestimos"], axis=1)
        
        _data.to_csv(self.userPath, sep=";", index=False)
    
    def returnLoan(self, user: User, idBook: int) -> None:
        _data = pd.read_csv(self.userPath, delimiter=";")
        row_info = list(_data[ _data["cpf"] == int(user.getCpf())]["Emprestimos"])
        try:
            loan = list(row_info[0])
        except:
            loan = row_info
        if (len(loan)<2): loan = ""
        else:
            try:
                _index = loan.index(str(idBook))
            except:
                return
            if (_index==(len(loan)-1)):
                loan.pop(_index)
                loan.pop(_index-1)
            else:
                loan.pop(_index)
                loan.pop(_index)
        loan = ''.join(loan)
        _data["Emprestimos"] = _data.apply(lambda row: (loan) if str(row["cpf"]) == user.getCpf() else row["Emprestimos"], axis=1)

        _data.to_csv(self.userPath, sep=";", index=False)

    def addReserve(self, user: User, idBook: int) -> None:
        _data = pd.read_csv(self.userPath, delimiter=";")
        
        _data["Reservas"] = _data.apply(lambda row: (str(idBook) if str(row["Reservas"])=="nan" else str(row["Reservas"] if type(row["Reservas"])!=float else int(row["Reservas"]))+","+str(idBook)) if str(row["cpf"]) == user.getCpf() else row["Reservas"], axis=1)

        _data.to_csv(self.userPath, sep=";", index=False)
    
    def removeReserve(self, user: User, idBook: int) -> None:
        _data = pd.read_csv(self.userPath, delimiter=";")
        row_info = list(_data[ _data["cpf"] == int(user.getCpf())]["Reservas"])
        try:
            reserve = list(row_info)
        except:
            reserve = row_info
        if (len(reserve)<2): reserve = ""
        else:
            try:
                _index = reserve.index(str(idBook))
            except:
                return
            if (_index==(len(reserve)-1)):
                reserve.pop(_index)
                reserve.pop(_index-1)
            else:
                reserve.pop(_index)
                reserve.pop(_index)
        reserve = ''.join(reserve)

        _data["Reservas"] = _data.apply(lambda row: (reserve) if str(row["cpf"]) == user.getCpf() else row["Reservas"], axis=1)
        
        _data.to_csv(self.userPath, sep=";", index=False)
