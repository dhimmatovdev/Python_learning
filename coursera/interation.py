class MyIterator:
    def __init__(self, start):
        self.num = start
    
    def __iter__(self):
        return self  # Iterator obyekt o‘zini qaytarishi kerak
    
    def __next__(self):
        self.num += 2
        return self.num

# Foydalanish
it = MyIterator(1)
print(next(it))  # 3
print(next(it))  # 5
print(next(it))  # 7
