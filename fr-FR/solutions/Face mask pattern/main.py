#!/bin/python3

from p5 import *
from random import randint

def dessin_motif():
  orange = color(191, 64, 191)
  brun = color(200, 120, 0)
  vert = color(100, 155, 0)
  fill(orange)
  ellipse(200, 200, 200, 190)
  fill(0)
  # Les yeux
  ellipse(160, 190, 30, 30)
  ellipse(240, 190, 30, 30)
  fill(255)
  ellipse(165, 200, 10, 10)
  ellipse(245, 200, 10, 10)
  # La bouche
  noFill()
  stroke(255, 255, 255)
  ellipse(150, 250, 30, 30)
  ellipse(250, 250, 30, 30)
  fill(255, 255, 255)
  noStroke()
  rect(150, 230, 100, 40)
  fill(108, 200, 206)
  rect(152, 235, 96, 30)
  
  
def setup():
  size(400, 400)
  background(255)
  no_stroke()
  frame_rate(10)


def draw():
  push_matrix()
  translate(randint(-50, 350), randint(-50, 350)) # décalé de la largeur du quart de la face
  scale(0.25) # chemins de quart de cercle
  dessin_motif()
  pop_matrix()
 

run()