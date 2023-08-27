import colorgram
import turtle as t
from random import choice

# Extract colors from image with colorgram
color_list = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    color_list.append((color.rgb.r,color.rgb.g,color.rgb.b))

# Draw the painting with turtle module
t.colormode(255)
tim = t.Turtle()
# set the speed and initial position of the turtle
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for _ in range(10):
    # draw a line of 10 dots
    for _ in range(10):
        tim.dot(20, choice(color_list))
        tim.forward(50)

    # reposition the turtle at the beginning of the line 50 pixel above
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen = t.Screen()
t.exitonclick()