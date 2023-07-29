lista=list()
d=list()
while True:
    a=str(input('Nome: '))
    lista.append(a)
    b=int(input('Nota 1: '))
    lista.append(b)
    c=int(input('Nota 2: '))
    lista.append(c)
    d.append(lista[:])
    lista.clear()
    sair=str(input('Deseja sair: S/N: ')).upper().strip()
    if sair == 'N':
        continue
    else:
        break
print('=-='*20)
print('''No.    NOME           media''')
cont=0
for a in d:
    print(cont,end=' ')
    print('''    ''',end=' ')
    print( a[0],end='')
    cont+=1
    print('''           ''',end='')
    media=(a[1]+a[2]) / 2
    print(media)
    print('=-=' * 20)
while True:
    aluno=(int(input('Mostrar notas de qual aluno: ')))
    print(f'As notas de {d[aluno][0]} são {d[aluno][1:]} ')
    if aluno ==999:
        break
    if aluno not in d:
        continue