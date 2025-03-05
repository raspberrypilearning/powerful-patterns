#!/bin/python3

from p5 import *
from random import randint

def draw_motif():
  orange = сolor(191, 64, 191) # помаранчевий
  brown = color(200, 120, 0) # коричневий
  green = color(100, 155, 0) # зелений
  fill(orange)
  ellipse(200, 200, 200, 190)
  fill(0)
  # Очі
  ellipse(160, 190, 30, 30)
  ellipse(240, 190, 30, 30)
  fill(255)
  ellipse(165, 200, 10, 10)
  ellipse(245, 200, 10, 10)
  # Рот
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
  translate(randint(-50, 350), randint(-50, 350)) # oзміщення по ширині на чверть розміру обличчя
  scale(0.25) # шляхи розміром у чверть
  draw_motif()
  pop_matrix()
 

run()