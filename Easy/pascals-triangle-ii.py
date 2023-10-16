# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = []
        for i in range(0, rowIndex+1):
            value = self.factorial(rowIndex) / (self.factorial(i) * self.factorial(rowIndex - i))
            row.append(int(value))
        return row

    @functools.cache
    def factorial(self, i: int) -> int:
        if i == 0:
            return 1
        return self.factorial(i-1) * i

# Observations:
# Each row has length equal to row index
# Each row is a "palindrome"
# Conclusion:
# Each cell is equal to "rowIndex over index" (binomial coefficient)

# Due to memoization, factorial function has total runtime O(rowIndex)
# Space is also equal to O(rowIndex)