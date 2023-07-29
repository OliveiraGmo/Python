
def voto(a):
    from datetime import date
    b=(date.today().year)-a
    if b >= 16 and b < 69:
        return f'Com {b} anos o VOTO é OBRIGATÓRIO'
    if b >= 70:
        return f'Com {b} anos o VOTO OPCIONAL'
    if b < 16:
        return f'Com {b} anos NÃO PODE VOTAR, ESPERE COMPLETAR 16 ANOS'



a = int(input('Qual a data de nascimento?  '))
print(voto(a))
