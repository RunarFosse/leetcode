# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        longest = increasing = decreasing = 1
        for i in range(n - 1):
            # Increment increasing or decreasing counter following elements
            if nums[i] == nums[i + 1]:
                increasing = 1
                decreasing = 1
            elif nums[i] < nums[i + 1]:
                increasing += 1
                decreasing = 1
            else:
                increasing = 1
                decreasing += 1

            # Store the largest subarray, strictly increasing or decreasing
            longest = max(increasing, decreasing, longest)
    
        # Return the size of the longest subarray
        return longest
            