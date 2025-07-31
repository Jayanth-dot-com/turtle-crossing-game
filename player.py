from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.y_cor = -280
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
    def move(self):
        self.forward(10)
    def finish(self):
        if self.ycor() > 280:
            self.reset()
            self.penup()
            self.goto(STARTING_POSITION)
            self.left(90)
            return True