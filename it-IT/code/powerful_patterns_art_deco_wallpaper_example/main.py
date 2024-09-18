#!/bin/python3

from p5 import *
from random import randint


def motif():
    global circle_size
    for i in range(5):
        ellipse(0, 0, circle_size / 5 * (5 - i), circle_size / 5 * (5 - i))


def setup():
    size(400, 400)
    print('🖌 Quest\'arte utilizza molti cerchi!')

    global circle_size

    circle_size = 50


def draw():
    # Colori del motivo
    stroke(40, 35, 100)  # blu
    stroke_weight(2)  # bordo spesso
    fill(200, 180, 128)  # oro

    translate(0, 0) # inizia dall'angolo in alto a sinistra dello schermo

    if frame_count <= 16: # crea 16 righe quindi si ferma
        for row in range(frame_count): # anima 1 riga alla volta
            for shape in range(16): # crea una fila di temi base
                motif()
                translate(circle_size / 2, 0)
            translate(-width, circle_size / 2) # spostati verso il basso per iniziare la riga successiva


run(frame_rate=3)
