#!/bin/python3

from p5 import *
from random import randint

def motivo():
    global tamanho_circulo
    for i in range(5):
        ellipse(0, 0, tamanho_circulo / 5 * (5 - i), tamanho_circulo / 5 * (5  - i)) 

def setup():
    size(400, 400)
    print('🖌 Esta arte usa muitos círculos!')
    
    global tamanho_circulo
    
    tamanho_circulo = 50
  
def draw():
    # Cores do padrão
    stroke(40, 35, 100)  # azul
    stroke_weight(2)  # borda grossa
    fill(200, 180, 128)  # ouro
    
    translate(0,0)  # comece no canto superior esquerdo da tela
    
    if frame_count <= 16:  # cria 16 linhas e depois pare
        for row in range (frame_count):  # anima 1 linha de cada vez
            for shape in range (16):  # criar uma linha por vez de motivos
                motivo()
                translate(tamanho_circulo / 2, 0)
            translate(-width, tamanho_circulo / 2)  # mover para baixo para iniciar a próxima linha
  
run(frame_rate=3)
