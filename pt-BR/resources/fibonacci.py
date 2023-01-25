#!/bin/python3

from p5 import *
from math import random

def setup():
  size(800, 800)
  frame_rate(2)
  stroke_weight(2)
  background(255)
  ellipseMode(CORNER)
  
def draw():

  BLUE = color(0, 0, 255)
  BLACK = color(0, 0, 0)
  translate(width/2, height/2)
  
  # Motif
  rect(0, 0, 1, 1)
  arc(0, 0, 1, 1, radians(90), radians(180))
  translate(1,1)
  rotate(radians(270))
  
  first = 0
  second = 1
  next = first + second
  
  # Pattern
  if frame_count < 20:
    for i in range (frame_count):
      stroke(BLACK)
      rect(0, 0, next, next)
      no_fill()
      stroke(BLUE)
      arc(0, -next, next*2, next*2, radians(90), radians(180))
      translate(next,next)
      rotate(radians(270))
      first = second
      second = next
      next = first + second

run()