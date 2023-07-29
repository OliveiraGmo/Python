lista =list()
while True:
    lista.append(int(input('Digite um valor: ')))
    s= str(input('Desenja sair S/N: ')).upper().strip()
    if s not in 'SN':
        s = str(input('Desenja sair S/N: ')).upper().strip()
    if s == 'N':
        continue
    else:
        break
print('=-='*20)
print(f'Foram digitados {len(lista)} números')
print('=-='*20)
lista.sort()
lista.reverse()
print(f'Lista em ordem descrescente {lista}')
print('=-='*20)
if 5 in lista:
    print('O número 5 está na lista...')
else:
    print('O número 5 não está na lista...')