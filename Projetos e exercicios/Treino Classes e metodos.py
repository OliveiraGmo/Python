
class pessoa():
    def __init__(self,nome,idade,altura):
        self.nome=nome
        self.idade=idade
        self.altura=altura
    
    def altura(self):
        if altura >= 180:
            print(f"Uau acima da média, você é alto") 
        else:
            print(f"Abaixo da média, você não é alto!") 

class imc():
    def __init__(self):
        altura = int(input("Digite sua altura:"))
        peso = int(input("Qual o seu peso?"))
        calc = peso/(altura*altura)
        calc=(calc*10000)
        calc = peso/(altura*altura)
        calc=(calc*10000)
        calc=int(calc)
        d = calc
        if d <= 18:
            print(f'o IMC é {d}, Abaixo do peso')
        elif d >= 19 and d <= 24:
            print(f'o IMC é {d}, Peso ideal parabens')
        elif d > 24 and d < 30:
            print(f'o IMC é {d}, Levemente acima do peso')
        elif d > 30 and d < 35:
            print(f'o IMC é {d}, obesidade grau I')
        elif d > 35 and d < 40:
            print(f'o IMC é {d}, obesidade severa')        
        elif d > 40:
            print(f'o IMC é {d}, obesidade morbida')        
    
       
#imc()
a=pessoa("gabriel",34,172)
a.altura()










