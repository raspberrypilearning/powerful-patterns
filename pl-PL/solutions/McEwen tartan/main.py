#!/bin/python3

from p5 import *

def setup():
  size(400, 400)
  frame_rate(10)
  print('????????????????? To jest McEwen Tartan ??????????? ')
 
  global square_size
  square_size = int(input('What size 🏴󠁧󠁢󠁳󠁣󠁴󠁿tartan would you like? 20, 50 lub 100'))
  
def draw():
  
  lines = 10 * frame_count # Use in shape width/length to animate over time
  
  # Kolory tartanowe McEwen
  # Podstawowe kolory kwadratowe
  BLUE = color(83, 143, 200)
  GREEN = color(78, 163, 162)
  BASE_COLOURS = [ZIELONY, NIEBIESKI]
  
  # Kolory krzyżowe
  YELLOW = color(155, 176, 135)
  RED = color(155, 129, 113)
  CROSS_COLOURS = [ŻÓŁTY, CZERWONY]
  
  # Kolory łączenia i nakładania się
  GREY = color(78, 99, 86)
  
  # Rysuj wszystkie ZIELONE i NIEBIESKIE naprzemienne kwadraty bazy
  no_stroke()
  y_coordinate = 0
  kwadraty = szerokość/kwadrat_rozmiar
  
  for i in range (int(squares)):
    przerwa = 0
    for j in range (int(squares)):
      fill(BASE_COLORS[j % 2]) # GREEN and BLUE 
      rect(przerwa, y_współrzędna, kwadrat_size, kwadrat_size)
      przerwa = przerwa + kwadrat_size
    y_coordinate = y_coordinate + square_size
  
  # Krzyże
  Stroke(SZARY)
 
  # NARYSUJ ŻÓŁTE i CZERWONE krzyże naprzemienne
  for i in range (4):
    Wypełnienie(ŻÓŁTY)
    krzyżyk = kwadrat_size / 2 - 2 
    for i in range (int(squares/2)):
      fill(CROSS_COLORS[i % 2]) # YELLOW and RED
      rect(krzyżyk, 0, 4, linie)  
      rect(0, krzyżyk, linie, 4) 
      krzyżyk = krzyżyk + 2 * kwadrat_size
    # Rysuj krzyże szwów
    no_fill() 
    krzyżyk = kwadrat_size + kwadrat_size / 2 - 2
    for i in range (int(squares)): 
      rect(krzyżyk, 0, 4, linie) 
      rect(0, krzyżyk, linie, 4)
      krzyżyk = krzyżyk + kwadrat_size

  # Narysuj szare linie, w których materiał się nakłada
  no_stroke()
  Wypełnienie(SZARY, 100)
  przerwa = kwadrat_size - 4
  for i in range (int(squares)):
    rect(przerwa, 0, 8, linie)
    przerwa = przerwa + kwadrat_size
  przerwa = kwadrat_size - 4
  for i in range (int(squares)):
    rect(0, przerwa, linie, 8)
    przerwa = przerwa + kwadrat_size
  
run()



