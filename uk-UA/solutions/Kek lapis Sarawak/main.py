#!/bin/python3

from draw import *
from time import *

# На основі дивовижного малайзійського мистецтва тортів з геометричними візерунками, що називається кек-ляпіс саравак

def quadrant():

  # Вибери декілька яскравих кольорів для шарів торта
  turquoise = color(64, 224, 208) # бірюзовий
  gold = color(255, 215, 0) # золотий
  tomato = color(255, 99, 71) # червоний
  
  # Джем скріплює шари між собою
  jam = color(255, 165, 0) 
  stroke(jam)
  stroke_weight(2) # Зміни число, щоб змінити кількість джему

  # Дев'ять шарів торта: 3 кольори повторюються тричі
  for i in range(3):
    start_y = i * 60 # висота трьох шарів торту
    fill(turquoise)
    rect(0, start_y, 180, 20)
    fill(gold)
    rect(0, start_y + 20, 180, 20)
    fill(tomato)
    rect(0, start_y + 40, 180, 20)

  
def outer():

  # Торт загорнутий у зовнішній шар
  yellowgreen = Color(154, 205, 50) 
  
  no_fill() # Не закривай середину торту
  stroke(yellowgreen)
  stroke_weight(20)
  rect(10, 10, 380, 380, 20) 


def setup():
  size(400, 400) # створи площину для торта
  background(255, 255, 255, 0) # прозорий фон
  frame_rate(5) # 5 кадрів за секунду


def draw():
  
  # Визнач чверті обороту, щоб твій код легко читався
  quarter = radians(90)

  translate(200, 200) # почни з центру
  
  # Зроби нижню праву четвертинку торта, потім по черзі інші четвертинки за допомогою обертання (функція rotate())

  if frame_count <= 4: # малює лише 4 четвертинки
    for i in range(frame_count): 
      quadrant()
      rotate(quarter)

  if frame_count == 5: # додає зовнішній шар
    translate(-200, -200) # назад у верхній кут
    outer() # зовнішній шар
    

run()
