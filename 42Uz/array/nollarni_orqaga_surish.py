def moveZeroes(nums: list) -> list:
    j = 0 
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]  # Swap qilish
            j += 1
    return nums
print(moveZeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
print(moveZeroes([0]))  # [0]
print(moveZeroes([0, 0, 1]))  # [1, 0, 0]
print(moveZeroes([1, 2, 3, 4]))  # [1, 2, 3, 4]
print(moveZeroes([0, 0, 0, 0, 0]))  # [0, 0, 0, 0, 0]

# def move_zeros(nums):
#     j = 0 # Nollar bo'lmagan elementlarni qo'yish uchun indeks
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[j], nums[i] = nums[i], nums[j] #Swap qilish
#             j+=1 #Keyingi pozitsiyaga otish 


# nums2 = [0]
# moveZeros(nums)
# print(nums2)

# def moveZeroes(nums: list) -> list:
#     j = 0 
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[j], nums[i] = nums[i], nums[j]  # Swap qilish
#             j += 1
#     return nums  # Natijani qaytarish

# # Test qilish
# print(moveZeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
# print(moveZeroes([0]))  # [0]
# print(moveZeroes([0, 0, 1]))  # [1, 0, 0]
# print(moveZeroes([1, 2, 3, 4]))  # [1, 2, 3, 4]
# print(moveZeroes([0, 0, 0, 0, 0]))  # [0, 0, 0, 0, 0]



