# import pygame
import turtle 
import random
import cv2

#loading image
img = cv2.imread('iron_man.jpg')
# for i in 
# colors = {}
# print(img[0][0])

	 


class Brush():

	pensize = 3.5

	def __init__(self,start_pos,offset,speed,color):
		#print("brush created")
		self.brush = turtle.Turtle()
		self.brush.speed(0)
		self.brush.shape("circle")
		self.brush.color(color[0],color[1],color[2])
		self.brush.penup()
		self.brush.goto(-(((start_pos[0] - 6.5*offset)//2) - self.pensize//2), start_pos[1]//2 - 20)
		self.brush.pensize(self.pensize)
		self.brush.hideturtle()
		self.brush.dy = speed
		self.brush.pendown()

	def move(self,speed):
		# print("moving")
		y = self.brush.ycor()
		y -= speed
		self.brush.sety(y)

#control variables
resolution = (1000,1000)

#initializing screen
wm = turtle.Screen()
wm.title("ARt")
wm.bgcolor("black")
wm.setup(width = resolution[0], height = resolution[1])
wm.tracer(0)
wm.colormode(255)

#paint
paint = []
speed = 1
for i in range(len(img[0])):
	paint.append(Brush(start_pos=(resolution[0], resolution[1]), offset = i, speed = speed, color = (img[0][i][2],img[0][i][1],img[0][i][0])))
	# speed = paint[i-1].brush.dy + (random.random() if paint[i-1].brush.dy <= 1 else (random.random()*random.randint(-1,2) if paint[i-1].brush.dy <= 2 else random.random()*-1))
	

#print("done")

#print(paint[:10])

# clock = pygame.time.Clock()
f = 1
rw = 1

for i in range(10000000):
	pass

while True:
	
	wm.update()


	# pygame.time.delay(50)
	# clock.tick(10)


	for i in range(len(paint)):
		speed = (random.random()*10)
		# paint[i].brush.write(str(i) if (i == len(paint)-1 or i == 0) else '1',align = "center", font = ("Courier", 11, "normal"))
		paint[i].move(speed)
		r,g,b = (img[rw][i][2],img[rw][i][1],img[rw][i][0])
		# if r > 50:
		# 	r, g = g, r
		paint[i].brush.color(r,g,b)

	rw += 1	
	# if f:
	# 	for i in paint[:10]:
	# 		print(i.brush.xcor())
	# 	f = 0

	#print("moved")
