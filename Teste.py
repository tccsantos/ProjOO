# from Adapter import csvReader

# class teste:

#     def __init__(self, num, nome) -> None:
#         self.num = num
#         self.nome = nome
    
#     def __repr__(self) -> str:
#         return self.nome + "-" + str(self.num)


# banana = teste(5, "Abacaxi")
# # abacaxi = {"Aba", "ca", "xi", "dois"}
# # for a, b in enumerate(abacaxi, start= 1):
# #     print(f'{a}- {b}')
# pera = teste(4, "Pera")
# uva = teste(7, "Uva")
# cereja = teste(8, "Cereja")
# caju = teste(5, "Caju")

# aba = [banana, pera, uva, cereja, caju]
# print("aba") if banana.aba else print('bab')

# abacaxi = csvReader("./Banco/Books.csv", "./Banco/Users.csv")
# users, books = abacaxi.initialize()
# for user in users:
#     print(user, end= '\n\n')
# for book in books:
#     print(book, end= '\n\n')
#     if book.isComposite():
#         composite = book

# print(composite.getBooks())
import csv



with open("./Banco/BancoTeste/Users.csv", "r", encoding="utf8") as csvfile:
            aba = csv.DictReader(csvfile, delimiter=";", fieldnames=["id", "nome","cpf","nascimento","Reservas","Emprestimos","Type"])
            print(aba)
            abacaxi = dict(aba)
            print(abacaxi)
            for key, item in abacaxi.items():
                print(key, item, sep= ": ")