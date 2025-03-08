# a = int(input("Hozirgi soatni kiriting (0-23): "))  # Soatni butun songa o‘giramiz
# x = int(input("Necha soat kutmoqchisiz? "))  # Kutish vaqtini butun songa o‘giramiz

# h = x // 24  # To‘liq kunlar
# s = x % 24  # Qolgan soatlar

# a = (a + s) % 24  # Yangi vaqtni hisoblash

# print(f"{h} kun va {s} soat o‘tdi")
# print(f"Hozirgi vaqt: {a}:00")
# str_time = input("What time is it now? ")
# str_wait_time = input("What is the number of hours to wait? ")
# time = int(str_time)
# wait_time = int(str_wait_time)

# time_when_alarm_go_off = time + wait_time
# print(time_when_alarm_go_off)


import turtle

wn = turtle.Screen()
june = turtle.Turtle()

june.color("green", "yellow")

for i in range(4):
    june.forward(100)
    june.right(90)

wn.exitonclick()  # Sichqoncha bosilganda oynani yopish

