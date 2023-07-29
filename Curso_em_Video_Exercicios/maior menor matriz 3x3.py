a=list()
b=list()
c=list()
soma=list()
for d in range(0,3):
    a.append(int(input(f'Digite um valor para [0,{d}]: ')))
for d in range(0, 3):
    b.append(int(input(f'Digite um valor para [1,{d}]: ')))
for d in range(0, 3):
    c.append(int(input(f'Digite um valor para [2,{d}]: ')))
print('=-='*20)
print(f'[ {a[0]} ] [ {a[1]} ] [ {a[2]} ]')
print(f'[ {b[0]} ] [ {b[1]} ] [ {b[2]} ]')
print(f'[ {c[0]} ] [ {c[1]} ] [ {c[2]} ]')
print('=-='*20)
soma=a[:]+b[:]+c[:]
par=0
for p in soma:
    if p % 2==0:
        par+=p
print(f'A soma dos valores pares é: {par}.')
ter=0
ter=a[2]+b[2]+c[2]
print(f'A soma da terceira coluna é {ter}.')
maior=0
for t in b:
    if t > maior:
        maior=t
print(f'O maior número da terceira linha é {maior}')
