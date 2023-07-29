temp = list()
t = list()
g =[]
d =[]
maior = menor =  0
for c in range(0 , 3):
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if c == 0 :
        maior = temp[1]
        menor= temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    t.append(temp[:])
    temp.clear()
print(f'Ao todo, voce cadastrou {len(t)} pessoas')
print(f'O maior peso foi de {maior}kg. Peso de ',end='')
for p in t:
    if p[1] == maior:
        print( p[0],end='')
print()
print(f'O menor peso foi de {menor}kg. Peso de ',end='')
for p in t:
      if p[1] == menor:
          print(f'{p[0]}')

