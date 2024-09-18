#!/bin/python3

from p5 import *
from math import random

def motivo():
  tamanho_motivo = 100
  
  #Define cores
  ORANGE = color(254, 96, 1)
  PURPLE = color(135, 18, 192)
  YELLOW = color(243, 200, 19)
  BLUE = color(83, 171, 176)
    
  # Quadrados
  fill(LARANJA)
  rect(0, 0, tamanho_motivo/2, tamanho_motivo/2)
  fill(ROXO)
  rect(50, 0, tamanho_motivo/2, tamanho_motivo/2)
  fill(AMARELO)
  rect(0, 50, tamanho_motivo/2, tamanho_motivo/2)
  fill(AZUL)
  rect(50, 50, tamanho_motivo/2, tamanho_motivo/2)
  fill(ROXO)
  rect(0, 0, tamanho_motivo/4, tamanho_motivo/4)
  fill(LARANJA)
  rect(50, 0, tamanho_motivo/4, tamanho_motivo/4)
  fill(AZUL)
  rect(0, 50, tamanho_motivo/4, tamanho_motivo/4)
  fill(AMARELO)
  rect(50, 50, tamanho_motivo/4, tamanho_motivo/4)

def girar_motivo():
  
  for shape in range(5): # row of shapes
    pushMatrix() # save settings
    rotate(radians(45)) # turn shape 45 degrees
    motivo()
    popMatrix() # go back to saved settings
    translate(motif_width, 0) # move horizontally

def setup():
  size(400, 400)
  frame_rate(3)
  background(250, 5, 94) # pink
  no_stroke()
  print('Isso é 🇵🇭 tecelagem Yakan') 
  
def draw():
  
  global largura_motivo
  largura_motivo = 150 
  
  translate(-motif_width/2, -motif_width/2) # to start with half motifs 
  
  if frame_count < 20: # maximum rows
    for linha in range(frame_count):
      girar_motivo()
      if row / 2 == 0: # to offset pattern on next row
        translate(-largura_motivo * 5 + 75, 80) 
      else:  
        translate(-largura_motivo * 5 - 75, 80) 
        
run()
