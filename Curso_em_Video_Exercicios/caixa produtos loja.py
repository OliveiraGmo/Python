d=maior=menor=j=r=0
g=''
print('-' * 20)
print('Loja de Embalagens')
while True:
    print('-' * 20)
    c = str(input('Nome do Produto: ')).strip()
    d = float(input('Preço R$:'))
    j+= d
    r+=1
    if r == 1:
        menor = d
        g=c
    if d < menor:
      menor=d
      g=c
    s=' '
    while s not in ('SN'):
        s=str(input('Deseja sair? [S/N]')).upper().strip()[0]
    if s == 'N':
       continue
    if s =='S':
       break
print(f"O Valor total das compras foi: R${j}, o produto mais barato foi {g} por R${menor:2}")
print('Acabou')
