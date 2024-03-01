#!/bin/python3

from p5 import *
from random import randint


def teken_motief():
    oranje = Color(191, 64, 191)
    bruin = Color(200, 120, 0)
    groen = Color(100, 155, 0)
    fill(oranje)
    ellipse(200, 200, 200, 190)
    fill(0)
    # Ogen
    ellipse(160, 190, 30, 30)
    ellipse(240, 190, 30, 30)
    fill(255)
    ellipse(165, 200, 10, 10)
    ellipse(245, 200, 10, 10)
    # Mond
    no_fill()
    stroke(255, 255, 255)
    ellipse(150, 250, 30, 30)
    ellipse(250, 250, 30, 30)
    fill(255, 255, 255)
    no_stroke()
    rect(150, 230, 100, 40)
    fill(108, 200, 206)
    rect(152, 235, 96, 30)


def setup():
    size(400, 400)
    background(255)
    no_stroke()


def draw():
    push_matrix()
    # gecompenseerd door de breedte van het kwartgrote gezicht
    translate(randint(-50, 350), randint(-50, 350))
    scale(0.25, 0.25) # kwart grootte paden
    teken_motief()
    pop_matrix()


run(frame_rate=10)
