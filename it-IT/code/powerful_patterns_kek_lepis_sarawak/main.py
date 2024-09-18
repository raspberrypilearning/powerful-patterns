#!/bin/python3

from p5 import *
from time import *

# Basato sulla straordinaria arte della torta geometrica malese: Sarawak


def quadrante():
    # Scegli degli splendidi colori per gli strati della torta
    turchese = Color(64, 224, 208)
    oro = Color(255, 215, 0)
    pomodoro = Color(255, 99, 71)

    # La marmellata tiene insieme gli strati
    marmellata = Color(255, 165, 0)
    stroke(marmellata)
    stroke_weight(2) # Cambia il numero per cambiare la quantità di marmellata

    # Nove strati di torta, ripetendo i tre colori 3 volte
    for i in range(3):
        start_y = i*60 # altezza di 3 blocchi di torta
        fill(turchese)
        rect(0, start_y, 180, 20)
        fill(oro)
        rect(0, start_y + 20, 180, 20)
        fill(pomodoro)
        rect(0, start_y + 40, 180, 20)


def esterno():
    # La torta è avvolta in uno strato esterno
    gialloverde= Color(154, 205, 50)

    no_fill() # Non coprire i quadranti della torta!
    stroke(gialloverde)
    stroke_weight(20)
    rect(10, 10, 380, 380, 20)


def setup():
    size(400, 400) # rende la torta quadrata
    background(255, 255, 255, 0) # sfondo trasparente


def draw():
    # Definisce un quarto di giro per rendere il codice più leggibile
    quarto= radians(90)

    translate(200, 200) # inizia dal centro

    # Crea il quarto in basso a destra della torta, quindi ruota per gli altri quarti

    if frame_count <= 4: # disegna fino a 4 quadranti
        for i in range(frame_count):
            quadrante()
            rotate(quarto)

    if frame_count == 5: # aggiunge lo strato esterno
        translate(-200, -200) # torna nell' angolo in alto
        esterno() # strato esterno


run(frame_rate=5) # 5 fotogrammi al secondo
