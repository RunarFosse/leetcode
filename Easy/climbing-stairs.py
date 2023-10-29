# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    @functools.cache
    def climbStairs(self, n: int) -> int:
        # Using dynamic programming
        if n <= 2:
            return n
        
        last1, last2 = 2, 1
        for _ in range(3, n):
            last1, last2 = (last1+last2), last1
        
        return last1 + last2


# Using dynamic programming we only use opt(i-1) and opt(i-2).
# These can be stored in variables, leading to constant space complexity.
