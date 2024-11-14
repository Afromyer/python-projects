import turtle
from turtle import Turtle, Screen

import random

tim = Turtle()

turtle.colormode(255)

def turn_left():
    tim.left(90)


def turn_right():
    tim.right(90)


def move_forward():
    global move_amount
    tim.forward(move_amount)


def move_backward():
    global move_amount
    tim.backward(move_amount)

screen = Screen()
def random_move():
    global screen
    screen_width = screen.canvwidth
    screen_height = screen.canvheight
    movement = random.choice(movements)
    movement()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

movements = [turn_left, turn_right, move_forward, move_backward]

tim.speed("fastest")
tim.pensize(10)
move_amount = 30
while True:
    random_move()
    tim.color(random_color())
