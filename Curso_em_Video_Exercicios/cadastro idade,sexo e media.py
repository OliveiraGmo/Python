mulher=homem=maior=menor=menorfemea=0
while True:
    print('-'*20)
    print('Vamos cadastrar pessoes')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo =' '
    while sexo not in 'MF':
        sexo = str(input( 'Sexo: [M/F]')).upper().strip()[0]
    if sexo =='M':
        mulher+=1
    else:
        homem+=1
    if idade>18:
        maior+=1
    else:
        menor+=1
    if idade < 18 and sexo =='F':
        menorfemea+=1
    cont=' '
    while cont not in 'SN':
        cont= str(input('Deseja continuar: [S/N]')).upper().strip()[0]
    if cont == 'S':
        continue
    else:
        break
print('-'*20)
print(f"A quantidade de homens foi de {homem}, a quantidades de mulheres foi de {mulher}, e a quantidade de mulheres menor de idade é igual {menorfemea}")
print('-'*20)
print('Acabou')