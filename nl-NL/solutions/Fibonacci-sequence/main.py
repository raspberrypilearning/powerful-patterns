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

  BLAUW = color(0, 0, 255)
  ZWART = color(0, 0, 0)
  translate(width/2, height/2)
  
  # Motief
  rect(0, 0, 1, 1)
  arc(0, 0, 1, 1, radians(90), radians(180))
  translate(1,1)
  rotate(radians(270))
  
  eerste = 0
  tweede = 1
  volgende = eerste + tweede
  
  # Patroon
  if frame_count < 20:
    for i in range (frame_count):
      stroke(ZWART)
      rect(0, 0, volgende, volgende)
      no_fill()
      stroke(BLAUW)
      arc(0, -volgende, volgende*2, volgende*2, radians(90), radians(180))
      translate(volgende,volgende)
      rotate(radians(270))
      eerste = tweede
      tweede = volgende
      volgende = eerste + tweede

run()