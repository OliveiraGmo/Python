def cabeçalho():
    print('=-='*30)
    print( ' '*30, ' Controle de terreno')
    print('=-=' * 30)
def area():

    l=int(input('Largura (m): '))
    c=int(input('Comprimento (m): '))
    a = l * c
    print(f'área de um terreno é {l} x {c} é de {a}m².')
cabeçalho()
area()

