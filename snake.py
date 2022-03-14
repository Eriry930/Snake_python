from turtle import Turtle

#build snake body
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]

UP= 90
DOWN = 270
RIGTH = 0
LEFT = 180

class Snake:
    #Constructor
    def __init__(self):
         # save snake segments
        self.segments = []
        # method than created snake
        self.create_snake()
        #atributo cabeza
        self.head =self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITION:
            snake_segment = Turtle("turtle")
            snake_segment.color("black","purple")
            snake_segment.shapesize(outline=2)
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)

    def  create_my_snake(self):
      for position in STARTING_POSITION:
        self.add_segment (position)
    
    def add_segment(self, position): 
      my_snake_segment = Turtle ("turtle")
      my_snake_segment.color ("black","#9933FF")
      my_snake_segment.shapesize(outline=2)
      my_snake_segment.penup ()
      my_snake_segment.goto (position)
      self.segments.append (my_snake_segment)



    def extend (self):
      self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up (self):
      if self.head.heading() != DOWN:
        self.head. setheading(UP)


    def down (self):
      if self.head.heading() != UP:
        self.head. setheading(DOWN)

    def rigth (self):
      if self.head.heading() != LEFT:
        self.head. setheading(RIGTH)

    def left (self):
      if self.head.heading() != RIGTH:
        self.head. setheading(LEFT)


  # condicionales
