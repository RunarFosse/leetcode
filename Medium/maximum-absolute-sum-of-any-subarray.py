# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Using prefix sum
        prefix = 0

        max_prefix, min_prefix = 0, 0
        for num in nums:
            # Add to prefix sum
            prefix += num

            # Compute max and min prefix sums
            max_prefix = max(prefix, max_prefix)
            min_prefix = min(prefix, min_prefix)
        
        # At last, return the maximum absolute sum
        return max_prefix - min_prefix