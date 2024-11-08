from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.setpos(-200, 250)
        self.update_scoreboard()

        self.lose = Turtle()
        self.lose.color("black")
        self.lose.hideturtle()
        self.lose.penup()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.lose.setpos(0, 0)
        self.lose.write("GAME OVER\nPress 'space' to restart", align=ALIGNMENT, font=FONT)

    def set_level(self, amount):
        self.level = amount
        self.clear()
        self.update_scoreboard()
