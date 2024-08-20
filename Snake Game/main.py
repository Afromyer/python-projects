import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
shape = "circle"
snake = Snake(shape)
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_over = False
while not game_over:
    screen.update()
    time.sleep(0.005)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend(shape)
        scoreboard.increase_score(1)

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if abs(snake.head.xcor() - segment.xcor()) < 10 and abs(snake.head.ycor() - segment.ycor()) < 10:
            scoreboard.reset()
            snake.reset()

screen.mainloop()
