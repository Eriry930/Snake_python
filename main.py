from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# board game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#6C0E47")
screen.title("Snake Game")
#disable default Turtle animation
screen.tracer(0)

my_snake = Snake()

#Creamos la manzana
apple= Food()

#creamos el objeto del tablero
scoreboard = ScoreBoard()

#almaceno los segmentos de la serpiente
segments = [] 

#Metodo de escucha de las teclas
screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.rigth, "Right")
screen.onkey(my_snake.left, "Left")



#snake animation
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    my_snake.move()


    # colision con la comida
    if my_snake.head.distance(apple) <15:
      apple.refresh()
      scoreboard.increase_score()
      my_snake.extend()

  #Detector de colisiones de paredes
    if my_snake.head.xcor () >299 or my_snake.head.xcor () < -299 or my_snake.head.ycor () > 299 or my_snake.head.ycor () < -299 :
      game_is_on = False
      scoreboard.game_over()

#Detector de colisiones con el cuerpo
    for segment in my_snake.segments:
      if segment == my_snake.head:
          pass 
      elif  my_snake.head.distance(segment) <10:
          game_is_on = False
          scoreboard.game_over()


screen.exitonclick()