# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Using dynamic programming
        self.n = len(nums)

        # First sort the nums array in ascending order
        self.nums = sorted(nums)

        # Then perform dynamic programming
        longest_streak = max(self.opt(i) for i in range(self.n))
        return longest_streak if longest_streak > 1 else -1

    @functools.cache
    def opt(self, i: int) -> int:
        if i == self.n:
            return 0
        
        # Try to locate a next square, to calculate streak length if picking i
        next_square = pow(self.nums[i], 2)
        j = bisect_left(self.nums, next_square)
        if j < self.n and self.nums[j] != next_square:
            j = self.n

        return 1 + self.opt(j)

# opt(i) - The longest square streak in nums[i:]

# Base case:
# opt(n) = 0

# Recurrency:
# opt(i) = max(1 + opt(j) if nums[j] == nums[i]^2, opt(i+1))


# N.o. states = n
# Runtime per state -> O(log n)

# Total runtime is O(nlog n)