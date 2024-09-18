#!/bin/python3

from draw import *
from time import *

# Basé sur l'incroyable art du gâteau géométrique malaisien : Kek lapis Sarawak

def quadrant():

  # Choisis des couleurs magnifiques pour les couches de gâteau
  turquoise = color(64, 224, 208)
  gold = color(255, 215, 0)
  tomato = color(255, 99, 71)
  
  # La confiture colle les couches ensemble
  jam = color(255, 165, 0) 
  stroke(confiture)
  stroke_weight(2) # Change the number to change the amount of jam

  # Neuf couches de gâteau, en répétant les 3 couleurs 3 fois
  for i in range(3):
    start_y = i * 60 # height of 3 blocks of cake
    fill(turquoise)
    rect(0, debut_y, 180, 20)
    fill(or_)
    rect(0, debut_y + 20, 180, 20)
    fill(tomate)
    rect(0, debut_y + 40, 180, 20)

  
def externe():

  # Thehe cake is wrapped in an outer layer
  jaunevert = Color(154, 205, 50) 
  
  no_fill() # Don't cover up the cake quadrants!
  stroke(jaunevert)
  stroke_weight(20)
  rect(10, 10, 380, 380, 20) 


def setup():
  size(400, 400) # make the cake square
  background(255, 255, 255, 0) # transparent background
  frame_rate(5) # 5 frames per second


def draw():
  
  # Définis un quart de tour pour que notre code soit facile à lire
  quart = radians(90)

  translate(200, 200) # start from the center
  
  # Faire le quart inférieur droit du gâteau puis faire pivoter pour les autres quarts

  if frame_count <= 4: # draw up to 4 quadrants
    for i in range(frame_count): 
      quadrant()
      rotate(quart)

  if frame_count == 5: # add the outer layer
    translate(-200, -200) # back to the top corner
    outer() # outer layer
    

run()
