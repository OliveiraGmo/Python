def fac(a):
    from math import factorial
    print(f'o fatorial de {a} é {factorial(a)}')
    i =0
    while i <= a:
        c=a-i
        print(f'{c} x',end='')
        i+=1
print(fac(5))