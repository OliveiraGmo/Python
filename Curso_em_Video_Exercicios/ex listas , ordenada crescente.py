c = list()
a=0
for k in range(0,5):
    d= int(input('Digite um valor: '))
    if k == 0 or d > c[-1]:
        c.append(d)
        print(c)
    else:
        pos=0
        while pos < len(c):
            print(pos,len(c))
            if d<= c[pos]:
                c.insert(pos,d)
                break
            pos+=1

print(c)
