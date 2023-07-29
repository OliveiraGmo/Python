a=list()
b=list()
c=list()
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
