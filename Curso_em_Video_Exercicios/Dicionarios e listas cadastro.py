jogador = dict()
dados = list()
gol = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, jogador['partidas']):
        gols = int(input(f'Quantos gols na partida {c + 1} ? '))
        gol.append(gols)
    jogador['gols'] = gol
    jogador['total'] = sum(gol)
    dados.append(jogador.copy())

    sair = str(input('Deseja continuar [S/N]? ')).upper()[0]
    while sair not in 'SN':
        sair = str(input('Deseja continuar [S/N]? ')).upper()[0]
    if sair == 'N':
        break
    if sair == 'S':
        continue

print('=-=' * 20)
print('Cod',end=' ')
for i in jogador.keys():
    print(f'{i:<15}',end=' ')
print()
for c, v in enumerate(dados):
    print(c,end=' ')
    for d in v.values():
        print(f'{str(d):<17}',end='')


print()
print('=-=' * 20)
print()
