#!/bin/python3

from draw import *
from time import *

# Based on the amazing Malaysian geometric cake art: Kek lapis Sarawak

def quadrant():

  # Dewiswch liwiau hyfryd ar gyfer haenau'r gacen
  turquoise = color(64, 224, 208)
  gold = color(255, 215, 0)
  tomato = color(255, 99, 71)
  
  # Mae jam yn glynu'r haenau at ei gilydd
  jam = color(255, 165, 0) 
  stroke(jam)
  stroke_weight(2) # Change the number to change the amount of jam

  # Cacen naw haen, gan ailadrodd y 3 lliw 3 gwaith
  for i in range(3):
    start_y = i * 60 # height of 3 blocks of cake
    fill(turquoise)
    rect(0, start_y, 180, 20)
    fill(gold)
    rect(0, start_y + 20, 180, 20)
    fill(tomato)
    rect(0, start_y + 40, 180, 20)

  
def outer():

  # Mae haen allanol o amgylch y gacen
  yellowgreen = Color(154, 205, 50) 
  
  no_fill() # Don't cover up the cake quadrants!
  stroke(yellowgreen)
  stroke_weight(20)
  rect(10, 10, 380, 380, 20) 


def setup():
  size(400, 400) # make the cake square
  background(255, 255, 255, 0) # transparent background
  frame_rate(5) # 5 frames per second


def draw():
  
  # Diffiniwch chwarter tro fel bod ein cod yn hawdd ei ddarllen
  quarter = radians(90)

  translate(200, 200) # start from the center
  
  # Gwnewch chwarter dde isaf y gacen wedyn cylchdroi ar gyfer y chwarteri eraill

  if frame_count <= 4: # draw up to 4 quadrants
    for i in range(frame_count): 
      quadrant()
      rotate(quarter)

  if frame_count == 5: # add the outer layer
    translate(-200, -200) # back to the top corner
    outer() # outer layer
    

run()
