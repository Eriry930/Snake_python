from turtle import Turtle

FONT = ("Arial", 20, "normal")
ALIGNMENT = "center"

class ScoreBoard (Turtle):

    def __init__(self):
      super().__init__()
      self.penup()
      self.score = 0
      self.goto(0,270)
      self.update_score()
      self.color ("white")
      self.hideturtle()

    def update_score (self):
      self.write( f"El puntaje es: {self.score}", font=FONT, align= ALIGNMENT)

    def increase_score(self):
      self.clear()
      self.score += 1
      self.update_score ()

    def game_over(self):
        self.clear()
        self.write("Game Over", font=FONT, align=ALIGNMENT)
      
      
