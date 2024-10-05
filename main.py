# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
from random import choice

turtle.colormode(255)

color_list = [
    (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
    (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
    (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
    (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
    (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

tim = turtle.Turtle()
tim.hideturtle()


def move_x():
    x_pos = 50
    for _ in range(10):
        tim.dot(20, choice(color_list))
        tim.teleport(x_pos)
        x_pos += 50


y_pos = 50

for i in range(10):
    move_x()
    tim.teleport(0, y_pos)
    y_pos += 50


screen = turtle.Screen()
screen.exitonclick()
