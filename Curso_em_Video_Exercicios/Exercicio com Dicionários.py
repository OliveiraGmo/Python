pessoa= dict()
galera=list()
soma=media=0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F.')
    pessoa['idade']= int(input('Idade: '))
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp= str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Responda apenas S ou N! ')
    if resp == 'N':
            break
print('=-='*20)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média das pessoas cadastradas é de {media} anos')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoa acima da media',end='')
for p in galera:
    if p['idade'] >=media:
        print('    ')




