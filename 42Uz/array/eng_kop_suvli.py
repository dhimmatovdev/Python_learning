def maxArea(nums: list) -> int:
    i, j = 0, len(nums)-1  # 1. Chap va o‘ng tomondan boshlaymiz
    max_area = 0           # 2. Eng katta maydonni 0 qilib boshlaymiz
    while i < j:           # 3. Ikki indeks kesishmaguncha davom etamiz
        area = (j-i) * min(nums[i], nums[j])  # 4. Maydonni hisoblaymiz
        max_area = max(area, max_area)  # 5. Eng katta maydonni yangilaymiz
        if nums[i] < nums[j]:  
            i += 1  # 6. Agar chap tomoni kichik bo‘lsa, chapni o‘ngga suramiz
        else:
            j -= 1  # 7. Aks holda, o‘ng tomonni chapga suramiz
    return max_area  # 8. Natijani qaytaramiz
