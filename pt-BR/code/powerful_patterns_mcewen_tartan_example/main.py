#!/bin/python3

from p5 import *


def setup():
    size(400, 400)


def draw():
    linhas = 10 * frame_count # Use na largura/comprimento da forma para animar ao longo do tempo

    # Cores tartan McEwen
    # Cores quadradas básicas
    AZUL = Color(83, 143, 200)
    VERDE = Color(78, 163, 162)
    CORES_BASE = [VERDE, AZUL]

    # Cores cruzadas
    AMARELO = Color(155, 176, 135)
    VERMELHO = Color(155, 129, 113)
    CRUZ_CORES = [AMARELO, VERMELHO]

    # Costura e cor de sobreposição
    CINZA = Color(78, 99, 86)

    # Desenhe todos os quadrados alternados de base VERDE e AZUL
    no_stroke()
    y_coordenada = 0
    quadrados = width/tamanho_quadrado

    for i in range(int(quadrados)):
        espaco = 0
        for j in range(int(quadrados)):
            fill(CORES_BASE[j % 2])  # VERDE e AZUL
            rect(espaco, y_coordenada, tamanho_quadrado, tamanho_quadrado)
            espaco = espaco + tamanho_quadrado
        y_coordenada = y_coordenada + tamanho_quadrado

    # Cruzes
    stroke(CINZA)

    # Desenhe as cruzes alternadas AMARELO e VERMELHO
    for i in range(4):
        fill(AMARELO)
        cruz = tamanho_quadrado / 2 - 2
        for i in range(int(quadrados/2)):
            fill(CRUZ_CORES[i % 2])  # AMARELO e VERMELHO
            rect(cruz, 0, 4, linhas)
            rect(0, cruz, linhas, 4)
            cruz = cruz + 2 * tamanho_quadrado
        # Desenhe as cruzes de costura
        no_fill()
        cruz = tamanho_quadrado + tamanho_quadrado / 2 - 2
        for i in range(int(quadrados)):
            rect(cruz, 0, 4, linhas)
            rect(0, cruz, linhas, 4)
            cruz = cruz + tamanho_quadrado

    # Desenhe as linhas cinzas onde o material se sobrepõe
    no_stroke()
    fill(CINZA, 100)
    espaco = tamanho_quadrado - 4
    for i in range(int(quadrados)):
        rect(espaco, 0, 8, linhas)
        espaco = espaco + tamanho_quadrado
    espaco = tamanho_quadrado - 4
    for i in range(int(quadrados)):
        rect(0, espaco, linhas, 8)
        espaco = espaco + tamanho_quadrado


print('🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁢󠁳󠁣󠁴󠁿 Este é McEwen Tartan 🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁧󠁢󠁳󠁣󠁴󠁿')
tamanho_quadrado = int(
    input('Qual tamanho de 🏴󠁧󠁢󠁳󠁣󠁴󠁿 tartan você gostaria? 20, 50 ou 100'))

run(frame_rate=10)
