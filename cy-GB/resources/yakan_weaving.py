#!/bin/python3

from p5 import *

def setup():
  size(400, 400)
  frame_rate(10)
  print('🏴 󠁧Dyma enghraifft o Dartan MacEwen 🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁧󠁢󠁳󠁣󠁴󠁿')
 
  global maint_sgwar
  maint_sgwar = int(input('Pa faint 🏴󠁧󠁢󠁳󠁣󠁴󠁿tartan hoffech chi? 20, 50 neu 100'))
  
def draw():
  
  llinellau = 10 * frame_count # Defnyddiwch mewn lled/hyd siâp i animeiddio dros amser
  
  # Lliwiau tartan MacEwen
  # Lliwiau sgwâr sylfaen
  GLAS = color(83, 143, 200)
  GWYRDD = color(78, 163, 162)
  LLIWIAU_SYLFAEN = [GWYRDD, GLAS]
  
  # Lliwiau croes
  MELYN = color(155, 176, 135)
  COCH = color(155, 129, 113)
  LLIWIAU_CROES = [MELYN, COCH]
  
  # Lliw pwyth a gorgyffwrdd
  LLWYD = color(78, 99, 86)
  
  # Llunio'r holl sgwariau sylfaen eiledol GWYRDD a GLAS
  no_stroke()
  cyfesuryn_y = 0
  sgwariau = width/maint_sgwar
  
  for i in range (int(sgwariau)):
    bwlch = 0
    for j in range (int(sgwariau)):
      fill(LLIWIAU_SYLFAEN[j % 2]) # GWYRDD a GLAS 
      rect(bwlch, cyfesuryn_y, maint_sgwar, maint_sgwar)
      bwlch = bwlch + maint_sgwar
    cyfesuryn_y = cyfesuryn_y + maint_sgwar
  
  # Croesau
  stroke(LLWYD)
 
  # Llunio'r croesau eiledol MELYN a COCH
  for i in range (4):
    fill(MELYN)
    croes = maint_sgwar / 2 - 2 
    for i in range (int(sgwariau/2)):
      fill(LLIWIAU_CROES[i % 2]) # MELYN a COCH
      rect(croes, 0, 4, llinellau)  
      rect(0, croes, llinellau, 4) 
      croes = croes + 2 * maint_sgwar
    # Llunio'r croesau pwytho
    no_fill() 
    croes = maint_sgwar + maint_sgwar / 2 - 2
    for i in range (int(sgwariau)): 
      rect(croes, 0, 4, llinellau) 
      rect(0, croes, llinellau, 4)
      croes = croes + maint_sgwar

  # Llunio'r llinellau llwyd lle mae'r deunydd yn gorgyffwrdd
  no_stroke()
  fill(LLWYD, 100)
  bwlch = maint_sgwar - 4
  for i in range (int(sgwariau)):
    rect(bwlch, 0, 8, llinellau)
    bwlch = bwlch + maint_sgwar
  bwlch = maint_sgwar - 4
  for i in range (int(sgwariau)):
    rect(0, bwlch, llinellau, 8)
    bwlch = bwlch + maint_sgwar
  
run()