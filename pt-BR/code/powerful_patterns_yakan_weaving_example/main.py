#!/bin/python3

from p5 import *
from math import random


def motivo():
    tamanho_motivo = 100

    # Define cores
    LARANJA = Color(254, 96, 1)
    ROXO = Color(135, 18, 192)
    AMARELO = Color(243, 200, 19)
    AZUL = Color(83, 171, 176)

    # Quadrados
    fill(LARANJA)
    rect(0, 0, tamanho_motivo/2, tamanho_motivo/2)
    fill(ROXO)
    rect(50, 0, tamanho_motivo/2, tamanho_motivo/2)
    fill(AMARELO)
    rect(0, 50, tamanho_motivo/2, tamanho_motivo/2)
    fill(AZUL)
    rect(50, 50, tamanho_motivo/2, tamanho_motivo/2)
    fill(ROXO)
    rect(0, 0, tamanho_motivo/4, tamanho_motivo/4)
    fill(LARANJA)
    rect(50, 0, tamanho_motivo/4, tamanho_motivo/4)
    fill(AZUL)
    rect(0, 50, tamanho_motivo/4, tamanho_motivo/4)
    fill(AMARELO)
    rect(50, 50, tamanho_motivo/4, tamanho_motivo/4)


def girar_motivo():
    for forma in range(5):  # linha de formas
        push_matrix()  # salvar configurações
        rotate(radians(45))  # vire a forma 45 graus
        motivo()
        pop_matrix()  # voltar para as configurações salvas
        translate(largura_motivo, 0)  # mover horizontalmente


def setup():
    size(400, 400)
    background(250, 5, 94)  # rosa
    no_stroke()
    print('Isso é 🇵🇭 tecelagem Yakan')


def draw():
    global largura_motivo
    largura_motivo = 150

    translate(-largura_motivo/2, -largura_motivo/2)  # para começar com metade dos motivos

    if frame_count < 20:  # linhas máximas
        for linha in range(frame_count):
            girar_motivo()
            if linha / 2 == 0:  # para compensar o padrão na próxima linha
                translate(-largura_motivo * 5 + 75, 80)
            else:
                translate(-largura_motivo * 5 - 75, 80)


run(frame_rate=3)
