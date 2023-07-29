total=f=0
g = 'x'
while True:
    c=str(input('Nome do produto: '))
    preco=float(input('Digite o preço: '))
    r=0
    j='x'
    total+=preco
    if preco > float(1000):
        f+=1
    r+=1
    if r == 1:
        p = preco
        g=c
    if preco < p:
        p=preco
        g=c
    while j not in 'SN':
        j=str(input('Deseja sair: [S/N]')).upper().strip()[0]
    if j =='N':
        continue
    elif j == 'S':
        break
print(f'Foram comprados {f} itens acima de R$1000,o item mais barato foi o {g},e o total gasto foi {total} ')

