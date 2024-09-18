#!/bin/python3

from p5 import *
from math import random
from random import randint

def motief():
  global cirkel_grootte
  for i in range(5):
    ellipse(0, 0, circle_size / 5 * (5 - i), circle_size / 5 * (5  - i)) 

def setup():
  size(400, 400)
  frame_rate(3) 
  print('🖌 Deze kunst gebruikt veel cirkels!')
  
  global cirkel_grootte
  
  cirkel_grootte = 50
  
def draw():
  
  # Patroonkleuren
  stroke(40, 35, 100) # blue
  stroke_weight(2) # thick border
  fill(200, 180, 128) # gold
  
  translate(0,0) # start from the top left of the screen
  
  if frame_count <= 16: # creates 16 rows then stops
    for row in range (frame_count): # animates 1 row at a time
      for shape in range (16): # create a row of motifs
        motief()
        translate(cirkel_grootte / 2, 0)
      translate(-width, circle_size / 2) # move down to start next row
  
run()