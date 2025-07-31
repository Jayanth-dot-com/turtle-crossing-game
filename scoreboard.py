from turtle import Turtle

FONT = ("Courier", 15, "bold")

class Scoreboard(Turtle):
    def __init__(self, cars):
        super().__init__()
        self.score = 0
        self.crash = cars
    def scorecard(self):
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.scoreboard()
    def scoreboard(self):
        self.clear()
        self.write(f"Level :{self.score}", False, "left", FONT)
    def increaseScore(self):
        self.score += 1
    def game_over(self):
        toby = Turtle()
        toby.color("black")
        toby.hideturtle()
        toby.penup()
        toby.write("GAME OVER", False, "center", ("Courier", 24, "bold"))