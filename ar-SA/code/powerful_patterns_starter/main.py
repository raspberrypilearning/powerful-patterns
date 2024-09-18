#!/bin/python3

from p5 import *
from random import randint


def setup():
    # ضع الشفرة البرمجية للتشغيل مرة واحدة هنا
    size(400, 400)
    background(255, 255, 255)


def draw():
    # ضع الشفرة البرمجية لتشغيل كل إطار هنا
    fill(255, 0, 255)
    rect(50, 50, 120, 100)


# احتفظ بهذا لتشغيل التعليمات البرمجية الخاصة بك
run(frame_rate=5)
