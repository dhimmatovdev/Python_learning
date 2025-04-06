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

def salom_ber(ism: str, yosh: int):
    if yosh < 18:
        return "Salom yosh dasturchi"
    return f"Salom {ism}"
if __name__ == "__main__":
    ism = input("Ismingizni kiriting: ")
    yosh = int(input("Yoshingizni kiriting: "))

print(salom_ber(ism, yosh))