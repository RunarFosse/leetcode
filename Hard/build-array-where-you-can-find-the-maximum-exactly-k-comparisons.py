# Author: Runar Fosse
# Time complexity: O(nm^2k)
# Space complexity: O(nmk)

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # Using Dynamic Programming
        self.n = n
        self.m = m
        return self.opt(0, 0, k) % int(1e9+7)

    @functools.cache
    def opt(self, i: int, max_last: int, max_left: int):
        if i == self.n:
            return 1 if not max_left else 0
        if max_left < 0:
            return 0

        skip = max_last * self.opt(i+1, max_last, max_left)
        add = 0
        for num in range(max_last+1, self.m+1):
            add += self.opt(i+1, num, max_left-1)
        
        return skip + add
        
  
# Simplify the problem:
# We want to find out how many different n-sized arrays
# we can create containing the values [1, .., m] such that
# traversing the array left to right grants us k new maximums.

# When building an array we need to know:
# The current index we are at, i
# The current maximum number we've seen, max_last
# How many new maximums do we need to place, max_left

# This gives us enough information for to construct a DP
# opt(i, max_last, max_left)

# Base Case:
# i == n:
# return 1 if max_left == 0 else 0
#
# max_left < 0:
# return 0

# Recurrency:
# (No. arrays without a new max at i + no. with a new max at i)
# return max_last * opt(i+1, max_last, max_left)
#     + (Σ_num∈[max_last+1, m] opt(i+1, num, max_left-1))

# Space complexity of this is number of different states n*m*k, O(nmk)
# Time complexity is obviously n.o. states * runtime per state (which is O(m))
# i.e. O(nm^2k)