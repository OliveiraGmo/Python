c=0
while True:
    c = int(input('Digite um número para exibir a sua tabuada:'))
    print('-' * 40)
    if c < 0:
        break
    for d in range(1,11):
        resultado = c*d
        print(f'{d} x {c} = {resultado}')


    print('-' * 40)