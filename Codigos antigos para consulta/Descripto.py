

def cripto(string: str, k: int) -> list[str, int]:
    alfabeto = list('abcdefghijklmnopqrstuvwxyz')
    upalfa = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')   
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
    return cript


cript = input('Escreva a mensagem para ser descriptografada: ')

for k in range(26):
    cript= cripto(cript, k)
    print(f'mensagem: {cript}\nchave: {26 - k}\n')
