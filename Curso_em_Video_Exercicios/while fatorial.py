n =int(input('Digite um numero a ser fatorado:  '))
c=n
d = 1
while c > 0:
    print('{}'.format(c),end=" ")
    print('x ' if c>1 else '=',end="")
    d*=c
    c-=1

print(' {}'.format(d))