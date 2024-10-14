import turtle
import colorsys

# set up the screen and turtle object
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)

# Number of colors in the design
n = 36
h = 0

# Draw the multi-spring pattern
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.color(c)
    t.left(10)
    t.forward(i * 0.5)
    t.circle(50, 180)
    h += 1/n # Change hue for each iteration to get different colors

turtle.done()