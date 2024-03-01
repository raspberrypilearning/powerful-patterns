#!/bin/python3

from p5 import *
from random import randint


def setup():
    # Zet de code om eenmalig uit te voeren hier onder
    size(400, 400)
    background(255, 255, 255)


def draw():
    # Zet hier code om bij elk frame uit te voeren
    fill(255, 0, 255)
    rect(50, 50, 120, 100)


# Bewaar dit om je code uit te voeren
run(frame_rate=5)
