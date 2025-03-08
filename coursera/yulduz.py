import turtle 

# Ekran yaratish 
wn = turtle.Screen()
wn.bgcolor("black")

star = turtle.Turtle()
star.color("green")
star.speed(10000000000000000)

for _ in range(5):
    star.forward(200)
    star.right(144)

turtle.done()