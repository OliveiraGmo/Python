c=cont=soma=0
while True:
    c = int(input('Digite um valor para ser somado:'))
    cont+=1
    if c == 999:
            break
    else:
        soma+=c
print(f'Foran somados {cont} numeros, e a soma deles é igual a {soma}!')
