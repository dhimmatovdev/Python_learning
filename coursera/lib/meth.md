Bu jadval **Python** ning **`turtle`** kutubxonasidagi muhim metodlarni tushuntiradi. Quyida bu metodlarning qanday ishlashini kod bilan tushuntirib beraman.  

---

## **`turtle` kutubxonasi metodlari bilan misollar** 🐢  

### **1. Yangi Turtle yaratish**
```python
import turtle
t = turtle.Turtle()  # Yangi turtle obyekti yaratish
```

---

### **2. Harakat va burilish metodlari**  
```python
t.forward(100)  # Oldinga 100 piksel yurish
t.backward(50)  # Orqaga 50 piksel yurish
t.right(90)     # Soat yo‘nalishida 90° burilish
t.left(45)      # Soat yo‘nalishiga teskari 45° burilish
```

---

### **3. Qalamni ko‘tarish va tushirish**
```python
t.up()    # Chizishni vaqtincha to‘xtatish
t.goto(50, 50)  # Belgilangan nuqtaga borish (chiziq chizilmaydi)
t.down()  # Qayta chizishni yoqish
```

---

### **4. Rang va shakl sozlash**  
```python
t.color("blue")  # Qalam rangini ko‘k qilish
t.fillcolor("red")  # To‘ldirish rangini qizil qilish
t.shape("turtle")  # Turtle shaklini o‘zgartirish
```

---

### **5. Joylashuv va yo‘nalishni tekshirish**  
```python
print(t.heading())   # Joriy burilish burchagini chiqarish
print(t.position())  # Joriy (x, y) koordinatalarni chiqarish
```

---

### **6. Koordinatalar bo‘yicha harakat qilish va chizish**  
```python
t.goto(-100, 100)  # (-100, 100) nuqtaga borish
t.begin_fill()  # To‘ldirishni boshlash
t.circle(50)  # Radiusi 50 bo‘lgan aylana chizish
t.end_fill()  # To‘ldirishni tugatish
```

---

### **7. Nuqta va belgi qo‘yish**  
```python
t.dot(10)  # Hozirgi joyga 10 px o‘lchamdagi nuqta qo‘yish
t.stamp()  # Hozirgi joyda turtle belgisini qoldirish
```

---

### **8. Chizish tezligini sozlash**  
```python
t.speed(1)  # Eng sekin tezlik
t.speed(10) # Juda tez chizish
t.speed(0)  # Animatsiyani o‘chirib tashlash (tez)
```

---

**Natijada**, siz **`turtle`** kutubxonasining muhim metodlarini o‘zlashtirib, grafikalar chizishingiz mumkin! 🐢🎨  

✅ **Tushunmovchilik bo‘lsa, qo‘shimcha savollaringizni bemalol so‘rashingiz mumkin.** 😊