#!/bin/python3

from p5 import *

def setup():
  size(400, 400)
  frame_rate(10)
  print('🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁢󠁳󠁣󠁴󠁿 Questo è il Tartan McEwen 🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁧󠁢󠁳󠁣󠁴󠁿')
 
  global dimensione_quadrato
  dimensione_quadrato = int(input('Che taglia di 🏴󠁧󠁢󠁳󠁣󠁴󠁿tartan vorresti? 20, 50, or 100'))
  
def draw():
  
  linee = 10 * frame_count # Utilizzare nella larghezza/lunghezza della forma per creare l'animazione
  
  # Colori trama del tartan McEwen
  # Colori quadrati di base
  BLU = Color(83, 143, 200)
  VERDE = Color(78, 163, 162)
  COLORI_BASE = [VERDE, BLU]
  
  # Colori incrociati
  GIALLO = Color(155, 176, 135)
  ROSSO = Color(155, 129, 113)
  COLORI_INCROCIATI = [GIALLO, ROSSO]
  
  # Colore di Cuciture e sovrapposizioni
  GRIGIO = Color(78, 99, 86)
  
  # Disegna tutti i quadrati di base alternati VERDE e BLU
  no_stroke()
  y_coordinate = 0
  quadrati= width/dimensione_quadrato
  
  for i in range(int(quadrati)):
    gap = 0
    for j in range(int(quadrati)):
      fill(COLORI_BASE[j % 2]) # VERDE e BLU 
      rect(gap, y_coordinate, dimensione_quadrato, dimensione_quadrato)
      gap = gap + dimensione_quadrato
    y_coordinate = y_coordinate + dimensione_quadrato
  
  # Incroci
  stroke(GRIGIO)
 
  # Disegnare gli incroci alternati GIALLO e ROSSO
  for i in range (4):
    fill(GIALLO)
    croce= dimensione_quadrato / 2 - 2 
    for i in range(int(quadrati/2)):
      fill(COLORI_INCROCIATI[i % 2]) # GIALLO e ROSSO
      rect(croce, 0, 4, linee)  
      rect(0, croce, linee, 4) 
      croce= croce + 2 * dimensione_quadrato
    # Disegna le croci di cucitura
    no_fill() 
    croce = dimensione_quadrato + dimensione_quadrato / 2 - 2
    for i in range(int(quadrati)): 
      rect(croce, 0, 4, linee) 
      rect(0, croce, linee, 4)
      croce= croce+dimensione_quadrato

  # Disegna le linee grigie dove il materiale si sovrappone
  no_stroke()
  fill(GRIGIO, 100)
  gap = dimensione_quadrato - 4
  for i in range(int(quadrati)):
    rect(gap, 0, 8, linee)
    gap = gap + dimensione_quadrato
  gap = dimensione_quadrato - 4
  for i in range(int(squares)):
    rect(0, gap, linee, 8)
    gap = gap + dimensione_quadrato
  
run()



