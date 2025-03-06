#!/bin/python3

from p5 import *
from math import random
from random import randint

def motif():
  global taille_cercle
  for i in range(5):
    ellipse(0, 0, taille_cercle / 5 * (5 - i), taille_cercle / 5 * (5 - i)) 

def setup():
  size(400, 400)
  frame_rate(3) 
  print('🖌 Cet art utilise beaucoup de cercles !')
  
  global taille_cercle
  
  taille_cercle = 50
  
def draw():
  
  # Couleurs du motif
  stroke(40, 35, 100) # bleu
  stroke_weight(2) # bordure épaisse
  fill(200, 180, 128) # or
  
  translate(0,0) # commencer en haut à gauche de l'écran
  
  if frame_count <= 16: # crée 16 lignes puis s'arrête
    for row in range (frame_count): # anime 1 ligne à la fois
      for shape in range(16): # créer une ligne de motifs
        motif()
        translate(taille_cercle / 2, 0)
      translate(-width, taille_cercle / 2) # descendre pour commencer à la ligne suivante
  
run()