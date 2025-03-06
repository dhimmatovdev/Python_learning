import turtle

def draw_heart():
    turtle.bgcolor("black")  # Orqa fon rangi
    turtle.pensize(3)        # Qalam qalinligi
    turtle.speed(5)          # Chizish tezligi
    turtle.color("red")      # Qalam rangi

    turtle.begin_fill()  # Ichini to‘ldirishni boshlash
    turtle.fillcolor("red")  # Ichki rangi

    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-90, 200)  # Chap tomon yumaloq qismi
    turtle.left(120)
    turtle.circle(-90, 200)  # O‘ng tomon yumaloq qismi
    turtle.forward(180)

    turtle.end_fill()  # Ichini to‘ldirishni tugatish

    turtle.hideturtle()  # Chizgichni yashirish
    turtle.done()  # Chizishni tugatish

# Yurak chizish
draw_heart()
