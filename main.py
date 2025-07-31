import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager(player)
scoreboard = Scoreboard(car)

screen.listen()
screen.onkey(player.move, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.car()
    if player.finish():
        scoreboard.increaseScore()
        car.increaseSpeed()
    car.movement()
    scoreboard.scorecard()
    if car.collides():
        game_is_on = False
        scoreboard.game_over()
    screen.update()

screen.exitonclick()