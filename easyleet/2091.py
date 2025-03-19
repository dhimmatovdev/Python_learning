class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        
        if min_index > max_index:
            min_index, max_index = max_index, min_index
        
        # 3 xil yo‘lni hisoblaymiz
        left = max(min_index + 1, max_index + 1)  # Chapdan
        right = max(n - min_index, n - max_index)  # O‘ngdan
        both = min_index + 1 + (n - max_index)  # Chapdan min, o‘ngdan max
        
        return min(left, right, both)
