sexo = str(input(' Informe o seu sexo M ou F :')).upper().strip()[0]
while sexo not in'MF':
    sexo= str(input('Invalido, digite novamente: ')).upper().strip()[0]
# Quando voce coloca aspas em not in , ele le como se fosse uma lista o s dados digitados
# e tambem com upper vc maximixa automaticamente as letras, strip tira os espaços e o colchete seleciona a letra
print('O sexo selecionado foi {}!'.format(sexo))

