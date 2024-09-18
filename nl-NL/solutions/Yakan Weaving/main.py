#!/bin/python3

from p5 import *
from math import random

def motief():
  motief_grootte = 100
  
  #Kleuren van de draad
  ORANGE = color(254, 96, 1)
  PURPLE = color(135, 18, 192)
  YELLOW = color(243, 200, 19)
  BLUE = color(83, 171, 176)
    
  # Vierkanten
  fill(ORANJE)
  rect(0, 0, motief_grootte/2, motief_grootte/2)
  fill(PAARS)
  rect(50, 0, motief_grootte/2, motief_grootte/2)
  fill(GEEL)
  rect(0, 50, motief_grootte/2, motief_grootte/2)
  fill(BLAUW)
  rect(50, 50, motief_grootte/2, motief_grootte/2)
  fill(PAARS)
  rect(0, 0, motief_grootte/4, motief_grootte/4)
  fill(ORANJE)
  rect(50, 0, motief_grootte/4, motief_grootte/4)
  fill(BLAUW)
  rect(0, 50, motief_grootte/4, motief_grootte/4)
  fill(GEEL)
  rect(50, 50, motief_grootte/4, motief_grootte/4)

def draai_motief():
  
  for shape in range(5): # row of shapes
    pushMatrix() # save settings
    rotate(radians(45)) # turn shape 45 degrees
    motief()
    popMatrix() # go back to saved settings
    translate(motif_width, 0) # move horizontally

def setup():
  size(400, 400)
  frame_rate(3)
  background(250, 5, 94) # pink
  no_stroke()
  print('Dit is 🇵🇭 Yakan-weven ') 
  
def draw():
  
  global motief_breedte
  motief_breedte = 150 
  
  translate(-motif_width/2, -motif_width/2) # to start with half motifs 
  
  if frame_count < 20: # maximum rows
    for row in range(frame_count):
      draai_motief()
      if row / 2 == 0: # to offset pattern on next row
        translate(-motief_breedte * 5 + 75, 80) 
      else:  
        translate(-motief_breedte * 5 - 75, 80) 
        
run()
