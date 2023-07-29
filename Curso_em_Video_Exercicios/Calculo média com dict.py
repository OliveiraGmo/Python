lista = dict()
lista['aluno'] = str(input('Nome: '))
lista['media'] = float(input('Média: '))
print(f'O nome do aluno é {lista["aluno"]}, e a média dele é {lista["media"]}')
if lista['media'] >= 7:
    print(f'{lista["aluno"]} foi aprovado')
else:
    print(f'{lista["aluno"]} foi reprovado')