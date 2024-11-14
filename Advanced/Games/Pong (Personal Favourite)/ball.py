from turtle import Turtle

BOUNCE_ANGLE = 30
MAX_X = 450
MAX_Y = 350
speed = 10
move_speed = 2
move_speed_increments = 0.05
COLOR = "gold1"

class Ball(Turtle):
    def __init__(self, shape):
        super().__init__()
        self.speed("fastest")
        self.color(COLOR)
        self.shape(shape)
        self.penup()
        self.setpos(0, 0)
        self.game_start = True
        self.player_bounced = False

    def move(self):
        if self.game_start:
            self.setheading(BOUNCE_ANGLE)
            self.game_start = False
        self.forward(move_speed)

    def check_bounce(self, left_paddle, right_paddle):
        global move_speed
        xBob = self.xcor()
        yBob = self.ycor()
        # Right Paddle bounce check
        if xBob + 20 >= right_paddle.xcor() and xBob < right_paddle.xcor() + right_paddle.width:
            if yBob > right_paddle.ycor() - 65 and yBob < right_paddle.ycor() + 65:
                heading = self.heading()
                self.setheading(180 - heading)
                if right_paddle.is_player == True:
                    self.player_bounced = True
                else:
                    self.player_bounced = False
                move_speed += move_speed_increments
                return True

        # Left Paddle bounce check
        if xBob - 20 <= left_paddle.xcor() and xBob > left_paddle.xcor() - left_paddle.width:
            if yBob > left_paddle.ycor() - 65 and yBob < left_paddle.ycor() + 65:
                heading = self.heading()
                self.setheading(180 - heading)
                if left_paddle.is_player == True:
                    self.player_bounced = True
                else:
                    self.player_bounced = False
                move_speed += move_speed_increments
        if abs(yBob) >= MAX_Y:
            heading = self.heading()
            self.setheading(-heading)

    def reset(self):
        global move_speed
        self.game_start = True
        self.setpos(0, 0)
        move_speed = 2





