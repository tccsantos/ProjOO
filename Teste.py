class teste:

    def __init__(self, num, nome) -> None:
        self.__num = num
        self.nome = nome
    
    def __repr__(self) -> str:
        return self.nome


#banana = teste(5, "Abacaxi")
# abacaxi = {"Aba", "ca", "xi", "dois"}
# for a, b in enumerate(abacaxi, start= 1):
#     print(f'{a}- {b}')
    
print("a") if 4%2 == 5 else print('b')
