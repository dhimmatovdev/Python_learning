import turtle 
wn = turtle.Screen()

elan = turtle.Turtle()

distance = 50
angle = 90
for i in range(120):
    elan.forward(distance)
    elan.right(angle)
    distance = distance + 10
    angle = angle - 3