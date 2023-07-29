jogador = dict()
partidas= list()
time=list()
while True:

    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    for c in range(0,tot):
            partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total']= sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input(f' Quer continuar?   [S/N] ')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('=-=' * 30)
print('Cod', end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
for k ,v in enumerate(time):
    print(f'{k:>3}',end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('=-='*30)
while True:
    busca=int(input('Qual jogador você quer buscar? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! nao exite jogador com o código {busca} !')
    else:
        print(f'Levantamento do Jogador {time[busca]["nome"]}')
        for i , g in enumerate(time[busca]['gols']):
            print(f' no jogo {i+1} fez {g} gols')
print('=-=' * 30)