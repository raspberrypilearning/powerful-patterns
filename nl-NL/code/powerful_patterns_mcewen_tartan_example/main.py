#!/bin/python3

from p5 import *


def setup():
    size(400, 400)


def draw():
    lines = 10 * frame_count # Gebruik de breedte/lengte van de vorm om in de loop van de tijd te animeren

    # McEwen tartan kleuren
    # Kleuren van de basisvierkanten
    BLAUW = Color(83, 143, 200)
    GREEN = Color(78, 163, 162)
    BASIS_KLEUREN = [GROEN, BLAUW]

    # Kruiskleuren
    GEEL = Color(155, 176, 135)
    ROOD = Color(155, 129, 113)
    KRUIS_KLEUREN = [GEEL, ROOD]

    # Kleur van het stiksel en overlappende kleur
    GRIJS = Color(78, 99, 86)

    # Teken afwisselend alle GROENE en BLAUWE basisvierkanten
    no_stroke()
    y_coördinaat = 0
    vierkanten = width/vierkant_grootte

    for i in range(int(vierkanten)):
        gap = 0
        for j in range(int(vierkanten)):
            fill(BASIS_KLEUREN[j % 2]) # GROEN en BLAUW
            rect(gap, y_coördinaat, vierkant_grootte, vierkant_grootte)
            opening = opening + vierkant_grootte
        y_coördinaat = y_coördinaat + vierkant_grootte

    # Kruizen
    stroke(GRIJS)

    # TEKEN afwisselend DE GELE en RODE kruizen
    for i in range(4):
        fill(GEEL)
        kruis = vierkant_grootte / 2 - 2
        for i in range(int(vierkanten/2)):
            fill(KRUIS_KLEUREN[1% 2]) #GEEL en ROOD
            rect(kruis, 0, 4, lijnen)
            rect(0, kruis, lijnen, 4)
            kruis = kruis + 2 * vierkant_grootte
        # Teken de stikkruisen
        no_fill()
        kruis = vierkant_grootte + vierkant_grootte / 2 - 2
        for i in range(int(vierkanten)):
            rect(kruis, 0, 4, lijnen)
            rect(0, kruis, lijnen, 4)
            kruis = kruis + * vierkant_grootte

    # Teken de grijze lijnen waar het materiaal overlapt
    no_stroke()
    fill(GRIJS, 100)
    gap = vierkant_grootte - 4
    for i in range(int(vierkanten)):
        rect(gap, 0, 8, lijnen)
        gap = gap + vierkant_grootte
    gap = vierkant_grootte - 4
    for i in range(int(vierkanten)):
        rect(0, gap, lijnen, 8)
        gap = gap + vierkant_grootte


print('🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁢󠁳󠁣󠁴󠁿 Dit is McEwen Tartan 🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁧󠁢󠁳󠁣󠁴󠁿')
vierkante_grootte = int(
    input('Welke maat 🏴󠁧󠁢󠁳󠁣󠁴󠁿tartan wil je graag hebben? 20, 50 of 100'))

run(frame_rate=10)
