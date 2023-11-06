import turtle
import colorsys

turt = turtle.Turtle()
NOWAY = turtle.Screen().bgcolor("black")
turt.speed(0)
count = 1

while count<100:
    c = colorsys.hsv_to_rgb(0,1,1)
    turt.color(c)
    turt.left(30)
    turt.circle(count)
    count = count + 1