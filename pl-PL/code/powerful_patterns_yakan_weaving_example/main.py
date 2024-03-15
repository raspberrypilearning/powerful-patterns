#!/bin/python3

from p5 import *
from math import random


def motif():
    rozmiar_motywu = 100

    # Kolory wątków
    POMARAŃCZOWY = Kolor(254, 96)
    FIOLETOWY = Kolor(135, 18, 192)
    ŻÓŁTY = Kolor(243, 200, 19)
    NIEBIESKI = Kolor(83, 171, 176)

    # Kwadraty
    Fill(POMARAŃCZOWY)
    rect(0, 0, motif_size/2, motif_size/2)
    Fill(FIOLETOWY)
    rect(50, 0, motif_size/2, motif_size/2)
    Wypełnienie(ŻÓŁTY)
    rect(0, 50, motif_size/2, motif_size/2)
    Fill(NIEBIESKI)
    rect(50, 50, motif_size/2, motif_size/2)
    Fill(FIOLETOWY)
    rect(0, 0, motif_size/4, motif_size/4)
    Fill(POMARAŃCZOWY)
    rect(50, 0, motif_size/4, motif_size/4)
    Fill(NIEBIESKI)
    rect(0, 50, motif_size/4, motif_size/4)
    Wypełnienie(ŻÓŁTY)
    rect(50, 50, motif_size/4, motif_size/4)


def rotate_motif():
    for shape in range(5): # wiersz kształtów
        push_matrix() # zapisz ustawienia
        obróć(radiany(45)) # obróć kształt o 45 stopni
        motyw()
        pop_matrix() # wróć do zapisanych ustawień
        translate(motif_width, 0) # przesuń poziomo


def setup():
    size(400, 400)
    tło(250, 5, 94) # różowy
    no_stroke()
    Print('to jest ?? Yakan tkanie ')


def draw():
    global motif_width
    motif_width = 150

    translate(-motif_width/2, -motif_width/2) #, aby rozpocząć od połowy motywów

    if frame_count < 20: # maksymalna liczba rzędów
        dla wiersza w zakresie(frame_count):
            obróć_motif()
            if row / 2 == 0: # aby przesunąć wzór w następnym wierszu
                translate(-motif_width * 5 + 75, 80)
            else:
                translate(-motif_width * 5 - 75, 80)


run(frame_rate=3)
