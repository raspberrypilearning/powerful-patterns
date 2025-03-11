from p5 import *
from math import random
from random import randint


def motief():
    fill(randint(0, 255), randint(0, 255), randint(0, 255))
    ellipse(0, 0, 25, 25)
    fill(0, 0, 0)
    ellipse(0, 0, 15, 15)
    fill(randint(0, 255), randint(0, 255), randint(0, 255))
    for i in range(4): # een korte rij vierkanten
        rect(i * 5, 0, 5, 5)


def setup():
    size(400, 400)
    stroke_weight(2) # dikke rand
    background(255)


def draw():
    translate(200, 200) # start vanaf de linkerbovenhoek van het scherm
    if frame_count < 150:
        for i in range(frame_count): # animeert het patroon
            motief()
            rotate(5) # draait het motief
            translate(i, i) # verplaatst het motief


run(frame_rate=10) # snelle animatie
