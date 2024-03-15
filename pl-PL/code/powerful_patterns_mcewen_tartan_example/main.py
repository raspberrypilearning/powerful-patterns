#!/bin/python3

from p5 import *


def setup():
    size(400, 400)


def draw():
    Linie = 10 * frame_count # Użyj w kształcie width/length, aby animować w czasie

    # Kolory tartanowe McEwen
    # Podstawowe kolory kwadratowe
    NIEBIESKI = Kolor(83, 143, 200)
    ZIELONY = Kolor(78, 163, 162)
    BASE_COLOURS = [ZIELONY, NIEBIESKI]

    # Kolory krzyżowe
    ŻÓŁTY = Kolor(155, 176, 135)
    CZERWONY = Kolor(155, 129, 113)
    CROSS_COLOURS = [ŻÓŁTY, CZERWONY]

    # Kolory łączenia i nakładania się
    SZARY = Kolor(78, 99, 86)

    # Rysuj wszystkie ZIELONE i NIEBIESKIE naprzemienne kwadraty bazy
    no_stroke()
    y_coordinate = 0
    kwadraty = szerokość/kwadrat_rozmiar

    for i in range(int(kwadraty)):
        przerwa = 0
        for j in range(int(kwadraty)):
            Fill(BASE_COLOURS[j % 2]) # ZIELONY i NIEBIESKI
            rect(przerwa, y_współrzędna, kwadrat_size, kwadrat_size)
            przerwa = przerwa + kwadrat_size
        y_coordinate = y_coordinate + square_size

    # Krzyże
    Stroke(SZARY)

    # NARYSUJ ŻÓŁTE i CZERWONE krzyże naprzemienne
    for i in range(4):
        Wypełnienie(ŻÓŁTY)
        krzyżyk = kwadrat_size / 2 - 2
        for i in range(int(kwadraty/2)):
            Fill(CROSS_COLOURS[i % 2]) # ŻÓŁTY i CZERWONY
            rect(krzyżyk, 0, 4, linie)
            rect(0, krzyżyk, linie, 4)
            krzyżyk = krzyżyk + 2 * kwadrat_size
        # Rysuj krzyże szwów
        no_fill()
        krzyżyk = kwadrat_size + kwadrat_size / 2 - 2
        for i in range(int(kwadraty)):
            rect(krzyżyk, 0, 4, linie)
            rect(0, krzyżyk, linie, 4)
            krzyżyk = krzyżyk + kwadrat_size

    # Narysuj szare linie, w których materiał się nakłada
    no_stroke()
    Wypełnienie(SZARY, 100)
    przerwa = kwadrat_size - 4
    for i in range(int(kwadraty)):
        rect(przerwa, 0, 8, linie)
        przerwa = przerwa + kwadrat_size
    przerwa = kwadrat_size - 4
    for i in range(int(kwadraty)):
        rect(0, przerwa, linie, 8)
        przerwa = przerwa + kwadrat_size


print('????????????????? To jest McEwen Tartan ??????????? ')
kwadrat_size = int(
    Input('jaki rozmiar ????????? tartan chcesz? 20, 50 lub 100'))

run(frame_rate=10)
