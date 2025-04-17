#!/bin/python3

from p5 import *
from math import random
from random import randint

def motif():
  global circle_size
  for i in range(5):
    ellipse(0, 0, circle_size / 5 * (5 - i), circle_size / 5 * (5 - i)) 

def setup():
  size(400, 400)
  frame_rate(3) 
  print('🖌 Цей візерунок складається з багатьох кіл!')
  
  global circle_size
  
  circle_size = 50
  
def draw():
  
  # Кольори візерунка
  stroke(40, 35, 100) # блакитний
  stroke_weight(2) # товстий контур
  fill(200, 180, 128) # золотий
  
  translate(0,0) # почати з верхнього лівого кута екрана
  
  if frame_count <= 16: # створює 16 рядків, а потім зупиняється
    for row in range(frame_count): # анімує 1 рядок за раз
      for shape in range(16): # створює рядок мотивів
        motif()
        translate(circle_size / 2, 0)
      translate(-width, circle_size / 2) # переходить вниз, щоб почати новий рядок
  
run()