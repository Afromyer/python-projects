import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def turtle_cross():
    global level
    car.set_level(level)
    scoreboard.set_level(level)
    game_is_on = True
    while game_is_on:
        car.spawn_cars()
        car.move()

        time.sleep(0.01)
        screen.update()

        for visual_car in car.cars:
            if player.check_collision(visual_car):
                scoreboard.game_over()
                screen.onkey(restart, " ")
                game_is_on = False

        if player.ycor() >= 290:
            player.reset()
            level += 1
            car.set_level(level)
            scoreboard.set_level(level)


def restart():
    global level, car, player, scoreboard, game_is_on

    player.reset()
    level = 1
    scoreboard.lose.clear()
    scoreboard.clear()
    scoreboard.update_scoreboard()
    turtle_cross()


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("DarkOliveGreen1")

player = Player()
car = CarManager()
scoreboard = Scoreboard()


def scroll_up(event):
    player.up()


def scroll_down(event):
    player.down()


screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

# Get the underlying tkinter canvas
canvas = screen.getcanvas()

# Bind scroll wheel events
canvas.bind("<MouseWheel>", lambda event: scroll_up(event) if event.delta > 0 else scroll_down(event))  # For Windows

level = 1

turtle_cross()

screen.mainloop()
