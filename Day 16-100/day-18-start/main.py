import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.shape("turtle")

turtle.colormode(255)
screen = Screen()
screen.tracer(0)
tim.hideturtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

import heroes
print(heroes.gen())

# import all
#from turtle import *

# aliases in imports
# import turtle as t



# draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# draw a dashed line
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# draw shapes on top of each other


# colors = [
#     "red", "orange", "yellow", "green", "blue",
#     "purple", "pink", "brown", "black", "gray",
#     "tomato", "gold", "lime green", "turquoise", "royal blue",
#     "medium orchid", "hot pink", "chocolate", "dark slate gray", "cornflower blue",
# ]

# Drawing an overlapping set of shapes pattern
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# directions = [0, 90, 180, 270]
# for i in range(500):
#     tim.pensize(10)
#     tim.color(random_color())
#     tim.speed("fastest")
#
#     heading = random.choice(directions)
#     tim.setheading(heading)
#     tim.forward(30)


def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)
        screen.update()

draw_spirograph(5)


screen.exitonclick()

