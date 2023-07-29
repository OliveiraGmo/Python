lista =list()
p=list()
i=list()

while True:
    d=(int(input('Digite um valor: ')))
    lista.append(d)
    s= str(input('Desenja sair S/N: ')).upper().strip()
    if d % 2 == 0:
        p.append(d)
    elif d % 2==1:
        i.append(d)
    if s not in 'SN':
        s = str(input('Desenja sair S/N: ')).upper().strip()
    if s == 'N':
        continue
    else:
        break

print(f'A lista completa é {lista}')
print(f'A lista de numeros pares é {p}')
print(f'A lista de numeros impares é {i}')

