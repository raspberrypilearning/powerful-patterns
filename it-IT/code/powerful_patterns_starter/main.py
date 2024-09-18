#!/bin/python3

from p5 import *
from random import randint


def setup():
    # Inserisci qui il codice da eseguire una volta
    size(400, 400)
    background(255, 255, 255)


def draw():
    # Inserisci qui il codice da eseguire ad ogni frame
    fill(255, 0, 255)
    rect(50, 50, 120, 100)


# Istruzione necessaria per eseguire il codice
run(frame_rate=5)
