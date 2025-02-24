#!/bin/python3

from p5 import *
from math import random

def motief():
  motief_grootte = 100
  
  #Kleuren van de draad
  ORANJE = color(254, 96, 1)
  PAARS = color(135, 18, 192)
  GEEL = color(243, 200, 19)
  BLAUW = color(83, 171, 176)
    
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
  
  for shape in range(5): # rij van motieven
    pushMatrix() # instellingen opslaan
    rotate(radians(45)) # vorm 45 graden draaien
    motief()
    popMatrix() # ga terug naar opgeslagen instellingen
    translate(motief_breedte, 0) # horizontaal bewegen

def setup():
  size(400, 400)
  frame_rate(3)
  background(250, 5, 94) # roze
  no_stroke()
  print('Dit is 🇵🇭 Yakan-weven ') 
  
def draw():
  
  global motief_breedte
  motief_breedte = 150 
  
  translate(-motief_breedte/2, -motief_breedte/2) # om te beginnen met halve motieven 
  
  if frame_count < 20: # maximum rijen
    for row in range(frame_count):
      draai_motief()
      if row / 2 == 0: # om het patroon op de volgende rij te verschuiven
        translate(-motief_breedte * 5 + 75, 80) 
      else:  
        translate(-motief_breedte * 5 - 75, 80) 
        
run()
