from random import randint
from time import sleep
jogos=int(input('Quantos jogos você quer fazer: '))
a=list()
temp=list()
b=0
while b < jogos:
    while True:
        temp.append(randint(1, 60))
        if temp[0] not in a:
            a+=temp
            temp.clear()
        else:
            temp.clear()
        if len(a) == 6:
            b+=1
            break
    sleep(1)
    a.sort()
    print(f'Jogo Nº{b},',a)
    a.clear()
