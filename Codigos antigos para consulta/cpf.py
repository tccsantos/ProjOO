from random import randint


def verifica(cpf: list[int]) -> bool:
    igual = True
    iguais = [cpf[0]]
    for valor in range(1, len(cpf)):
        if cpf[valor] not in iguais:
            igual = False
            break
    if igual:
        return False
    index = 0
    soma = 0
    for i in range(10,1, -1):
        soma += cpf[index]*i
        index += 1
    avalia = soma %11
    #print(avalia)
    if avalia <= 1 and cpf[9] != avalia:
        return False
    elif avalia > 1 and cpf[9] != 11 - avalia:
         return False
    index = 0
    soma = 0
    for i in range(11,1, -1):
        soma += cpf[index]*i
        index += 1
    avalia = soma %11
    #print(avalia)
    if avalia <= 1 and cpf[10] != avalia:
        return False
    elif avalia > 1 and cpf[10] != 11 - avalia:
         return False
    return True


def gera() -> list[int]:
    cpf = []
    for _ in range(9):
        valor = randint(0,9)
        cpf.append(valor)
    index = 0
    soma = 0
    for i in range(10,1, -1):
        soma += cpf[index]*i
        index += 1
    avalia = soma %11
    if avalia <= 1:
        cpf.append(avalia)
    else:
        cpf.append(11-avalia)
    index = 0
    soma = 0
    for i in range(11,1, -1):
        soma += cpf[index]*i
        index += 1
    avalia = soma %11
    if avalia <= 1:
        cpf.append(avalia)
    else:
        cpf.append(11-avalia)
    return cpf
    


raw = gera()
for i in raw: print(i, end='')
cpf = [int(i) for i in raw]
print()
print(verifica(cpf))
