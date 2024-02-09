# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Using dynamic programming
        nums.sort()

        n = len(nums)
        opt = [[] for i in range(n)]

        current_longest = []
        for i in reversed(range(n)):
            opt[i].append(nums[i])
            for j in range(i+1, n):
                if not nums[j] % nums[i] and len(opt[j]) >= len(opt[i]):
                    opt[i] = [nums[i]] + opt[j]
            
            if len(opt[i]) > len(current_longest):
                current_longest = opt[i]

        return current_longest

# By sorting list at start in descending order, we can greedily check if an
# element can divide the whole other subset by comparing with only 1 other
# element in the subset. This is due to division transitivity.

# opt(i) - Largest divisible subset on nums[i:]

# Base case:
# opt(n-1) = [nums[n-1]]

# Recurrency:
# opt(i) = [nums[i]] + longest(opt(j) for j in [i+1..n] if nums[j] % nums[i] == 0)

# n.o. states = n, runtime per state = O(n).
# Final TC: O(n^2).

# Note: Even though we store a list in each opt[i], the size of this array is 
# upperbounded by the largest possible divisble subset size given the constraints,
# (which is len([1, 2, 4, 8, ..., 2^32]) = 33, hence SC: O(33*n) = O(n))