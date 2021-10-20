import turtle
#import os
import random

#control variables
resolution = 1080

#initializing screen
wm = turtle.Screen()
wm.title("ARt")
wm.bgcolor("black")
wm.setup(width = resolution, height = resolution)
wm.tracer(0)
#----

#paddle a
paddle_a = turtle.Turtle()
#not the speed of paddle but speed of animation.This command sets animation to 
#max possible speed
paddle_a.speed(0)
paddle_a.shape("circle")
paddle_a.color("red")
paddle_a.pendown()
paddle_a.goto(-350,0)
paddle_a.pensize(10)
paddle_a.hideturtle()
#paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.dy = 2

while True:
	wm.update()

	if paddle_a.ycor() < 100:
		y = paddle_a.ycor()
		y += paddle_a.dy
		paddle_a.sety(y)
