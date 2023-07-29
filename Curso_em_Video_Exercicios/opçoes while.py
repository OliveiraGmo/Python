from time import sleep
a=0
b=0
c=0
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo  valor: '))
while c !=5:
    c = int(input('''
                         Selecione uma opção:
                  
                         [1] Para somar
                         [2] Para multiplicar
                         [3] Para mostrar o número maior
                         [4] Para novos numeros
                         [5] Para sair
                     >>>>> Qual a sua opção :    '''))
    if c == 1:
        print('A soma dos numeros é igual {}!'.format(a+b))
    elif c == 2:
        print('A multiplicação dos numeros é igual {}!'.format(a * b))
    elif c == 3:
        if a > b:
            print('O maior número é {}!'.format(a))
        else:
            print('O maior número é {}!'.format(b))
    elif c ==4:
        a = float(input('Digite o primeiro valor: '))
        b = float(input('Digite o segundo  valor: '))
    elif c == 5:
        print('Finalizando o programa')





