# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Using dynamic programming
        n = len(nums)
        
        opt = [0] * n
        for i in range(n):
            # Base cases
            if i in [0, 1]:
                opt[i] = max(nums[1], nums[0]) if i else nums[0]
                continue

            # Recurrency
            opt[i] = max(nums[i] + opt[i-2], opt[i-1])
        
        return opt[n-1]

# opt(i) - Maximum amount of money you can rob from houses [0, i]
#          without alerting the police.

# Base case:
# opt(0) = nums[0]
# opt(1) = max(nums[1], nums[0])

# Recurrency:
# opt(i) = max(nums[i] + opt(i-2), opt(i-1))

# n.o. states = n, runtime per state O(1).