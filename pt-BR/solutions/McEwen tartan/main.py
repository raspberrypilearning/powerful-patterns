#!/bin/python3

from p5 import *

def setup():
  size(400, 400)
  frame_rate(10)
  print('🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁢󠁳󠁣󠁴󠁿 Este é McEwen Tartan 🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁧󠁢󠁳󠁣󠁴󠁿')
 
  global square_size
  square_size = int(input('What size 🏴󠁧󠁢󠁳󠁣󠁴󠁿tartan would you like? 20, 50 ou 100'))
  
def draw():
  
  lines = 10 * frame_count # Use in shape width/length to animate over time
  
  # Cores tartan McEwen
  # Cores quadradas básicas
  BLUE = color(83, 143, 200)
  GREEN = color(78, 163, 162)
  CORES_BASE = [VERDE, AZUL]
  
  # Cores cruzadas
  YELLOW = color(155, 176, 135)
  RED = color(155, 129, 113)
  CRUZ_CORES = [AMARELO, VERMELHO]
  
  # Costura e cor de sobreposição
  GREY = color(78, 99, 86)
  
  # Desenhe todos os quadrados alternados de base VERDE e AZUL
  no_stroke()
  y_coordenada = 0
  quadrados = width/tamanho_quadrado
  
  for i in range (int(squares)):
    espaco = 0
    for j in range (int(squares)):
      fill(BASE_COLORS[j % 2]) # GREEN and BLUE 
      rect(espaco, y_coordenada, tamanho_quadrado, tamanho_quadrado)
      espaco = espaco + tamanho_quadrado
    y_coordenada = y_coordenada + tamanho_quadrado
  
  # Cruzes
  stroke(CINZA)
 
  # Desenhe as cruzes alternadas AMARELO e VERMELHO
  for i in range (4):
    fill(AMARELO)
    cruz = tamanho_quadrado / 2 - 2 
    for i in range (int(squares/2)):
      fill(CROSS_COLORS[i % 2]) # YELLOW and RED
      rect(cruz, 0, 4, linhas)  
      rect(0, cruz, linhas, 4) 
      cruz = cruz + 2 * tamanho_quadrado
    # Desenhe as cruzes de costura
    no_fill() 
    cruz = tamanho_quadrado + tamanho_quadrado / 2 - 2
    for i in range (int(squares)): 
      rect(cruz, 0, 4, linhas) 
      rect(0, cruz, linhas, 4)
      cruz = cruz + tamanho_quadrado

  # Desenhe as linhas cinzas onde o material se sobrepõe
  no_stroke()
  fill(CINZA, 100)
  espaco = tamanho_quadrado - 4
  for i in range (int(squares)):
    rect(espaco, 0, 8, linhas)
    espaco = espaco + tamanho_quadrado
  espaco = tamanho_quadrado - 4
  for i in range (int(squares)):
    rect(0, espaco, linhas, 8)
    espaco = espaco + tamanho_quadrado
  
run()



