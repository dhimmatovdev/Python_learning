# Counter: 
# Counter — bu Python dasturida elementlar sonini sanash uchun 
# ishlatiladigan maxsus klass (collections.Counter).
# U list, string, tuple yoki boshqa iteratsion obyektlardagi 
# takrorlanuvchi elementlarni hisoblab, natijani lug‘at (dictionary) 
# shaklida qaytaradi.
from collections import Counter

numbers = [1,2,3,4,5,4,3,4,5,6,33,6]
counter = Counter(numbers)
print(counter)

text = "mississippi"
counter = Counter(text)
print(counter)

counter = Counter("banana")
print(counter.most_common(2))  # Eng ko‘p uchragan 2 ta element

counter = Counter({'a': 4, 'b': 2})
counter.subtract("ab")  # "a" va "b" bittadan kamayadi
print(counter)

c1 = Counter("apple")
c2 = Counter("pear")
print(c1 - c2)
