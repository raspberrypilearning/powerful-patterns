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

  BLU = Color(0, 0, 255)
  NERO = Color(0, 0, 0)
  translate(width/2, height/2)
  
  # Motivo
  rect(0, 0, 1, 1)
  arc(0, 0, 1, 1, radians(90), radians(180))
  translate(1,1)
  rotate(radians(270))
  
  primo = 0
  secondo = 1
  successivo = primo + secondo
  
  # Modello
  if frame_count < 20:
    for i in range (frame_count):
      stroke(NERO)
      rect(0, 0, successivo, successivo)
      no_fill()
      stroke(BLU)
      arc(0, -successivo, successivo*2, successivo*2, radians(90), radians(180))
      translate(successivo,successivo)
      rotate(radians(270))
      primo = secondo
      secondo = successivo
      successivo = primo + secondo

run()