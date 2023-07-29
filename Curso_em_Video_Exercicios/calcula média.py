soma =cont=0
sair = str
while sair !='N':
    c= int(input('Digite um número: '))
    sair = str(input('Deseja continuar s/n?')).upper().strip()[0]
    soma+=c
    cont+=1
    if cont ==1:
        maior=c
        menor=c
    else:
        if c > maior:
            maior=c
        if c < menor:
            menor=c

print("Foram somados {} valores, e a soma e igual á {}, o menor número digitado foi {}, e o maior é {}, a média é igual a {}.".format(cont,soma,menor,maior,soma/cont))