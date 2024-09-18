#!/bin/python3

from p5 import *
from random import randint


def setup():
    # Розмісти тут код для одноразового запуску
    size(400, 400)
    background(255, 255, 255)


def draw():
    # Помісти тут код для запуску на кожному кадрі
    fill(255, 0, 255)
    rect(50, 50, 120, 100)


# За допомогою цього ти зможеш запустити свій код
run(frame_rate=5)
