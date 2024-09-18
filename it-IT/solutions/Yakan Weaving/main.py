#!/bin/python3

from p5 import *
from math import random

def motivo():
  dimensione_motivo = 100
  
  #Colori del filo
  ARANCIONE = Color(254, 96, 1)
  VIOLA = Color(135, 18, 192)
  GIALLO = Color(243, 200, 19)
  BLU = Color(83, 171, 176)
    
  # Quadrati
  fill(ARANCIONE)
  rect(0, 0, dimensione_motivo/2, dimensione_motivo/2)
  fill(VIOLA)
  rect(50, 0, dimensione_motivo/2, dimensione_motivo/2)
  fill(GIALLO)
  rect(0, 50, dimensione_motivo/2, dimensione_motivo/2)
  fill(BLU)
  rect(50, 50, dimensione_motivo/2, dimensione_motivo/2)
  fill(VIOLA)
  rect(0, 0, dimensione_motivo/4, dimensione_motivo/4)
  fill(ARANCIONE)
  rect(50, 0, dimensione_motivo/4, dimensione_motivo/4)
  fill(BLU)
  rect(0, 50, dimensione_motivo/4, dimensione_motivo/4)
  fill(GIALLO)
  rect(50, 50, dimensione_motivo/4, dimensione_motivo/4)

def ruota_motivo():
  
  for forma in range(5): # righe di forme
    pushMatrix() # memorizza le impostazioni
    rotate(radians(45)) # ruota la forma di 45 gradi
    motif()
    popMatrix() # torna alle impostazioni memorizzate
    translate(larghezza_motivo, 0) # sposta orizzontalmente

def setup():
  size(400, 400)
  frame_rate(3)
  background(250, 5, 94) # rosa
  no_stroke()
  print('Questo è il tessuto 🇵🇭 Yakan ') 
  
def draw():
  
  global larghezza_motivo
  larghezza_motivo = 150 
  
  translate(-larghezza_motivo/2, -larghezza_motivo/2) # per iniziare con metà motivi 
  
  if frame_count < 20: # numero massimo di righe
    for riga in range(frame_count):
      ruota_motivo()
      if riga / 2 == 0: # per spostare il motivo sulla riga successiva
        translate(-larghezza_motivo * 5 + 75, 80) 
      else:  
        translate(-larghezza_motivo * 5 - 75, 80) 
        
run()
