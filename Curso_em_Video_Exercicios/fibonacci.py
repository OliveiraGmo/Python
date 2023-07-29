c= int(input("Digite quantos termos você quer ver: "))
n=0
t1=0
t2=1
t3=0
while n < c:
    t3=t1+t2
    n+=1
    print(t3,end=' ')
    t1=t2
    t2=t3