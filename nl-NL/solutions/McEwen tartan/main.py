#!/bin/python3

from p5 import *

def setup():
  size(400, 400)
  frame_rate(10)
  print('🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁢󠁳󠁣󠁴󠁿 Dit is McEwen Tartan 🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁧󠁢󠁳󠁣󠁴󠁿')
 
  global square_size
  square_size = int(input('What size 🏴󠁧󠁢󠁳󠁣󠁴󠁿tartan would you like? 20, 50 of 100'))
  
def draw():
  
  lines = 10 * frame_count # Use in shape width/length to animate over time
  
  # McEwen tartan kleuren
  # Kleuren van de basisvierkanten
  BLUE = color(83, 143, 200)
  GREEN = color(78, 163, 162)
  BASIS_KLEUREN = [GROEN, BLAUW]
  
  # Kruiskleuren
  YELLOW = color(155, 176, 135)
  RED = color(155, 129, 113)
  KRUIS_KLEUREN = [GEEL, ROOD]
  
  # Kleur van het stiksel en overlappende kleur
  GREY = color(78, 99, 86)
  
  # Teken afwisselend alle GROENE en BLAUWE basisvierkanten
  no_stroke()
  y_coordinaat = 0
  vierkanten = width/vierkant_grootte
  
  for i in range (int(squares)):
    gap = 0
    for j in range (int(squares)):
      fill(BASE_COLORS[j % 2]) # GREEN and BLUE 
      rect(gap, y_coordinaat, vierkant_grootte, vierkant_grootte)
      gap = gap + vierkant_grootte
    y_coordinaat = y_coordinaat + vierkant_grootte
  
  # Kruizen
  stroke(GRIJS)
 
  # TEKEN afwisselend DE GELE en RODE kruizen
  for i in range (4):
    fill(GEEL)
    kruis = vierkant_grootte / 2 - 2 
    for i in range (int(squares/2)):
      fill(CROSS_COLORS[i % 2]) # YELLOW and RED
      rect(kruis, 0, 4, lijnen)  
      rect(0, kruis, lijnen, 4) 
      kruis = kruis + 2 * vierkant_grootte
    # Teken de stikkruisen
    no_fill() 
    kruis = vierkant_grootte + vierkant_grootte / 2 - 2
    for i in range (int(squares)): 
      rect(kruis, 0, 4, lijnen) 
      rect(0, kruis, lijnen, 4)
      kruis = kruis + vierkant_grootte

  # Teken de grijze lijnen waar het materiaal overlapt
  no_stroke()
  fill(GRIJS, 100)
  gap = vierkant_grootte - 4
  for i in range (int(squares)):
    rect(gap, 0, 8, lijnen)
    gap = gap + vierkant_grootte
  gap = vierkant_grootte - 4
  for i in range (int(squares)):
    rect(0, gap, lijnen, 8)
    gap = gap + vierkant_grootte
  
run()



