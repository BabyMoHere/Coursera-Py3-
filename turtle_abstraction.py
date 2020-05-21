import turtle # importing the module
wn = turtle.Screen() # the dot operator is used to connect the module name with an item  that is in the module
wn.bgcolor("black")
guku = turtle.Turtle() # 
guku.color("green")
guku.shape("turtle") # cjhanging the shape of an arrow :D
guku.pensize(15)
distance = 30
angle = 90
guku.speed(10)
guku.up() # so it does nnot live the trace
for _ in range(15):
	guku.stamp() #point a place on the screen
	guku.forward(distance)
	guku.right(angle)
	distance += 10
	angle += -3
lara = turtle.Turtle()
lara.color("pink")
lara.pensize(2)
lara.shape("square")
distance = 30
angle = 90
lara.speed(3)
for _ in range(15):
	lara.forward(distance)
	lara.right(angle)
	distance += 10
	angle += -3
jamal = turtle.Turtle()
jamal.color("yellow")
jamal.pensize(10)
jamal.speed(5)
jamal.up()
for _ in range(10):
	jamal.forward(220)
	jamal.stamp()
	jamal.forward(-220)
	jamal.right(36)
tutu = turtle.Turtle()
tutu.color("green")
tutu.left(90)
tutu.forward(280)
tutu.heading() # puttin tutu in the starting position
tutu.fillcolor("blue") # setting the color of the filling
tutu.begin_fill() # starting to fill
for _ in range(4):
	tutu.forward(90)
	tutu.right(90)
tutu.end_fill() # ending to fill
tutu.left(90)
tutu.forward(90)
tutu.fillcolor("orange")
tutu.begin_fill()
tutu.circle(40)
tutu.end_fill()
wn.exitonclick()