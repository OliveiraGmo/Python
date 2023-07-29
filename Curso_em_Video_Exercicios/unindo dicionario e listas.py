dados= dict()
i=list()
tot =list()
mulher=list()
maior=()
count=0
media=0
for c in range(0,3):
    dados['nome']=str(input('Nome: ')).strip()
    dados['sexo']=str(input('Sexo [M/F]')).strip().upper()
    i.append(int(input('Idade: ')))
    dados['idade'] = i[:]
    count+=1
    media = sum(i)/count
    dados['media']= media
    tot.append(dados.copy())
    if dados['sexo'] == 'F':
        mulher.append(dados.copy())
    if i > media:
        maior.append(dados.copy())


print('=-='*20)
print(f'Foram cadastradas {count} pessoas')
print(f'a média de idade é {dados["media"]}')
print('As mulheres cadastradas foram: ',end='')
c=0
for c in range(c,len(mulher)):
    print(mulher[c]["nome"],end=' ')
