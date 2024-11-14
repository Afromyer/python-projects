import time
import turtle
from turtle import Turtle
import math

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 1
SEGMENT_WIDTH = 20
SEGMENT_HEIGHT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def segment_up(segment):
    segment.setheading(UP)


def segment_down(segment):
    segment.setheading(DOWN)


def segment_left(segment):
    segment.setheading(LEFT)


def segment_right(segment):
    segment.setheading(RIGHT)


up_clicked = False
down_clicked = False
left_clicked = False
right_clicked = False

buttons = {
    "up": up_clicked,
    "down": down_clicked,
    "left": left_clicked,
    "right": right_clicked,
}

segment_directions = {
    "up": segment_up,
    "down": segment_down,
    "left": segment_left,
    "right": segment_right,
}


def set_button_clicked(button_clicked):
    for button in buttons:
        if button == button_clicked:
            buttons[button] = True
        else:
            buttons[button] = False


def round_up_to_multiple(number, multiple):
    """
    Rounds up the given number to the nearest multiple.

    Args:
        number (int): The number to be rounded.
        multiple (int): The desired multiple.

    Returns:
        int: The rounded-up value.
    """

    remainder = number % multiple
    if remainder == 0:
        return number
    else:
        new_coord = number + (multiple - remainder)
        return new_coord
class Snake:
    def __init__(self, shape):
        self.segments = []
        self.create_snake(shape)
        self.segments[0].is_head = True
        self.head = self.segments[0]
        self.input_received = False
        self.has_end_added = False
        self.end_segment_turn_points = {}

    def create_snake(self, shape):
        self.turn_points = {}
        for position in STARTING_POSITIONS:
            self.add_segment(position, shape)

    def add_segment(self, position, shape):
        new_segment = Segment(shape)
        new_segment.set_position(position)
        self.segments.append(new_segment)

    def extend(self, shape):
        last_segment = self.segments[-1]
        last_segment_heading = last_segment.heading()
        last_segment_x = last_segment.xcor()
        last_segment_y = last_segment.ycor()
        new_segment_end = Segment(shape)
        self.segments.append(new_segment_end)
        if len(last_segment.turn_points) != 0:
            for point in last_segment.turn_points:
                new_segment_end.turn_points[point] = last_segment.turn_points[point]
        if last_segment_heading == UP:
            new_segment_end.setheading(UP)
            new_segment_end.setpos((last_segment_x, last_segment_y - 20))
        elif last_segment_heading == DOWN:
            new_segment_end.setheading(DOWN)
            new_segment_end.setpos((last_segment_x, last_segment_y + 20))
        elif last_segment_heading == LEFT:
            new_segment_end.setheading(LEFT)
            new_segment_end.setpos((last_segment_x + 20, last_segment_y))
        elif last_segment_heading == RIGHT:
            new_segment_end.setheading(RIGHT)
            new_segment_end.setpos((last_segment_x - 20, last_segment_y))
        self.has_end_added = True

    def move(self):
        self.head.forward(MOVE_DISTANCE)
        for segment in self.segments[1:]:
            segment.check_turn_point()
            segment.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == DOWN:
            head_coordinate = self.head.pos()
            new_x_coordinate = round_up_to_multiple(head_coordinate[0], 20)
            new_y_coordinate = self.head.pos()[1]
            new_coordinate = (new_x_coordinate, new_y_coordinate)
            self.head.setheading(UP)
            set_button_clicked("up")
            self.update_segment_turn_points(head_coordinate, segment_up)

    def down(self):
        if not self.head.heading() == UP:
            head_coordinate = self.head.pos()
            new_x_coordinate = round_up_to_multiple(head_coordinate[0], 20)
            new_y_coordinate = self.head.pos()[1]
            new_coordinate = (new_x_coordinate, new_y_coordinate)
            self.head.setheading(DOWN)
            set_button_clicked("down")
            self.update_segment_turn_points(head_coordinate, segment_down)

    def left(self):
        if not self.head.heading() == RIGHT:
            head_coordinate = self.head.pos()
            new_x_coordinate = self.head.pos()[0]
            new_y_coordinate = round_up_to_multiple(head_coordinate[1], 20)
            new_coordinate = (new_x_coordinate, new_y_coordinate)
            self.head.setheading(LEFT)
            set_button_clicked("left")
            self.update_segment_turn_points(head_coordinate, segment_left)

    def right(self):
        if not self.head.heading() == LEFT:
            head_coordinate = self.head.pos()
            new_x_coordinate = self.head.pos()[0]
            new_y_coordinate = round_up_to_multiple(head_coordinate[1], 20)
            new_coordinate = (new_x_coordinate, new_y_coordinate)
            self.head.setheading(RIGHT)
            set_button_clicked("right")
            self.update_segment_turn_points(head_coordinate, segment_right)

    def update_segment_turn_points(self, turn_coordinate, turn_function):
        for segment in self.segments[1:]:
            segment.turn_points[turn_coordinate] = turn_function

    def distance(self, something):
        return turtle.distance(something)

    def reset(self):
        for seg in self.segments:
            seg.setpos((700, 700))
        self.segments.clear()
        self.create_snake('circle')
        self.head = self.segments[0]



class Segment:
    def __init__(self, shape):
        self.create_segment(shape)
        self.is_head = False
        self.turn_points = {}
        self.is_moving = True

    def create_segment(self, shape):
        self.new_segment = Turtle(shape)
        self.new_segment.color("red")
        self.new_segment.speed("fastest")
        self.new_segment.penup()

    def hideturtle(self):
        self.hideturtle()

    def set_position(self, position):
        self.new_segment.setpos(position)

    def heading(self):
        return self.new_segment.heading()

    def pos(self):
        return self.new_segment.pos()

    def setpos(self, coordinate):
        self.new_segment.setpos(coordinate)

    def setheading(self, to_angle: float):
        return self.new_segment.setheading(to_angle)

    def move(self):
        self.is_moving = True

    def xcor(self):
        return self.new_segment.xcor()

    def ycor(self):
        return self.new_segment.ycor()

    def forward(self, distance):
        if self.is_moving:
            self.new_segment.forward(distance)

    def stop(self):
        self.is_moving = False

    def distance(self, turtle):
        return self.new_segment.distance(turtle)

    def change_direction(self, turn_fun):
        turn_fun(self.new_segment)

    def check_turn_point(self):
        coordinates = list(self.turn_points.keys())
        functions = list(self.turn_points.values())
        if len(self.turn_points) != 0:
            if self.new_segment.pos() == coordinates[0]:
                self.change_direction(functions[0])
                self.turn_points.pop(coordinates[0])


