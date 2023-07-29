a = int(input('Digite o primero número: '))
b = int(input('Digite a razão da progressão: '))
r = a + 10* b
for c in range(a,r,b):
    print(c,end=' ')
