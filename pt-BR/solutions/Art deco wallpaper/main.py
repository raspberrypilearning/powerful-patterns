#!/bin/python3

from p5 import *
from math import random
from random import randint

def motivo():
  global tamanho_circulo
  for i in range(5):
    ellipse(0, 0, circle_size / 5 * (5 - i), circle_size / 5 * (5  - i)) 

def setup():
  size(400, 400)
  frame_rate(3) 
  print('🖌 Esta arte usa muitos círculos!')
  
  global tamanho_circulo
  
  tamanho_circulo = 50
  
def draw():
  
  # Cores do padrão
  stroke(40, 35, 100) # blue
  stroke_weight(2) # thick border
  fill(200, 180, 128) # gold
  
  translate(0,0) # start from the top left of the screen
  
  if frame_count <= 16: # creates 16 rows then stops
    for row in range (frame_count): # animates 1 row at a time
      for shape in range (16): # create a row of motifs
        motivo()
        translate(tamanho_circulo / 2, 0)
      translate(-width, circle_size / 2) # move down to start next row
  
run()