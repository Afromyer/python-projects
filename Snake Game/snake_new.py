from turtle import Turtle
import math

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0), (-100, 0), (-120, 0), (-140, 0), (-160, 0),
                      (-180, 0)]
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


class NewSnake:
    def __init__(self, shape):
        self.segments = []
        self.create_snake(shape)
        self.segments[0].is_head = True
        self.head = self.segments[0]
        self.input_received = False

    def create_snake(self, shape):
        self.turn_points = {}
        for position in STARTING_POSITIONS:
            new_segment = Segment(shape)
            new_segment.set_position(position)
            new_segment.move_sequence = self.turn_points
            self.segments.append(new_segment)

    def move(self):
        self.head.forward(MOVE_DISTANCE)
        for segment in self.segments[1:]:
            segment.forward(MOVE_DISTANCE)
            segment.check_turn_point()

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

    def adjust_position(self):
        current_heading = self.head.heading()
        current_x, current_y = self.head.pos()

        if current_heading == UP or current_heading == DOWN:
            new_x = round_up_to_multiple(current_x, 20)
            if current_heading == UP:
                new_y = math.ceil(current_y / 20) * 20
            else:  # DOWN
                new_y = math.floor(current_y / 20) * 20
        else:  # LEFT or RIGHT
            new_y = round_up_to_multiple(current_y, 20)
            if current_heading == RIGHT:
                new_x = math.ceil(current_x / 20) * 20
            else:  # LEFT
                new_x = math.floor(current_x / 20) * 20

        # Calculate the difference to move all segments
        dx = new_x - current_x
        dy = new_y - current_y

        # Move all segments, including the head
        for segment in self.segments:
            current_segment_x, current_segment_y = segment.pos()
            segment.setpos(current_segment_x + dx, current_segment_y + dy)

        # Update turn points
        new_turn_points = {}
        for coord, turn_func in self.turn_points.items():
            new_coord = (coord[0] + dx, coord[1] + dy)
            new_turn_points[new_coord] = turn_func
        self.turn_points = new_turn_points

        # Update turn points for all segments
        for segment in self.segments[1:]:
            new_segment_turn_points = {}
            for coord, turn_func in segment.turn_points.items():
                new_coord = (coord[0] + dx, coord[1] + dy)
                new_segment_turn_points[new_coord] = turn_func
            segment.turn_points = new_segment_turn_points

    def update_segment_turn_points(self, turn_coordinate, turn_function):
        for segment in self.segments[1:]:
            segment.turn_points[turn_coordinate] = turn_function


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

    def forward(self, distance):
        if self.is_moving:
            self.new_segment.forward(distance)

    def stop(self):
        self.is_moving = False

    def change_direction(self, turn_fun):
        turn_fun(self.new_segment)

    def check_turn_point(self):
        coordinates = list(self.turn_points.keys())
        if len(self.turn_points) != 0:
            if self.new_segment.pos() == coordinates[0]:
                self.change_direction(self.turn_points[coordinates[0]])
