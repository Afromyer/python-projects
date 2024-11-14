import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(900, 700)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

left_paddle = Paddle("left", "firebrick")
right_paddle = Paddle("right", "DodgerBlue")
ball = Ball("circle")
scoreboard = Scoreboard()

game_over = False
right_paddle.control(screen)
has_reset = True
player_bounced = False

# Main game loop
while not game_over:

    #Check for bounces
    player_bounced = ball.check_bounce(left_paddle, right_paddle)
    if player_bounced:
        has_reset = False

    #When the opponent can move
    if ball.player_bounced and ball.xcor() < 0:
        left_paddle.move(ball, 4)

    #Give scores
    if ball.xcor() >= 450:
        scoreboard.increase_score("left", 1)
        ball.reset()
        has_reset = True
    elif ball.xcor() <= -450:
        scoreboard.increase_score("right", 1)
        ball.reset()
        has_reset = True

    ball.move()
    if not has_reset:
        time.sleep(0.002)
    else:
        time.sleep(0.005)

    if scoreboard.right_score == 12 or scoreboard.left_score == 12:
        scoreboard.game_over()
        game_over = True
    screen.update()  # Manually update the screen

screen.mainloop()
