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

  BLEU = color(0, 0, 255)
  NOIR = color(0, 0, 0)
  translate(width/2, height/2)
  
  # Motif
  rect(0, 0, 1, 1)
  arc(0, 0, 1, 1, radians(90), radians(180))
  translate(1,1)
  rotate(radians(270))
  
  premier = 0
  deuxieme = 1
  suivant = premier + deuxieme
  
  # Motif
  if frame_count < 20:
    for i in range (frame_count):
      stroke(NOIR)
      rect(0, 0, suivant, suivant)
      no_fill()
      stroke(BLEU)
      arc(0, -suivant, suivant*2, suivant*2, radians(90), radians(180))
      translate(suivant,suivant)
      rotate(radians(270))
      premier = deuxieme
      deuxieme = suivant
      suivant = premier + deuxieme

run()