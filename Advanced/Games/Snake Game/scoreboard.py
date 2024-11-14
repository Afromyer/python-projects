from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        self.highscore = 0
        try:
            with open("highscore.txt", mode="r") as file:
                self.highscore = file.read()
        except:
            with open("highscore.txt", mode="w") as file:
                file.write("0")
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self, amount):
        self.score += amount
        self.update_scoreboard()
