#!/bin/python3

from draw import *
from time import *

# Baseado na incrível arte geométrica do bolo da Malásia: Kek lapis Sarawak

def quadrante():

  # Escolha algumas cores lindas para as camadas do bolo
  turquoise = color(64, 224, 208)
  gold = color(255, 215, 0)
  tomato = color(255, 99, 71)
  
  # Geleia gruda as camadas juntas
  jam = color(255, 165, 0) 
  stroke(geleia)
  stroke_weight(2) # Change the number to change the amount of jam

  #Nove camadas de bolo, repetindo as 3 cores 3 vezes
  for i in range(3):
    start_y = i * 60 # height of 3 blocks of cake
    fill(turquesa)
    rect(0, iniciar_y, 180, 20)
    fill(ouro)
    rect(0, iniciar_y + 20, 180, 20)
    fill(tomate)
    rect(0, iniciar_y + 40, 180, 20)

  
def exterior():

  # O bolo é embrulhado em uma camada externa
  amareloverde = Color(154, 205, 50) 
  
  no_fill() # Don't cover up the cake quadrants!
  stroke(amareloverde)
  stroke_weight(20)
  rect(10, 10, 380, 380, 20) 


def setup():
  size(400, 400) # make the cake square
  background(255, 255, 255, 0) # transparent background
  frame_rate(5) # 5 frames per second


def draw():
  
  # Defina um quarto de volta para que nosso código seja fácil de ler
  quarto = radians(90)

  translate(200, 200) # start from the center
  
  # Faça o quadrado inferior direito do bolo e gire para os outros quadrados

  if frame_count <= 4: # draw up to 4 quadrants
    for i in range(frame_count): 
      quadrante()
      rotate(quarto)

  if frame_count == 5: # add the outer layer
    translate(-200, -200) # back to the top corner
    outer() # outer layer
    

run()
