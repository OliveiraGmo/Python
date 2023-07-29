c=('\033[m', #sem cor
    '\033[0;30;41m', #vermelho
    '\033[0;30;42m', #verde
    '\033[0;30;43m',# amarelo
    '\033[0;30;44m',#azul
    '\033[0;30;45m',#roxo
    '\033[7;30m',   #branco
   );

def ajuda(com):
    help(com)

def titulo(msg,cor=0):
    tam =len(msg)+4
    print(c[cor],end='')
    print('~'*tam)
    print(f'{msg}')
    print('~' * tam)
    print(c[0],end='')


comando=''
while True:
    titulo('SISTEMA DE AJUDA PyHELP',5)
    comando=str(input('Função biblioteca >'))
    if comando.upper() =='FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!',0)