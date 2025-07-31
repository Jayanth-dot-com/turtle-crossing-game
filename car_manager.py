from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self, player):
        self.cars_list = []
        self.STARTING_MOVE_DISTANCE = 5
        self.x_cor = 300
        self.player = player
    def car(self):
        if random.randint(1, 6) == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(300, random.randint(-250, 250))
            car.setheading(180)
            self.cars_list.append(car)
    def movement(self):
        for i in range(len(self.cars_list)):
            self.cars_list[i].forward(self.STARTING_MOVE_DISTANCE)
    def collides(self):
        for i in self.cars_list:
            x_distance = abs(i.xcor() - self.player.xcor())
            y_distance = abs(i.ycor() - self.player.ycor())
            if x_distance < 20 and y_distance < 20:
                return True
    def increaseSpeed(self):
        self.STARTING_MOVE_DISTANCE += 5