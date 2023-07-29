a = int(input('Digite um numero para verificar se ele é primo: '))
for c in range(2,a+1):
    if a % c==0:
        print('\33[34m {}'.format(c),end=' ')
    else:
        print('\33[31m {}'.format(c),end=' ')