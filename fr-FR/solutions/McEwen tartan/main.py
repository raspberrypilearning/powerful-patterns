#!/bin/python3

from p5 import *

def setup():
  size(400, 400)
  frame_rate(10)
  print('🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁢󠁳󠁣󠁴󠁿 Voici McEwen Tartan 🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁧󠁢󠁳󠁣󠁴󠁿')
 
  global square_size
  square_size = int(input('What size 🏴󠁧󠁢󠁳󠁣󠁴󠁿tartan would you like? 20, 50 ou 100'))
  
def draw():
  
  lines = 10 * frame_count # Use in shape width/length to animate over time
  
  # Couleurs du tartan McEwen
  # Couleurs des carrés de base
  BLUE = color(83, 143, 200)
  GREEN = color(78, 163, 162)
  COULEURS_BASE = [VERT, BLEU]
  
  # Couleurs des croix
  YELLOW = color(155, 176, 135)
  RED = color(155, 129, 113)
  COULEURS_CROIX = [JAUNE, ROUGE]
  
  # Couleur de couture et de chevauchement
  GREY = color(78, 99, 86)
  
  # Dessiner tous les carrés de base alternés VERT et BLEU
  no_stroke()
  coordonnee_y = 0
  carres = width/taille_carre
  
  for i in range (int(squares)):
    ecart = 0
    for j in range (int(squares)):
      fill(BASE_COLORS[j % 2]) # GREEN and BLUE 
      rect(ecart, coordonnee_y, taille_carre, taille_carre)
      ecart = ecart + taille_carre
    coordonnee_y = coordonnee_y + taille_carre
  
  # Croix
  stroke(GRIS)
 
  # Dessine des croix alternées JAUNE et ROUGE
  for i in range (4):
    fill(JAUNE)
    croix = taille_carre / 2 - 2 
    for i in range (int(squares/2)):
      fill(CROSS_COLORS[i % 2]) # YELLOW and RED
      rect(croix, 0, 4, lignes)  
      rect(0, croix, lignes, 4) 
      croix = croix + 2 * taille_croix
    # Dessine les croix de couture
    no_fill() 
    croix = taille_carre + taille_carre / 2 - 2
    for i in range (int(squares)): 
      rect(croix, 0, 4, lignes) 
      rect(0, croix, lignes, 4)
      croix = croix + taille_croix

  # Dessine les lignes grises où le matériau se chevauche
  no_stroke()
  fill(GRIS, 100)
  ecart = taille_carre - 4
  for i in range (int(squares)):
    rect(ecart, 0, 8, lignes)
    ecart = ecart + taille_carre
  ecart = taille_carre - 4
  for i in range (int(squares)):
    rect(0, ecart, lignes, 8)
    ecart = ecart + taille_carre
  
run()


