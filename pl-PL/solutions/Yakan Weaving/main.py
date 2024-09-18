#!/bin/python3

from p5 import *
from math import random

def motif():
  rozmiar_motywu = 100
  
  #Kolory wątków
  ORANGE = color(254, 96, 1)
  PURPLE = color(135, 18, 192)
  YELLOW = color(243, 200, 19)
  BLUE = color(83, 171, 176)
    
  # Kwadraty
  Fill(POMARAŃCZOWY)
  rect(0, 0, motif_size/2, motif_size/2)
  Fill(FIOLETOWY)
  rect(50, 0, motif_size/2, motif_size/2)
  Wypełnienie(ŻÓŁTY)
  rect(0, 50, motif_size/2, motif_size/2)
  Fill(NIEBIESKI)
  rect(50, 50, motif_size/2, motif_size/2)
  Fill(FIOLETOWY)
  rect(0, 0, motif_size/4, motif_size/4)
  Fill(POMARAŃCZOWY)
  rect(50, 0, motif_size/4, motif_size/4)
  Fill(NIEBIESKI)
  rect(0, 50, motif_size/4, motif_size/4)
  Wypełnienie(ŻÓŁTY)
  rect(50, 50, motif_size/4, motif_size/4)

def rotate_motif():
  
  for shape in range(5): # row of shapes
    pushMatrix() # save settings
    rotate(radians(45)) # turn shape 45 degrees
    motyw()
    popMatrix() # go back to saved settings
    translate(motif_width, 0) # move horizontally

def setup():
  size(400, 400)
  frame_rate(3)
  background(250, 5, 94) # pink
  no_stroke()
  Print('to jest ?? Yakan tkanie ') 
  
def draw():
  
  global motif_width
  motif_width = 150 
  
  translate(-motif_width/2, -motif_width/2) # to start with half motifs 
  
  if frame_count < 20: # maximum rows
    dla wiersza w zakresie(frame_count):
      obróć_motif()
      if row / 2 == 0: # to offset pattern on next row
        translate(-motif_width * 5 + 75, 80) 
      else:  
        translate(-motif_width * 5 - 75, 80) 
        
run()
