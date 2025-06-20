#!/bin/python3

from p5 import *
from random import randint


def setup():
    # Füge hier den Code ein, der einmal ausgeführt werden soll
    size(400, 400)
    background(255, 255, 255)


def draw():
    # Füge hier den Code ein, der bei jedem Frame ausgeführt werden soll
    fill(255, 0, 255)
    rect(50, 50, 120, 100)


# Lass dies so stehen, um deinen Code auszuführen
run(frame_rate=5)
