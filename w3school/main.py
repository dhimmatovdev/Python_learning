# x, y, z = "Tuz"

# fruits = ["olma", "anor", "baliq"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# Global variables 


# x = "test"

# def myfunc():
#     x = "ok"
#     print("Python is " + x)

# myfunc()
# print("Python is " + x)

# roy =  [1,3,4,8]
# for i in range(len(roy)):
#     if roy[i] % 2 == 0:
#         print("Juft")
#     else:
#         print("Toq")    
# def juft(a):
#     return sum(1 for i in a if i % 2 ==0)

# print(juft([1,2,4,5,6,9]))

# 2 masala

# Masala: Foydalanuvchidan ismi va yoshi kiritiladigan funksiya yozing.
# Agar foydalanuvchi yoshi 18 dan kichik bo‘lsa, 
# unga "Salom, yosh dasturchi!" deb qaytarilsin. 
# Aks holda "Salom, [ism]!" yozilsin.

# def solom():
#     yosh = int(input("Yoshingizni kiriting: "))
#     ism = str(input("Ismingizni kiriting: "))
#     if yosh < 18:
#         print("Salom yosh dasturchi ")
#     else:
#         print(f"Salom{ism}")
# solom()

# Optimal yechim

# def salom_ber(ism: str, yosh: int):
#     if yosh < 18:
#         return "Salom yosh dasturchi"
#     return f"Salom {ism}"
# if __name__ == "__main__":
#     ism = input("Ismingizni kiriting: ")
#     yosh = int(input("Yoshingizni kiriting: "))

# print(salom_ber(ism, yosh))

# class Shaxs():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def salom_ber(self):
#         return f"Salom, mening ismim {self.name}, yoshim {self.age}"
    
# ism = input("Ism: ")
# yosh = int(input("Yosh: "))
# # Obyekt yaratish
# shaxs = Shaxs(ism, yosh)

# print(shaxs.salom_ber())

# 4 masala
# class Talabalar():
#     def __init__(self, ism, facultet, baholar):
#         self.ism = ism
#         self.facultet = facultet
#         self.baholar = baholar
#     def talaba_info(self):
#         return f"Talaba ismini kiriting: {self.ism}, Fakultet: {self.facultet}"
#     def ortacha_baho(self):
#         return sum(self.baholar) / len(self.baholar)
#     def baho_yigindi(self):
#         return sum(self.baholar)
    

# ism = input("Talaba ismini kiriting: ")
# fac = input("Fakultetni kiriting: ")

# baholar = list(map(int, input("Baholarni kiriting (masalan: 5 4 3): ").split()))

# talaba = Talabalar(ism, fac, baholar)

# print(talaba.talaba_info())
# print("Baholar yig'indisi:", talaba.baho_yigindi())
# print("O'rtacha baho:", round(talaba.ortacha_baho(), 2))

class Hisob():
    def __init__(self, ism, balans=0):
        self.ism = ism
        self.balans = balans
    def pul_qoshish(self, miqdor):
        if miqdor > 0:
            self.balans += miqdor
            print(f"{miqdor} so'm hisobga qo'shildi. ")
        else:
            print("Xato: Manfiy miqdor qo'shib bo'lmaydi. ")
    def pul_yechish(self, miqdor):
        if miqdor > self.balans:
            print("Hisobda pul yo'q")
        elif miqdor <= 0:
            print("Xato kiritma! ")
        else:
            self.balans -=miqdor
            print(f"{miqdor} so'm yechildi.")
    def balansni_korish(self):
        print(f"{self.ism} hisobida: {self.balans} so'm mavjud. ")



    # Hisob ochish
ism = input("Ismingizni kiriting: ")
hisob = Hisob(ism)

# Amal bajarish
hisob.pul_qoshish(50000)
hisob.balansni_korish()

hisob.pul_yechish(20000)
hisob.balansni_korish()

hisob.pul_yechish(40000)  # yetarli mablag' yo'q
hisob.balansni_korish()
