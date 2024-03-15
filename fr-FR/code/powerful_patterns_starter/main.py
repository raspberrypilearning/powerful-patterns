#!/bin/python3

from p5 import *
from random import randint


def setup():
    # Mets le code à exécuter une fois ici
    size(400, 400)
    background(255, 255, 255)


def draw():
    # Mets le code à exécuter une fois ici
    fill(255, 0, 255)
    rect(50, 50, 120, 100)


# Garde ceci pour exécuter ton code
run(frame_rate=5)
