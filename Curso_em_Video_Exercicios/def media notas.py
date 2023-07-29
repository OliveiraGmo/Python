def notas(a=0,b=0,c=0,d=0,e=0,f=0,g=0,sit=False):
    lista={a,b,c,d,e,f,g}
    k=dict()
    k['Total']= len(lista)
    k['Maior']= max(lista)
    k['Menor']= min(lista)
    k['Média']= sum(lista)/len(lista)
    if sit:
        if k['Média']>=6:
            k['Situação']= 'BOA'
        else:
            k['Situação'] = 'RUIM'

    return k
resp =notas(5.5,1.5,3,6.1,sit=True)
print(resp)