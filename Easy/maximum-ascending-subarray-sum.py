# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)

        # Iterate the array
        current_sum, max_sum = 0, 0
        for i in range(n):
            # Counting sums of strictly increasing subarrays
            if i > 0 and nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            max_sum = max(current_sum, max_sum)
        
        # Return the maximum such sum
        return max_sum