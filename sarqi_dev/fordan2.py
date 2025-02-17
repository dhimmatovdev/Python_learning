sonlar = list(range(10,100))
for son in sonlar:
    print(f"{son},ning kubi {son**3},ga teng")

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, 
# va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]
for ism in ismlar:
    print(f"Salom {ism}, bugun choyxona bormi?")
print(f"Kod {len(ismlar)} marta takrorlandi")

kinolar = [] 
print("3 ta eng sevimli kinolaringizni kiriting: ")
for k in range(3):
    kinolar.append(input(f"{k+1}-kino: "))
print(kinolar)


n_people = int(input("Bugun nechta odam bilan suhbat qildingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi?>>>"))
print(ismlar)