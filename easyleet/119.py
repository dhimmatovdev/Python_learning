class Solution(object):
    def getRow(self, rowIndex):
        row = [1] * (rowIndex + 1)

        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]

        return row

sol = Solution()
print(sol.getRow(3))  # [1, 3, 3, 1]
print(sol.getRow(4))  # [1, 4, 6, 4, 1]
print(sol.getRow(5))  # [1, 5, 10, 10, 5, 1]
