#def cad(a,b):
#    if len(a) <= 0:
#        a='<desconhecido>'
#    if len(b) <= 0:
#        b= '0'
#    return f'O nome do jogador é {a} e o número de gols é {b}'


#a=str(input('Nome do jogador: '))
#b=str(input('Numero de gols: '))
#print(cad(a,b))


def ficha(jog='<desconhecido>', gol=0):
    print( f'O nome do jogador é {jog} e o número de gols é {gol}')


n=str(input('Nome do jogador: '))
g=str(input('Numero de gols: '))
if g.isnumeric():
    g= int(g)
else:
    g=0
if n.strip()=='':
    ficha(gol=g)
else:
    ficha(n,g)

