#!/bin/python3

from p5 import *
from math import random


def motif():
    motif_size = 100

    # Thread colours
    ORANGE = Color(254, 96, 1)
    PURPLE = Color(135, 18, 192)
    YELLOW = Color(243, 200, 19)
    BLUE = Color(83, 171, 176)

    # Squares
    fill(ORANGE)
    rect(0, 0, motif_size/2, motif_size/2)
    fill(PURPLE)
    rect(50, 0, motif_size/2, motif_size/2)
    fill(YELLOW)
    rect(0, 50, motif_size/2, motif_size/2)
    fill(BLUE)
    rect(50, 50, motif_size/2, motif_size/2)
    fill(PURPLE)
    rect(0, 0, motif_size/4, motif_size/4)
    fill(ORANGE)
    rect(50, 0, motif_size/4, motif_size/4)
    fill(BLUE)
    rect(0, 50, motif_size/4, motif_size/4)
    fill(YELLOW)
    rect(50, 50, motif_size/4, motif_size/4)


def rotate_motif():
    for shape in range(5):  # row of shapes
        push_matrix()  # save settings
        rotate(radians(45))  # turn shape 45 degrees
        motif()
        pop_matrix()  # go back to saved settings
        translate(motif_width, 0)  # move horizontally


def setup():
    size(400, 400)
    background(250, 5, 94)  # pink
    no_stroke()
    print('This is 🇵🇭 Yakan weaving ')


def draw():
    global motif_width
    motif_width = 150

    translate(-motif_width/2, -motif_width/2)  # to start with half motifs

    if frame_count < 20:  # maximum rows
        for row in range(frame_count):
            rotate_motif()
            if row / 2 == 0:  # to offset pattern on next row
                translate(-motif_width * 5 + 75, 80)
            else:
                translate(-motif_width * 5 - 75, 80)


run(frame_rate=3)
