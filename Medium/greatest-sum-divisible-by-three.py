# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # Using dynamic programming
        opt = [0, -1e9, -1e9]
        for num in nums:
            temp = opt[:]
            for j in range(3):
                pick, skip = temp[(j - num) % 3] + num, temp[j]
                opt[j] = max(pick, skip)

        # Return the maximum sum divisible by three
        return opt[0]

# opt(i, j) - Maximum sum of the first i elements such that i % 3 == j

# Base case:
# opt(0, 0) = 0
# opt(0, 1) = -inf
# opt(0, 2) = -inf

# Recurrency:
# opt(i, j) = max(opt(i - 1, (j - nums[i]) % 3) + nums[i]), opt(i - 1, j))

# Both of these only use the previous i, meaning we can solve it using top-down