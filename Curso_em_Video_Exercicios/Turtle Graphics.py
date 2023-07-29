from time import sleep
import emoticon

import turtle


def jump(t, x, y):
    'faz tartaruga saltar para coordenadas (x, y)'
    t.penup()
    t.goto(x, y)
    t.pendown()
    sleep(1)

sleep(1)
s = turtle.Screen()
sleep(1)
t = turtle.Turtle()

def emoticon(t, x, y):

    'tartaruga t desenha uma carinha com queixo na coordenada (x, y)'
    sleep(1)# define direção da tartaruga e tamanho da caneta
    t.pensize(3)
    sleep(1)
    t.setheading(0)
    sleep(1)# move para (x, y) e desenha cabeça
    jump(t, x, y)
    sleep(1)
    t.circle(100)
    sleep(1)# desenha olho direito
    jump(t, x + 35, y + 120)
    sleep(1)
    t.dot(25)
    sleep(1)# desenha olho esquerdo
    jump(t, x - 35, y + 120)
    sleep(1)
    t.dot(25)
    sleep(1)
    # desenha sorriso
    jump(t, x - 60.62, y + 65)
    sleep(1)
    t.setheading(-60)  # sorriso está em 120 graus
    sleep(1)
    t.circle(70, 120)  # seção de um círculo
    sleep(1)
