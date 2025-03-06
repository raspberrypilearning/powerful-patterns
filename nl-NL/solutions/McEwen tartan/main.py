#!/bin/python3

from p5 import *

def setup():
  size(400, 400)
  frame_rate(10)
  print('🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁢󠁳󠁣󠁴󠁿 Dit is McEwen Tartan 🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁧󠁢󠁳󠁣󠁴󠁿')
 
  global vierkant_grootte
  vierkant_grootte = int(input('Welke maat 🏴󠁧󠁢󠁳󠁣󠁴󠁿tartan wil je? 20, 50 of 100'))
  
def draw():
  
  lijnen = 10 * frame_count # Gebruik de breedte/lengte van de vorm om in de loop van de tijd te animeren
  
  # McEwen tartankleuren
  # Kleuren van de basisvierkanten
  BLAUW = color(83, 143, 200)
  GROEN = color(78, 163, 162)
  BASIS_KLEUREN = [GROEN, BLAUW]
  
  # Kruiskleuren
  GEEL = color(155, 176, 135)
  ROOD = color(155, 129, 113)
  KRUIS_KLEUREN = [GEEL, ROOD]
  
  # Kleur van het stiksel en overlappende kleur
  GRIJS = color(78, 99, 86)
  
  # Teken afwisselend alle GROENE en BLAUWE basisvierkanten
  no_stroke()
  y_coordinaat = 0
  vierkanten = width/vierkant_grootte
  
  for i in range (int(vierkanten)):
    gat = 0
    for j in range (int(vierkanten)):
      fill(BASIS_KLEUREN[j % 2]) # GROEN en BLAUW 
      rect(gat, y_coordinaat, vierkant_grootte, vierkant_grootte)
      gat = gat + vierkant_grootte
    y_coordinaat = y_coordinaat + vierkant_grootte
  
  # Kruizen
  stroke(GRIJS)
 
  # TEKEN afwisselend DE GELE en RODE kruizen
  for i in range (4):
    fill(GEEL)
    kruis = vierkant_grootte / 2 - 2 
    for i in range (int(vierkanten/2)):
      fill(KRUIS_KLEUREN[i% 2]) #GEEL en ROOD
      rect(kruis, 0, 4, lijnen)  
      rect(0, kruis, lijnen, 4) 
      kruis = kruis + 2 * vierkant_grootte
    # Teken de stikkruisen
    no_fill() 
    kruis = vierkant_grootte + vierkant_grootte / 2 - 2
    for i in range (int(vierkanten)): 
      rect(kruis, 0, 4, lijnen) 
      rect(0, kruis, lijnen, 4)
      kruis = kruis + vierkant_grootte

  # Teken de grijze lijnen waar het materiaal overlapt
  no_stroke()
  fill(GRIJS, 100)
  gap = vierkant_grootte - 4
  for i in range (int(vierkanten)):
    rect(gap, 0, 8, lijnen)
    gap = gap + vierkant_grootte
  gap = vierkant_grootte - 4
  for i in range (int(vierkanten)):
    rect(0, gap, lijnen, 8)
    gap = gap + vierkant_grootte
  
run()



