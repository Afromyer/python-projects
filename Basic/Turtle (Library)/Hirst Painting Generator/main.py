import random
import turtle

import colorgram
import turtle as t

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()
s = t.Screen()
turtle.colormode(255)
start_x_position = -1 * (s.canvwidth / 2)
start_y_position = -1 * (s.canvheight)
tim.teleport(start_x_position, start_y_position)
tim.speed("fastest")
tim.hideturtle()
def draw_dots(dot_size, gap, row_count, column_count):
    for i in range(row_count):
        initial_position = tim.pos()
        print(initial_position)
        for j in range(column_count):
            color = random.choice(color_list)
            tim.dot(dot_size, color)
            tim.penup()
            tim.teleport(tim.pos()[0] + gap)
        new_x_position = start_x_position
        new_y_position = initial_position[1] + gap
        tim.teleport(new_x_position, new_y_position)


draw_dots(20, 50, 10, 10)
s.mainloop()

