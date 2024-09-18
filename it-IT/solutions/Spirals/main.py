#!/bin/python3

from p5 import *
from math import random
from random import randint

def motivo():
  fill(randint(0, 255),randint(0, 255) ,randint(0, 255))
  ellipse(0, 0, 25, 25) 
  fill(0, 0, 0)
  ellipse(0, 0, 15, 15) 
  fill(randint(0, 255),randint(0, 255) ,randint(0, 255))
  for i in range(4): # una breve fila di quadrati
    rect(i * 5, 0, 5, 5) 

def setup():
  size(400, 400) 
  frame_rate(10) # animazione veloce
  stroke_weight(2) # bordo spesso
  background(255)
  
def draw():
  translate(200, 200) # inizia dal centro dello schermo
  if frame_count < 150:
    for i in range(frame_count): # anima il motivo geometrico
      motivo()
      rotate(5) # gira il motivo base
      translate(i, i) # sposta il motivo base
  
run()