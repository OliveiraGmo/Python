from time import sleep

def cont(a, b, c):
    print(f'Contagem de {a} até {b} de {c} em {c}. ')
    print('  ')
    if c == 0:
        c += 1
    elif c <= -1:
        for d in range(a, b + c, c):
            print(d, end=' ')
            sleep(0.5)
    elif b > a:
        for d in range(a, b + 1, c):
            print(d, end=' ')
            sleep(0.5)
    elif a > b:
        d = (c) * -1
        for v in range(a, b, d):
            print(v, end=' ')
            sleep(0.5)


print('=-=' * 20)
print(' ' * 4, ' Contagem de 1 até 10 de 1 em 1')
for n in range(1, 11):
    print(n, end=' ')
print()
print('=-=' * 20)
print(' ' * 4, 'Contagem de 10 até 0 de 2 em 2')
for n in range(10, -2, -2):
    print(n, end=' ')

print('')
print('=-=' * 20)
print('Agora é sua vez de fazer sua contagem')
a = (int(input('inicio: ')))
b = (int(input('Fim: ')))
c = (int(input('passo: ')))
print('=-=' * 20)
cont(a, b, c)