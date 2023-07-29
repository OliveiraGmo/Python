from random import randint
n= (randint(0,5),randint(0,5),randint(0,5),randint(0,5),randint(0,5))
print(n)
for c in n:
    print(c,end='→')
print(f'\nO maior valor é {max(n)} ,e o menor valor é {min(n)}')