#!/bin/python3

from draw import *
from time import *

# Gebaseerd op de prachtige Maleisische geometrische taartkunst: Kek lapis Sarawak

def kwadrant():

  # Kies een aantal prachtige kleuren voor de taartlagen
  turkoois = color(64, 224, 208)
  goud = color(255, 215, 0)
  tomaat = color(255, 99, 71)
  
  # Jam plakt de lagen aan elkaar
  jam = jolor(255, 165, 0) 
  stroke(jam)
  stroke_weight(2) # Wijzig het getal om de hoeveelheid jam te wijzigen

  # Negen lagen cake, waarbij de 3 kleuren 3 keer worden herhaald
  for i in range(3):
    start_y = i * 60 # hoogte van 3 blokken cake
    fill(turkoois)
    rect(0, start_y, 180, 20)
    fill(goud)
    rect(0, start_y + 20, 180, 20)
    fill (tomaat)
    rect(0, start_y + 40, 180, 20)

  
def buitenste():

  # De cake is verpakt in een buitenste laag
  geelgroen = color(154, 205, 50) 
  
  no_fill() # Bedek de taartkwadranten niet!
  stroke(geelgroen)
  stroke_weight(20)
  rect(10, 10, 380, 380, 20) 


def setup():
  size(400, 400) # maak de taart vierkant
  background(255, 255, 255, 0) # transparante achtergrond
  frame_rate(5) # 5 frames per seconde


def draw():
  
  # Definieer een kwartslag zodat onze code gemakkelijk te lezen is
  kwart = radians(90)

  translate(200, 200) # start vanuit het midden
  
  # Maak het kwart rechtsonder van de cake en draai dan voor de andere kwarten

  if frame_count <= 4: # teken maximaal 4 kwadranten
    for i in range(frame_count): 
      kwadrant()
      rotate(kwart)

  if frame_count == 5: # voeg de buitenste laag toe
    translate(-200, -200) # terug naar de bovenhoek
    buitenste() # buitenste laag
    

run()
