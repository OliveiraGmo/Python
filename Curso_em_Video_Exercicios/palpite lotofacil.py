from random import randint
print('=-='*20)
print('JOGO DA LOTOFACIL!!!')
print('=-='*20)
jogos=int(input('Quantos jogos você quer fazer: '))
a=list()
temp=list()
b=0
while b < jogos:
    while True:
        temp.append(randint(1, 25))
        if temp[0] not in a:
            a+=temp
            temp.clear()
        else:
            temp.clear()
        if len(a) == 15:
            b+=1
            break
    a.sort()
    print(f'Jogo Nº{b},',a)
    a.clear()

print('=-='*10,'Boa Sorte','=-='*10)