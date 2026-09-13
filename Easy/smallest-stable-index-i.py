# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # Using prefix sum
        n = len(nums)

        # Compute the suffix minimum of the array
        minimums = nums.copy()
        for i in range(1, n):
            minimums[n - i - 1] = min(minimums[n - i - 1], minimums[n - i])
        
        # Then iterate each index
        maximum = 0
        for i in range(n):
            # Update the running prefix maximum of the array
            maximum = max(nums[i], maximum)

            # And compute instability score
            instability = maximum - minimums[i]

            # If this is stable, we have our smallest index
            if instability <= k:
                return i
        
        # However, if loop terminates, there is no smallest stable index
        return -1
