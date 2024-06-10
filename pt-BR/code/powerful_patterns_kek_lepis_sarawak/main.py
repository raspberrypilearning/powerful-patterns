#!/bin/python3

from p5 import *
from time import *

# Baseado na incrível arte geométrica do bolo da Malásia: Kek lapis Sarawak


def quadrante():
    # Escolha algumas cores lindas para as camadas do bolo
    turquesa = Color(64, 224, 208)
    ouro = Color(255, 215, 0)
    tomate = Color(255, 99, 71)

    # Geleia gruda as camadas juntas
    geleia = Color(255, 165, 0)
    stroke(geleia)
    stroke_weight(2)  # Altere o número para alterar a quantidade de geleia

    #Nove camadas de bolo, repetindo as 3 cores 3 vezes
    for i in range(3):
        iniciar_y = i * 60  # altura de 3 blocos de bolo
        fill(turquesa)
        rect(0, iniciar_y, 180, 20)
        fill(ouro)
        rect(0, iniciar_y + 20, 180, 20)
        fill(tomate)
        rect(0, iniciar_y + 40, 180, 20)


def exterior():
    # O bolo é embrulhado em uma camada externa
    amareloverde = Color(154, 205, 50)

    no_fill()  # Não cubra os quadrantes do bolo!
    stroke(amareloverde)
    stroke_weight(20)
    rect(10, 10, 380, 380, 20)


def setup():
    size(400, 400)  # faça o bolo quadrado
    background(255, 255, 255, 0)  # fundo transparente


def draw():
    # Defina um quarto de volta para que nosso código seja fácil de ler
    quarto = radians(90)

    translate(200, 200)  # comece do centro

    # Faça o quadrado inferior direito do bolo e gire para os outros quadrados

    if frame_count <= 4:  # desenhar até 4 quadrantes
        for i in range(frame_count):
            quadrante()
            rotate(quarto)

    if frame_count == 5:  # adicione a camada externa
        translate(-200, -200)  # de volta ao canto superior
        exterior()  # camada externa


run(frame_rate=5)  # 5 quadros por segundo
