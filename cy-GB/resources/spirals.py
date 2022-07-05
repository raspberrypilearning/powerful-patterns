#!/bin/python3

from p5 import *
from math import random
from random import randint

def motiff():
  fill(randint(0, 255),randint(0, 255) ,randint(0, 255))
  ellipse(0, 0, 25, 25) 
  fill(0, 0, 0)
  ellipse(0, 0, 15, 15) 
  fill(randint(0, 255),randint(0, 255) ,randint(0, 255))
  for i in range(4): # rhes fer o sgwariau
    rect(i * 5, 0, 5, 5) 

def setup():
  size(400, 400) 
  frame_rate(10) # animeiddiad cyflym
  stroke_weight(2) # border trwchus
  background(255)
  
def draw():
  translate(200, 200) # dechrau o ganol y sgrin
  if frame_count < 150:
    for i in range(frame_count): # animeiddio'r patrwm
      motiff()
      rotate(5) # troi'r motiff
      translate(i,i) # symud y motiff
  
run()