#!/bin/python3

from p5 import *
from random import randint


def motif():
    globalny rozmiar_koła
    for i in range(5):
        elipsa(0, 0, circle_size / 5 * (5 - i), circle_size / 5 * (5 - i))


def setup():
    size(400, 400)
    print('? Ta sztuka używa wielu kręgów!')

    globalny rozmiar_koła

    circle_size = 50


def draw():
    # Kolory wzoru
    stroke(40, 35, 100) # niebieski
    stroke_weight(2) # gruba obwódka
    fill(200, 180, 128) # złoto

    translate(0, 0) # start od lewego górnego rogu ekranu

    jeśli frame_count <= 16: # tworzy 16 wiersze, to zatrzymuje się
        dla wiersza w zakresie(frame_count): # animuje jeden wiersz na raz
            for shape in range(16): # utwórz wiersz motywów
                motyw()
                translate(okrąg_size / 2, 0)
            translate(-width, circle_size / 2) # przesuń w dół, aby rozpocząć następny wiersz


run(frame_rate=3)
