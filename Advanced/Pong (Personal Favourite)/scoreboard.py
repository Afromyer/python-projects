from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Unispace", 50, "normal")
COLOR = "green"

class Scoreboard:

    def __init__(self):
        self.left_scoreboard = Turtle()
        self.right_scoreboard = Turtle()
        self.end_game = Turtle()

        self.end_game.color("snow")
        self.end_game.hideturtle()
        self.end_game.penup()

        self.divider = Turtle()
        self.divider.hideturtle()
        self.divider.penup()
        self.divider.color(COLOR)
        self.divider.speed("fastest")
        self.divider.setpos(0, 400)
        self.divider.setheading(270)
        self.divider.pensize(5)
        self.draw_divider()



        self.left_score = 0
        self.right_score = 0

        self.right_scoreboard.color(COLOR)
        self.left_scoreboard.color(COLOR)

        self.right_scoreboard.hideturtle()
        self.left_scoreboard.hideturtle()

        self.right_scoreboard.penup()
        self.left_scoreboard.penup()

        self.right_scoreboard.setpos(60, 260)
        self.left_scoreboard.setpos(-60, 260)

        self.update_left_score()
        self.update_right_score()


    def update_left_score(self):
        self.left_scoreboard.write(self.left_score, align=ALIGNMENT, font=FONT)

    def update_right_score(self):
        self.right_scoreboard.write(self.right_score, align=ALIGNMENT, font=FONT)

    def increase_score(self, side, amount):
        if side.lower() == "left":
            self.left_score += amount
            self.left_scoreboard.clear()
            self.update_left_score()
        elif side.lower() == "right":
            self.right_score += amount
            self.right_scoreboard.clear()
            self.update_right_score()

    def draw_divider(self):
        while self.divider.ycor() > -350:
            self.divider.forward(20)
            self.divider.penup()
            self.divider.forward(20)
            self.divider.pendown()

    def game_over(self):
        self.end_game.setpos(0, 0)
        self.end_game.write("GAME OVER", align=ALIGNMENT, font=FONT)
