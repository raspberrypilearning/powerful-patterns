#!/bin/python3

from p5 import *
from math import random

def motif():
  taille_motif = 100
  
  #Couleurs du fil
  ORANGE = color(254, 96, 1)
  PURPLE = color(135, 18, 192)
  YELLOW = color(243, 200, 19)
  BLUE = color(83, 171, 176)
    
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
  
  for shape in range(5): # row of shapes
    pushMatrix() # save settings
    rotate(radians(45)) # turn shape 45 degrees
    motif()
    popMatrix() # go back to saved settings
    translate(motif_width, 0) # move horizontally

def setup():
  size(400, 400)
  frame_rate(3)
  background(250, 5, 94) # pink
  no_stroke()
  print('C\'est le 🇵🇭 tissage Yakan') 
  
def draw():
  
  global largeur_motif
  largeur_motif = 150 
  
  translate(-motif_width/2, -motif_width/2) # to start with half motifs 
  
  if frame_count < 20: # maximum rows
    for row in range(frame_count):
      rotation_motif()
      if row / 2 == 0: # to offset pattern on next row
        translate(-largeur_motif * 5 + 75, 80) 
      else:  
        translate(-largeur_motif * 5 - 75, 80) 
        
run()
