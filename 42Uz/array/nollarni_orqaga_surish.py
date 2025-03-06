def moveZeroes(nums: list) -> list:
    j = 0 
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]  # Swap qilish
            j += 1
    return nums  # Natijani qaytarish

# Test qilish
print(moveZeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
print(moveZeroes([0]))  # [0]
print(moveZeroes([0, 0, 1]))  # [1, 0, 0]
print(moveZeroes([1, 2, 3, 4]))  # [1, 2, 3, 4]
print(moveZeroes([0, 0, 0, 0, 0]))  # [0, 0, 0, 0, 0]
