# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    mod = int(1e9 + 7)
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # Using Dynamic programming
        self.zero = zero
        self.one = one

        return sum(self.opt(i) for i in range(low, high+1)) % self.mod
    
    @functools.cache
    def opt(self, i: int) -> int:
        if i == 0:
            return 1
        if i < 0:
            return 0
        
        return (self.opt(i - self.zero) + self.opt(i - self.one)) % self.mod


# DP:
# opt(i) = optimal solution with string of length i
# Then solution = sum of i ∈ [low, high] of opt(i)

# Base Case:
# opt(0) = 1
# opt(less than 0) = 0              # Invalid case

# Recurrency:
# opt(i) = opt(i-zero) + opt(i-one)

# N.o. states = O(n) (only depends on high-bound because of memoization)
# runtime per state = O(1), thus time complexity: O(n)