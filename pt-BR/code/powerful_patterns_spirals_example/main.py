from p5 import *
from math import random
from random import randint


def motivo():
    fill(randint(0, 255), randint(0, 255), randint(0, 255))
    ellipse(0, 0, 25, 25)
    fill(0, 0, 0)
    ellipse(0, 0, 15, 15)
    fill(randint(0, 255), randint(0, 255), randint(0, 255))
    for i in range(4):  # uma pequena fileira de quadrados
        rect(i * 5, 0, 5, 5)


def setup():
    size(400, 400)
    stroke_weight(2)  # borda grossa
    background(255)


def draw():
    translate(200, 200)  # comece do centro da tela
    if frame_count < 150:
        for i in range(frame_count):  # anima o padrão
            motivo()
            rotate(5)  # vira o motivo
            translate(i, i)  # move o motivo


run(frame_rate=10) # animação rápida
