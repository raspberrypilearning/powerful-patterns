#!/bin/python3

from p5 import *
from random import randint


def setup():
    # Wstaw kod, aby uruchomić go raz tutaj
    size(400, 400)
    background(255, 255, 255)


def draw():
    # Wstaw kod, aby uruchomić każdą klatkę tutaj
    fill(255, 0, 255)
    rect(50, 50, 120, 100)


# Zatrzymaj to, aby uruchomić swój kod
run(frame_rate=5)
