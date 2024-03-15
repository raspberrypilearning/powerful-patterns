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
    for i in range(4):  # une courte rangée de carrés
        rect(i * 5, 0, 5, 5)


def setup():
    size(400, 400)
    stroke_weight(2) # bordure épaisse
    background(255)


def draw():
    translate(200, 200) # démarrer depuis le centre de l'écran
    if frame_count < 150:
        for i in range(frame_count): # anime le motif
            motif()
            rotate(5) # tourne le motif
            translate(i, i) # déplace le motif


run(frame_rate=10) # animation rapide
