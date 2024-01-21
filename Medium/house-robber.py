# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Using dynamic programming
        n = len(nums)
        
        for i in range(1, n):
            # Base cases
            if i == 1:
                if nums[0] > nums[1]:
                    nums[1] = nums[0]
                continue

            # Recurrency
            if nums[i-1] < nums[i] + nums[i-2]:
                nums[i] += nums[i-2]
            else:
                nums[i] = nums[i-1]
        
        return nums[n-1]

# opt(i) - Maximum amount of money you can rob from houses [0, i]
#          without alerting the police.

# Base case:
# opt(0) = nums[0]
# opt(1) = max(nums[1], nums[0])

# Recurrency:
# opt(i) = max(nums[i] + opt(i-2), opt(i-1))

# n.o. states = n, runtime per state O(1).
# Implementing in-place dp gives space complexity of O(1).