a = int(input('Digite um número para confirmar se ele é primo:'))
cont = 0
num = 0
for c in range(2,a+1):
     if a % c == 0 :
         num += 1

if num > 1:
    print('\33[31mO numero é {}'.format('não é primo'))
else:
    print('\33[32mO numéro é {}'.format('é primo'))

