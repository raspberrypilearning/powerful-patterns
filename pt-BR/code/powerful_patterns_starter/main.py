#!/bin/python3

from p5 import *
from random import randint


def setup():
    # Coloque o código para ser executado uma vez aqui
    size(400, 400)
    background(255, 255, 255)


def draw():
    # Coloque o código para executar em cada quadro aqui
    fill(255, 0, 255)
    rect(50, 50, 120, 100)


# Mantenha isto para executar seu código
run(frame_rate=5)
