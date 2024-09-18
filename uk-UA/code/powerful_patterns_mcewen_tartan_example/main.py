#!/bin/python3

from p5 import *


def setup():
    size(400, 400)


def draw():
    lines = 10 * frame_count  # Use in shape width/length to animate over time

    # Кольори Тартана Макьюєна
    # Базові кольори квадратів
    BLUE = Color(83, 143, 200)
    GREEN = Color(78, 163, 162)
    BASE_COLORS = [GREEN, BLUE]

    # Кольори перетинів
    YELLOW = Color(155, 176, 135)
    RED = Color(155, 129, 113)
    CROSS_COLORS = [YELLOW, RED]

    # Колір швів та накладання
    GREY = Color(78, 99, 86)

    # Намалюй основу за допомогою GREEN та BLUE квадратів, які чергуються між собою
    no_stroke()
    y_coordinate = 0
    squares = width/square_size

    for i in range(int(squares)):
        gap = 0
        for j in range(int(squares)):
            fill(BASE_COLORS[j % 2])  # GREEN and BLUE
            rect(gap, y_coordinate, square_size, square_size)
            gap = gap + square_size
        y_coordinate = y_coordinate + square_size

    # Перетини
    stroke(GREY)

    # DRAW THE YELLOW and RED alternating crosses
    for i in range(4):
        fill(YELLOW)
        cross = square_size / 2 - 2
        for i in range(int(squares/2)):
            fill(CROSS_COLORS[i % 2])  # YELLOW and RED
            rect(cross, 0, 4, lines)
            rect(0, cross, lines, 4)
            cross = cross + 2 * square_size
        # Draw the stiching crosses
        no_fill()
        cross = square_size + square_size / 2 - 2
        for i in range(int(squares)):
            rect(cross, 0, 4, lines)
            rect(0, cross, lines, 4)
            cross = cross + square_size

    # Намалюй сірі лінії в місцях перекриття матеріалів
    no_stroke()
    fill(GREY, 100)
    gap = square_size - 4
    for i in range(int(squares)):
        rect(gap, 0, 8, lines)
        gap = gap + square_size
    gap = square_size - 4
    for i in range(int(squares)):
        rect(0, gap, lines, 8)
        gap = gap + square_size


print('🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁢󠁳󠁣󠁴󠁿 This is McEwen Tartan 🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁧󠁢󠁳󠁣󠁴󠁿')
square_size = int(
    input('What size 🏴󠁧󠁢󠁳󠁣󠁴󠁿tartan would you like? 20, 50 або 100'))

run(frame_rate=10)
