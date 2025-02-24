#!/bin/python3

from p5 import *
from math import random
from random import randint

def motief():
  global cirkel_grootte
  for i in range(5):
    ellipse(0, 0, cirkel_grootte / 5 * (5 - i), cirkel_grootte / 5 * (5 - i)) 

def setup():
  size(400, 400)
  frame_rate(3) 
  print('🖌 Deze kunst gebruikt veel cirkels!')
  
  global cirkel_grootte
  
  cirkel_grootte = 50
  
def draw():
  
  # Patroonkleuren
  stroke(40, 35, 100) # blauw
  stroke_weight(2) # dikke rand
  fill(200, 180, 128) # goud
  
  translate(0,0) # start vanaf de linkerbovenhoek van het scherm
  
  if frame_count <= 16: # maakt 16 rijen aan en stopt dan
    for row in range (frame_count): #animeert 1 rij tegelijk
      for shape in range(16): # maak een rij motieven aan
        motief()
        translate(cirkel_grootte / 2, 0)
      translate(-width, cirkel_grootte / 2) # ga naar beneden om de volgende rij te beginnen
  
run()