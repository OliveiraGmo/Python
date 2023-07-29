idade=dict()
idade['nome']= str(input('Nome: '))
idade['nasc']= int(input('Ano de nasc: '))
idade['ctps']= int(input('Carteira de trabalho: '))
if idade['ctps'] ==0:
    print(idade)
else :
    idade['contr'] = int(input('Ano de Contratação: '))
    idade['salario']= int(input('Salário: R$'))
    idade['idade'] = 2022 - idade["nasc"]
print(idade)
aposentadoria=2022-idade['contr']
if aposentadoria > 34:
    print('Vai se aposentar!')
else:
    print(f'Não ainda faltam {35-aposentadoria} anos.')