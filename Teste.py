class teste:

    def __init__(self, num, nome) -> None:
        self.num = num
        self.nome = nome
    
    def __repr__(self) -> str:
        return self.nome + "-" + str(self.num)


banana = teste(5, "Abacaxi")
# abacaxi = {"Aba", "ca", "xi", "dois"}
# for a, b in enumerate(abacaxi, start= 1):
#     print(f'{a}- {b}')
pera = teste(4, "Pera")
uva = teste(7, "Uva")
cereja = teste(8, "Cereja")
caju = teste(5, "Caju")

aba = [banana, pera, uva, cereja, caju]
print("aba") if banana.aba else print('bab')
