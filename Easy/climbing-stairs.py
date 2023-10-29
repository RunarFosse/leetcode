class Solution:
    @functools.cache
    def climbStairs(self, n: int) -> int:
        # Using dynamic programming
        if n <= 0:
            return 1 if n == 0 else 0
            
        return self.climbStairs(n-1) + self.climbStairs(n-2)
