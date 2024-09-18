#!/bin/python3

from p5 import *
from random import randint


def setup():
    # Βάλε εδώ κώδικα που θα εκτελεστεί μια φορά
    size(400, 400)
    background(255, 255, 255)


def draw():
    # Βάλε εδώ κώδικα που θα εκτελείται σε κάθε καρέ
    fill(255, 0, 255)
    rect(50, 50, 120, 100)


# Από εδώ εκτελείς τον κώδικά σου
run(frame_rate=5)
