'''As funções que recebem o automato e o estado inicial e retornam se faz ou não parte da linguagem.
    Não fiz a interface de receber um automato por um input ou algo do tipo, mas tem exemplos do
    projeto 2 para demonstrar o funcionamento.

    Thiago Cortez - 163997
'''



def delta(aut: list[int], state: str, inp: int) -> int:
    for i in aut:
        if i[2] == state: return i[inp]

def delta_chapeu(aut: list[int], state: str, word: list[int]) -> str:
    if len(word) == 0: return state
    else: 
        return delta(aut, delta_chapeu(aut, state, word[:-1]), word[-1])
    

def automat(aut: list[int], state: str, word: list[int]) -> bool:
    final = delta_chapeu(aut, state, word)
    for i in aut:
        if i[2] == final: return i[3]



aut_teste = [['A','B','A',True],['C','D','B',False],['E','A','C',False],['B','C','D',False],['D','E','E',False]] # L{w|w possui valor binário divisível por 5}

aut_teste2 = [['A','B','A',False],['A','C','B',False],['D','C','C',False],['A','E','D',False],['A','C','E',True]]# L{w|w termina em 1101}

string_true = [1,0,0,0,1,1]

string_false = [0,1,0,1,1,0,1,1]

string2_false = [0,1,0,1,1,0,0,1]

string2_true = [0,1,1,1,0,1,1,0,1]

print(automat(aut_teste, 'A', string_true))

print(automat(aut_teste, 'A', string_false))

print(automat(aut_teste2, 'A', string2_true))

print(automat(aut_teste2, 'A', string2_false))


