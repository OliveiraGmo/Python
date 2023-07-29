from random import randint
from time import sleep
from operator import itemgetter
ranking=dict()
a={'jogador1': randint(1,6),
   'jogador2': randint(1,6),
   'jogador3': randint(1,6),
   'jogador4': randint(1,6)}

for k, v in a.items():
    print(f'O {k} tirou {v}.')

ranking = sorted(a.items(), key=itemgetter(1),reverse=True)

for c,v in enumerate(ranking):
    print(f'O {c+1}º foi o {v[0]} com {v[1]}')