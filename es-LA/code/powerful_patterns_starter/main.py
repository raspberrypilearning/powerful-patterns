#!/bin/python3

from p5 import *
from random import randint


def setup():
    # Ejecuta el código aquí una vez
    size(400, 400)
    background(255, 255, 255)


def draw():
    # Ejecuta el código para cada cuadro aquí
    fill(255, 0, 255)
    rect(50, 50, 120, 100)


# Mantén esto para ejecutar tu código
run(frame_rate=5)
