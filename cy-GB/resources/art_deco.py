#!/bin/python3

from p5 import *
from math import random
from random import randint

def motiff():
  global maint_cylch
  for i in range(5):
    ellipse(0, 0, maint_cylch / 5 * (5 - i), maint_cylch / 5 * (5  - i)) 

def setup():
  size(400, 400)
  frame_rate(3) 
  print('🖌', 'Mae\'r celfwaith hwn yn defnyddio llawer o gylchoedd!')
  
  global maint_cylch
  
  maint_cylch = 50
  
def draw():
  
  # Lliwiau patrwm
  stroke(40, 35, 100) # glas
  stroke_weight(2) # border trwchus
  fill(200, 180, 128) # aur
  
  translate(0,0) # dechrau o ochr chwith uchaf y sgrin
  
  if frame_count <= 16: # creu 16 rhes wedyn yn stopio
    for row in range (frame_count): # animeiddio 1 rhes ar y tro
      for shape in range (16): # creu rhes o fotiffau
        motiff()
        translate(maint_cylch / 2, 0)
      translate(-width, maint_cylch / 2) # symudwch i lawr i ddechrau'r rhes nesaf
  
run()