#!/bin/python3

from draw import *
from time import *

# Gebaseerd op de prachtige Maleisische geometrische taartkunst: Kek lapis Sarawak

def kwadrant():

  # Kies een aantal prachtige kleuren voor de taartlagen
  turquoise = color(64, 224, 208)
  gold = color(255, 215, 0)
  tomato = color(255, 99, 71)
  
  # Jam plakt de lagen aan elkaar
  jam = color(255, 165, 0) 
  stroke(jam)
  stroke_weight(2) # Change the number to change the amount of jam

  # Negen lagen cake, waarbij de 3 kleuren 3 keer worden herhaald
  for i in range(3):
    start_y = i * 60 # height of 3 blocks of cake
    fill(turkoois)
    rect(0, start_y, 180, 20)
    fill(goud)
    rect(0, start_y + 20, 180, 20)
    fill (tomaat)
    rect(0, start_y + 40, 180, 20)

  
def buitenste():

  # Thehe cake is wrapped in an outer layer
  geelgroen = Color(154, 205, 50) 
  
  no_fill() # Don't cover up the cake quadrants!
  stroke(geelgroen)
  stroke_weight(20)
  rect(10, 10, 380, 380, 20) 


def setup():
  size(400, 400) # make the cake square
  background(255, 255, 255, 0) # transparent background
  frame_rate(5) # 5 frames per second


def draw():
  
  # Definieer een kwartslag zodat onze code gemakkelijk te lezen is
  kwart = radians(90)

  translate(200, 200) # start from the center
  
  # Maak het kwart rechtsonder van de cake en draai dan voor de andere kwarten

  if frame_count <= 4: # draw up to 4 quadrants
    for i in range(frame_count): 
      kwadrant()
      rotate(kwart)

  if frame_count == 5: # add the outer layer
    translate(-200, -200) # back to the top corner
    outer() # outer layer
    

run()
