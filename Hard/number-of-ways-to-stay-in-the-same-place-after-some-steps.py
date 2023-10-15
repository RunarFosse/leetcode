# Author: Runar Fosse
# Time complexity: O(n min(n,m))
# Space complexity: O(n min(n,m))

class Solution:
    mod = int(1e9 + 7)
    def numWays(self, steps: int, arrLen: int) -> int:
        # Using dynamic programming
        self.arrLen = min(steps // 2 + 1, arrLen)
        return self.opt(0, steps) % self.mod

    @functools.cache
    def opt(self, i: int, j: int) -> int:
        if j == 0:
            return 1 if i == 0 else 0

        ways = self.opt(i, j-1) % self.mod
        if i > 0:
            ways += self.opt(i-1, j-1) % self.mod
        if i < self.arrLen - 1:
            ways += self.opt(i+1, j-1) % self.mod
        
        return ways


# opt(i, j) - no. different ways to return to index 0 from index i given j steps
# Note, we can clamp arrLen to steps // 2 + 1, as walking more than
# half of our steps to the right will make it impossible to return to index 0!

# Base case:
# opt(i, 0) = 1 if i == 0 else 0       - No steps left

# Recurrency:
# opt(i, j) = (
#   opt(i-1, j-1) +      - Go left (only if i > 0)
#   opt(i, j-1) +        - Stay
#   opt(i+1, j-1)        - Go right (only if i < arrLen)
#)

# No. states    = n*m (m is min(steps//2+1, arrLen), n is steps)
# -> No. states = n*min(n//2 + 1,m) = O(n min(n,m))
# Runtime per state = O(1)
# --- > Time complexity of O(n min(n,m))