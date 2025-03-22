import turtle

t = turtle.Turtle()

t.speed(0)

turtle.bgcolor("black")
t.pencolor("cyan")

t.pensize(2)

for i in range(100):
    t.forward(i*2)
    t.right(144)
turtle.done()

