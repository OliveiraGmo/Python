print('=-='*10)
print('Vamos jogar par ou impar')
print('=-='*10)
c=f=j=0
from random import randint
while True:
    c = int(input('Escolha um número: '))
    d = str(input("Par ou impar: ")).upper().strip()[0]
    print('-'*20)
    f = randint(0,10)
    j=c+f
    if j % 2 == 0:
        print(f'Você jogou {c} e o computador {f}. Total de {c + f} DEU PAR')
        print('-'*20)
        if d == 'P':
            print('Voce  ganhou')
            print('-' * 20)
        if d != 'P':
            print('Voce perdeu')
            print('-' * 20)
    else:
        print(f'Você jogou {c} e o computador {f}. Total de {c + f} DEU IMPAR')
        print('-' * 20)
        if d == 'I':
            print('Voce  ganhou')
            print('-' * 20)
        if d !='I':
            print('Voce perdeu')
            print('-' * 20)
