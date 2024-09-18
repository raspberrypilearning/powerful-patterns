#!/bin/python3

from draw import *
from time import *

# Na podstawie niesamowitej sztuki malezyjskiego geometrycznego ciasta: Kek lapis Sarawak

def kwadrant():

  # Wybierz kilka wspaniałych kolorów dla warstw ciasta
  turquoise = color(64, 224, 208)
  gold = color(255, 215, 0)
  tomato = color(255, 99, 71)
  
  # Zacięcie skleja warstwy razem
  jam = color(255, 165, 0) 
  skok(zacięcie)
  stroke_weight(2) # Change the number to change the amount of jam

  # Dziewięć warstw ciasta, powtarzając 3 kolory 3 razy
  for i in range(3):
    start_y = i * 60 # height of 3 blocks of cake
    wypełnienie(turkusowy)
    rect(0, start_y, 180, 20)
    fill(złoto)
    rect(0, start_y + 20, 180, 20)
    fill(pomidor)
    rect(0, start_y + 40, 180, 20)

  
def outer():

  # Thehe cake is wrapped in an outer layer
  Żółtozielony = Kolor(154, 205, 50) 
  
  no_fill() # Don't cover up the cake quadrants!
  stroke(żółto-zielony)
  stroke_weight(20)
  rect(10, 10, 380, 380, 20) 


def setup():
  size(400, 400) # make the cake square
  background(255, 255, 255, 0) # transparent background
  frame_rate(5) # 5 frames per second


def draw():
  
  # Zdefiniuj ćwierć obrotu, aby nasz kod był łatwy do odczytania
  ćwiartka = radiany(90)

  translate(200, 200) # start from the center
  
  # Dopasuj prawą dolną ćwiartkę ciasta, a następnie obróć o pozostałe ćwiartki

  if frame_count <= 4: # draw up to 4 quadrants
    for i in range(frame_count): 
      kwadrant()
      obróć(ćwiartka)

  if frame_count == 5: # add the outer layer
    translate(-200, -200) # back to the top corner
    outer() # outer layer
    

run()
