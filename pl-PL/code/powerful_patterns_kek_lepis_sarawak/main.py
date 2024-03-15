#!/bin/python3

from p5 import *
from time import *

# Na podstawie niesamowitej sztuki malezyjskiego geometrycznego ciasta: Kek lapis Sarawak


def kwadrant():
    # Wybierz kilka wspaniałych kolorów dla warstw ciasta
    Turkus = Kolor(64, 224, 208)
    Złoto = Kolor(255, 215, 0)
    Pomidor = Kolor(255, 99, 71)

    # Zacięcie skleja warstwy razem
    Zacięcie = Kolor(255, 165, 0)
    skok(zacięcie)
    Stroke_weight(2) # Zmień liczbę, aby zmienić ilość zacięcia

    # Dziewięć warstw ciasta, powtarzając 3 kolory 3 razy
    for i in range(3):
        start_y = i * 60 # wysokość 3 bloków ciasta
        wypełnienie(turkusowy)
        rect(0, start_y, 180, 20)
        fill(złoto)
        rect(0, start_y + 20, 180, 20)
        fill(pomidor)
        rect(0, start_y + 40, 180, 20)


def outer():
    # Ciasto jest owinięte w zewnętrzną warstwę
    Żółtozielony = Kolor(154, 205, 50)

    No_fill() # nie zakrywaj kwadrantów ciasta!
    stroke(żółto-zielony)
    stroke_weight(20)
    rect(10, 10, 380, 380, 20)


def setup():
    rozmiar(400, 400) # zrób ciasto kwadratem
    tło(255, 255, 255, 0) # przezroczyste tło


def draw():
    # Zdefiniuj ćwierć obrotu, aby nasz kod był łatwy do odczytania
    ćwiartka = radiany(90)

    translate(200, 200) # start od środka

    # Dopasuj prawą dolną ćwiartkę ciasta, a następnie obróć o pozostałe ćwiartki

    if frame_count <= 4: # narysuj do 4 kwadrantów
        for i in range(frame_count):
            kwadrant()
            obróć(ćwiartka)

    if frame_count == 5: # dodaj zewnętrzną warstwę
        przetłumacz(-200, -200) # z powrotem do górnego rogu
        zewnętrzna() # warstwa


run(frame_rate=5) # 5 klatek na sekundę
