#!/bin/python3

from p5 import *


def setup():
    size(400, 400)


def draw():
    lignes = 10 * frame_count # Utiliser dans la forme largeur/longueur pour animer au fil du temps

    # Couleurs du tartan McEwen
    # Couleurs des carrés de base
    BLEU = Color(83, 143, 200)
    VERT = Color(78, 163, 162)
    COULEURS_BASE = [VERT, BLEU]

    # Couleurs des croix
    JAUNE = Color(155, 176, 135)
    ROUGE = Color(155, 129, 113)
    COULEURS_CROIX = [JAUNE, ROUGE]

    # Couleur de couture et de chevauchement
    GRIS = Color(78, 99, 86)

    # Dessiner tous les carrés de base alternés VERT et BLEU
    no_stroke()
    coordonnee_y = 0
    carres = width/taille_carre

    for i in range(int(carres)):
        ecart = 0
        for i in range(int(carres)):
            fill(COULEURS_BASE[j % 2])  # VERT et BLEU
            rect(ecart, coordonnee_y, taille_carre, taille_carre)
            ecart = ecart + taille_carre
        coordonnee_y = coordonnee_y + taille_carre

    # Croix
    stroke(GRIS)

    # Dessine des croix alternées JAUNE et ROUGE
    for i in range(4):
        fill(JAUNE)
        croix = taille_carre / 2 - 2
        for j in range(int(carres/2)):
            fill(COULEURS_CROIX[i % 2])  # JAUNE et ROUGE
            rect(croix, 0, 4, lignes)
            rect(0, croix, lignes, 4)
            croix = croix + 2 * taille_carre
        # Dessine les croix de couture
        no_fill()
        croix = taille_carre + taille_carre / 2 - 2
        for i in range(int(carres)):
            rect(croix, 0, 4, lignes)
            rect(0, croix, lignes, 4)
            croix = croix + taille_carre

    # Dessine les lignes grises où le matériau se chevauche
    no_stroke()
    fill(GRIS, 100)
    ecart = taille_carre - 4
    for i in range(int(carres)):
        rect(ecart, 0, 8, lignes)
        ecart = ecart + taille_carre
    ecart = taille_carre - 4
    for i in range(int(carres)):
        rect(0, ecart, lignes, 8)
        ecart = ecart + taille_carre


print('🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁢󠁳󠁣󠁴󠁿 Voici McEwen Tartan 🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁧󠁢󠁳󠁣󠁴󠁿')
taille_carre = int(
    input('Quelle taille de tartan 🏴souhaites-tu ? 20, 50 ou 100'))

run(frame_rate=10)
