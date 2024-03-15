#!/bin/python3

from p5 import *
from time import *

# Basé sur l'incroyable art du gâteau géométrique malaisien : Kek lapis Sarawak


def quadrant():
    # Choisis des couleurs magnifiques pour les couches de gâteau
    turquoise = Color(64, 224, 208)
    or_ = Color(255, 215, 0)
    tomate = Color(255, 99, 71)

    # La confiture colle les couches ensemble
    confiture = Color(255, 165, 0)
    stroke(confiture)
    stroke_weight(2) # Change le nombre pour changer la quantité de confiture

    # Neuf couches de gâteau, en répétant les 3 couleurs 3 fois
    for i in range(3):
        debut_y = i * 60 # hauteur de 3 blocs de gâteau
        fill(turquoise)
        rect(0, debut_y, 180, 20)
        fill(or_)
        rect(0, debut_y + 20, 180, 20)
        fill(tomate)
        rect(0, debut_y + 40, 180, 20)


def externe():
    # Le gâteau est enveloppé dans une couche extérieure
    jaunevert = Color(154, 205, 50)

    no_fill() # Ne couvre pas les quadrants du gâteau !
    stroke(jaunevert)
    stroke_weight(20)
    rect(10, 10, 380, 380, 20)


def setup():
    size(400, 400) # faire le gâteau carré
    background(255, 255, 255, 0) # arrière-plan transparent


def draw():
    # Définis un quart de tour pour que notre code soit facile à lire
    quart = radians(90)

    translate(200, 200) # partir du centre

    # Faire le quart inférieur droit du gâteau puis faire pivoter pour les autres quarts

    if frame_count <= 4: # dessine jusqu'à 4 quadrants
        for i in range(frame_count):
            quadrant()
            rotate(quart)

    if frame_count == 5: # ajoute la couche externe
        translate(-200, -200) # retour au coin supérieur
        externe() # couche externe


run(frame_rate=5) # 5 images par seconde
