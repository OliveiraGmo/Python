def vertical(n):
    if n < 10:
        print(n)
    else:
        vertical(n //10)
        print(n%10)

def reverse(n):
    if n <10:
        print(n)
    else:
        print(n%10)
        reverse(n//10)

def cherrs(a):
    if a == 0:
        print('Hurrah!!!')
    else:
        print('Hip '*a,'Hurrah!!!')

cherrs(4)


