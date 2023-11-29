# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        # Using bit manipulation
        ones = 0
        while n:
            if n & 1:
                ones += 1
            n >>= 1
        
        return ones