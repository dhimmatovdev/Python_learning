class Naqd:
    def tolov(self, summa):
        print(f"Naqd pul bilan {summa} to'lanadi. ")

class Karta:
    def tolov(self, summa):
        print(f"Karta orqali {summa} so'm to'lanadi ")

class Payme:
    def tolov(self, summa):
        print(f"Payme orqali {summa} so'm to'lanadi ")

def tolov_qil(turi, summa):
    turi.tolov(summa)

naqd = Naqd()
karta = Karta()
payme = Payme()

for t in (naqd, karta, payme):
    tolov_qil(t, 100000)