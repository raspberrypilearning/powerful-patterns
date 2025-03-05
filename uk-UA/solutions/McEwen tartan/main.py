#!/bin/python3

from p5 import *

def setup():
  size(400, 400)
  frame_rate(10)
  print('🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁢󠁳󠁣󠁴󠁿 Це тартан шотландського клану Макʼюенів 🏴󠁧󠁢󠁳󠁣󠁴󠁿󠁧󠁢󠁳󠁣󠁴󠁿')
 
  global square_size
  square_size = int(input('Який має бути розмір 🏴󠁧󠁢󠁳󠁣󠁴󠁿тартану? 20, 50 або 100'))
  
def draw():
  
  lines = 10 * frame_count # Використовуй під час визначення ширини й довжини фігури для поступової анімації
  
  # Кольори тартану клану Макʼюєнів
  # Кольори квадратів основи
  BLUE = color(83, 143, 200) # блакитний
  GREEN = color(78, 163, 162) # зелений
  BASE_COLORS = [GREEN, BLUE]
  
  # Кольори перетинів
  YELLOW = color(155, 176, 135) # жовтий
  RED = color(155, 129, 113) # червоний
  CROSS_COLORS = [YELLOW, RED]
  
  # Колір швів та накладання
  GREY = color(78, 99, 86) # сірий
  
  # Намалюй квадрати основи за допомогою GREEN та BLUE
  no_stroke()
  y_coordinate = 0
  squares = width/square_size
  
  for i in range (int(squares)):
    gap = 0
    for j in range (int(squares)):
      fill(BASE_COLORS[j % 2]) # GREEN і BLUE (зелений і блакитний) 
      rect(gap, y_coordinate, square_size, square_size)
      gap = gap + square_size
    y_coordinate = y_coordinate + square_size
  
  # Перетини
  stroke(GREY)
 
  # Малює перехрестя жовтого і червоного кольорів (YELLOW і RED)
  for i in range (4):
    fill(YELLOW)
    cross = square_size / 2 - 2 
    for i in range (int(squares/2)):
      fill(CROSS_COLORS[i % 2]) # YELLOW і RED (жовтий і червоний)
      rect(cross, 0, 4, lines)  
      rect(0, cross, lines, 4) 
      cross = cross + 2 * square_size
    # Намалюй перетини для швів
    no_fill() 
    cross = square_size + square_size / 2 - 2
    for i in range (int(squares)): 
      rect(cross, 0, 4, lines) 
      rect(0, cross, lines, 4)
      cross = cross + square_size

  # Намалюй сірі лінії, де матеріал нашаровується
  no_stroke()
  fill(GREY, 100)
  gap = square_size - 4
  for i in range (int(squares)):
    rect(gap, 0, 8, lines)
    gap = gap + square_size
  gap = square_size - 4
  for i in range (int(squares)):
    rect(0, gap, lines, 8)
    gap = gap + square_size
  
run()



