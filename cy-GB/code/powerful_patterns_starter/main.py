#!/bin/python3

from p5 import *
from random import randint


def setup():
    # Rhowch god i redeg unwaith yma
    size(400, 400)
    background(255, 255, 255)


def draw():
    # Rhowch god i redeg ym mhob ffrâm yma
    fill(255, 0, 255)
    rect(50, 50, 120, 100)


# Cadwch hwn i redeg eich cod
run(frame_rate=5)
