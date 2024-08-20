import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1

#Higher = Less chance to spawn
DENSITY_CALCULATION_NUM = 100
LENGTH = 2
WIDTH = 1


class CarManager:
    def __init__(self):
        self.level = 1
        self.car_density = 5
        self.car_speed = 1
        self.cars = []

    def create_car(self):
        self.new_car = Turtle()
        self.new_car.shape('square')
        self.new_car.penup()
        self.new_car.setheading(180)
        self.new_car.speed("fastest")
        self.new_car.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.new_car.color(random.choice(COLORS))
        return self.new_car

    def move(self):
        for car in self.cars:
            car.forward(self.car_speed)
            if car.xcor() < -340:
                car.clear()
                car.hideturtle()
                self.cars.remove(car)
                del car


    def spawn_cars(self):
        numbers = []
        spawn_number = random.randint(1, DENSITY_CALCULATION_NUM)
        for i in range(self.car_density):
            random_number = random.randint(1, DENSITY_CALCULATION_NUM)
            numbers.append(random_number)

        for number in numbers:
            if number == spawn_number:
                x_pos = 300 + (20 * LENGTH)
                y_pos = random.randrange(-240, 240)
                car = self.create_car()
                car.setpos(x_pos, y_pos)
                self.cars.append(car)

    def set_level(self, level):
        if level == 1:
            self.car_speed = 1
            self.car_density = 2
        elif level == 2:
            self.car_speed = 2
            self.car_density = 3
        elif level == 3:
            self.car_speed = 2
            self.car_density = 5
        elif level == 4:
            self.car_speed = 3
            self.car_density = 10
        elif level == 5:
            self.car_speed = 3
            self.car_density = 15
        else:
            self.car_speed = 3
            self.car_density = 15
            self.car_density += 1
