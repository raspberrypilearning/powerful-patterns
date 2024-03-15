#!/bin/python3

from p5 import *
from math import random


def motif():
    taille_motif = 100

    # Couleurs du fil
    ORANGE = Color(254, 96, 1)
    VIOLET = Color(135, 18, 192)
    JAUNE = Color(243, 200, 19)
    BLEU = Color(83, 171, 176)

    # Carrés
    fill(ORANGE)
    rect(0, 0, taille_motif/2, taille_motif/2)
    fill(VIOLET)
    rect(50, 0, taille_motif/2, taille_motif/2)
    fill(JAUNE)
    rect(0, 50, taille_motif/2, taille_motif/2)
    fill(BLEU)
    rect(50, 50, taille_motif/2, taille_motif/2)
    fill(VIOLET)
    rect(0, 0, taille_motif/4, taille_motif/4)
    fill(ORANGE)
    rect(50, 0, taille_motif/4, taille_motif/4)
    fill(BLEU)
    rect(0, 50, taille_motif/4, taille_motif/4)
    fill(JAUNE)
    rect(50, 50, taille_motif/4, taille_motif/4)


def rotation_motif():
    for shape in range(5):  # ligne de motifs
        push_matrix() # enregistrer les paramètres
        rotate(radians(45)) # tourner la forme de 45 degrés
        motif()
        pop_matrix() # retourne aux paramètres enregistrés
        translate(largeur_motif, 0) # se déplacer horizontalement


def setup():
    size(400, 400)
    background(250, 5, 94)  # rose
    no_stroke()
    print('C\'est le 🇵🇭 tissage Yakan')


def draw():
    global largeur_motif
    largeur_motif = 150

    translate(-largeur_motif/2, -largeur_motif/2) # pour commencer avec des demi-motifs

    if frame_count < 20: # nombre maximum de lignes
        for row in range(frame_count):
            rotation_motif()
            if row / 2 == 0: # pour décaler le motif sur la ligne suivante
                translate(-largeur_motif * 5 + 75, 80)
            else:
                translate(-largeur_motif * 5 - 75, 80)


run(frame_rate=3)
