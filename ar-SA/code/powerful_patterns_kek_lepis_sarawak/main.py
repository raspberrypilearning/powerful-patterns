#!/bin/python3

from p5 import *
from time import *

# Based on the amazing Malaysian geometric cake art: Kek lapis Sarawak


def quadrant():
    # اختر بعض الألوان الرائعة لطبقات الكيك
    turquoise = Color(64, 224, 208)
    gold = Color(255, 215, 0)
    tomato = Color(255, 99, 71)

    # المربى تلتصق الطبقات ببعضها البعض
    jam = Color(255, 165, 0)
    stroke(jam)
    stroke_weight(2)  # Change the number to change the amount of jam

    # تسع طبقات من الكيك بتكرار 3 ألوان 3 مرات
    for i in range(3):
        start_y = i * 60  # height of 3 blocks of cake
        fill(turquoise)
        rect(0, start_y, 180, 20)
        fill(gold)
        rect(0, start_y + 20, 180, 20)
        fill(tomato)
        rect(0, start_y + 40, 180, 20)


def outer():
    # الكعكة ملفوفة في طبقة خارجية
    yellowgreen = Color(154, 205, 50)

    no_fill()  # Don't cover up the cake quadrants!
    stroke(yellowgreen)
    stroke_weight(20)
    rect(10, 10, 380, 380, 20)


def setup():
    size(400, 400)  # make the cake square
    background(255, 255, 255, 0)  # transparent background


def draw():
    # حدد ربع دورة حتى يسهل قراءة التعليمات البرمجية الخاص بنا
    quarter = radians(90)

    translate(200, 200)  # start from the center

    # اصنع الربع الأيمن السفلي من الكعكة ثم قم بتدوير الأرباع الأخرى

    if frame_count <= 4:  # draw up to 4 quadrants
        for i in range(frame_count):
            quadrant()
            rotate(quarter)

    if frame_count == 5:  # add the outer layer
        translate(-200, -200)  # back to the top corner
        outer()  # outer layer


run(frame_rate=5)  # 5 frames per second
