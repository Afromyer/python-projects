from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color("brown")
        self.setheading(90)
        self.setpos(STARTING_POSITION)
        self.speed("fastest")

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)

    def check_collision(self, car):
        # Get the player's position and size
        player_x, player_y = self.pos()
        player_size = 20

        # Get the car's position
        car_x, car_y = car.pos()

        # Define car dimensions
        car_width = 40
        car_height = 20

        # Calculate the boundaries
        player_left = player_x - player_size / 2
        player_right = player_x + player_size / 2
        player_top = player_y + player_size / 2
        player_bottom = player_y - player_size / 2

        car_left = car_x - car_width / 2
        car_right = car_x + car_width / 2
        car_top = car_y + car_height / 2
        car_bottom = car_y - car_height / 2

        # Check for overlap
        if (player_left < car_right and player_right > car_left and
                player_top > car_bottom and player_bottom < car_top):
            return True

        return False

    def reset(self):
        self.setpos(STARTING_POSITION)
