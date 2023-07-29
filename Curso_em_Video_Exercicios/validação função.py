def leiaint(txt):
    while True:
        a=input(txt)
        if a.isalnum():
            return a
        print('\33[31m ERRO! Digite um numero inteiro!!')





n=leiaint('\33[38m Digite um numero: ')
print(f'\33[36m Você acabou de digitar o número {n}')