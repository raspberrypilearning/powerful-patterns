#!/bin/python3

from p5 import *
from math import random
from random import randint


def motif():
    fill(randint(0, 255), randint(0, 255), randint(0, 255))
    ellipse(0, 0, 25, 25)
    fill(0, 0, 0)
    ellipse(0, 0, 15, 15)
    fill(randint(0, 255), randint(0, 255), randint(0, 255))
    for i in range(4): # короткий ряд квадратів
        rect(i * 5, 0, 5, 5)


def setup():
    size(400, 400)
    stroke_weight(2)  # товстий контур
    background(255)


def draw():
    translate(200, 200)  # почати з центру екрана
    if frame_count < 150:
        for i in range(frame_count):  # анімує візерунок
            motif()
            rotate(5)  # обертає мотив
            translate(i, i)  # переміщує мотив


run(frame_rate=10) # швидка анімація
