#!/bin/python3

from p5 import *
from math import random

def motif():
  motif_size = 100
  
  #Кольори матеріалів
  ORANGE = color(254, 96, 1) # помаранчевий
  PURPLE = color(135, 18, 192) # фіолетовий
  YELLOW = color(243, 200, 19) # жовтий
  BLUE = color(83, 171, 176) # блакитний
    
  # Квадрати
  fill(ORANGE)
  rect(0, 0, motif_size/2, motif_size/2)
  fill(PURPLE)
  rect(50, 0, motif_size/2, motif_size/2)
  fill(YELLOW)
  rect(0, 50, motif_size/2, motif_size/2)
  fill(BLUE)
  rect(50, 50, motif_size/2, motif_size/2)
  fill(PURPLE)
  rect(0, 0, motif_size/4, motif_size/4)
  fill(ORANGE)
  rect(50, 0, motif_size/4, motif_size/4)
  fill(BLUE)
  rect(0, 50, motif_size/4, motif_size/4)
  fill(YELLOW)
  rect(50, 50, motif_size/4, motif_size/4)

def rotate_motif():
  
  for shape in range(5): # ряд фігур
    push_matrix() # зберегти налаштування
    rotate(radians(45)) # повернути фігуру на 45 градусів
    motif()
    popMatrix() # повернутися до збережених налаштувань
    translate(motif_width, 0) # переміститися по горизонталі

def setup():
  size(400, 400)
  frame_rate(3)
  background(250, 5, 94) # рожевий
  no_stroke()
  print('Це 🇵🇭 яканське плетіння') 
  
def draw():
  
  global motif_width
  motif_width = 150 
  
  translate(-motif_width/2, -motif_width/2) # щоб почати з половинками мотиву 
  
  if frame_count < 20: # максимальна кількість рядків
    for row in range(frame_count):
      rotate_motif()
      if row % 2 == 0: # щоб змістити візерунок на наступному рядку
        translate(-motif_width * 5 + 75, 80) 
      else:  
        translate(-motif_width * 5 - 75, 80) 
        
run()
