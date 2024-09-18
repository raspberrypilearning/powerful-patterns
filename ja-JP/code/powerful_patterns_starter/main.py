#!/bin/python3

from p5 import *
from random import randint


def setup():
    # 一度だけ動かしたいコードをこの下に書く
    size(400, 400)
    background(255, 255, 255)


def draw():
    # フレームごとに動かしたいコードをこの下に書く
    fill(255, 0, 255)
    rect(50, 50, 120, 100)


# コードを実行するのに必要
run(frame_rate=5)
