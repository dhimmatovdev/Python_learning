a = int(input("Hozirgi soatni kiriting (0-23): "))  # Soatni butun songa o‘giramiz
x = int(input("Necha soat kutmoqchisiz? "))  # Kutish vaqtini butun songa o‘giramiz

h = x // 24  # To‘liq kunlar
s = x % 24  # Qolgan soatlar

a = (a + s) % 24  # Yangi vaqtni hisoblash

print(f"{h} kun va {s} soat o‘tdi")
print(f"Hozirgi vaqt: {a}:00")
