# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Using prefix sum
        n = len(nums)
        
        # First compute the sum of the array as right part
        left, right = 0, sum(nums)

        # Then iterate the array, keeping track of running prefix sum
        splits = 0
        for i in range(n - 1):
            left += nums[i]
            right -= nums[i]

            # If left is greater or equal to right, this is a valid split
            if left >= right:
                splits += 1
        
        # Finally, return the number of valid splits
        return splits