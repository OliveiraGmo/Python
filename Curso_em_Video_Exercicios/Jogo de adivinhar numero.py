import random
x= random.randint(1,10)
c= int(input('Adivinhe o numero qu eo computador pensou:'))
b= 1
while c !=x:
    c = int(input("Errrrou , tente novamente :"))
    b+=1

print('O número sorteado foi {}  e você levou {} tentativas para acertar!!! '. format(x,b))
