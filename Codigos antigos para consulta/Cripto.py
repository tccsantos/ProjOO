from random import randint


def cripto(string: str) -> list[str, int]:
    alfabeto = list('abcdefghijklmnopqrstuvwxyz')
    upalfa = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')   
    k = randint(1,25)
    cript = ''
    for letra in string:
        if letra in alfabeto:
            i = alfabeto.index(letra) + k
            cript += alfabeto[i%26]
        elif letra in upalfa:
            if letra in upalfa:
                i = upalfa.index(letra) + k
                cript += upalfa[i%26]
        else:
            cript += letra
    return [cript, k]




cript = input('Escreva a mensagem para ser criptografada: ')
cript, k = cripto(cript)
print(f'mensagem: {cript}\nchave: {k}')




