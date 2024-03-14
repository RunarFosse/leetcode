# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Using sliding window
        n = len(nums)

        p1, p2 = 0, 0
        window, count = 0, 0
        prefix_0s = 0
        while p2 < n:
            # Expand the window
            window += nums[p2]
            p2 += 1

            # Now shrink the window again until it sums to goal
            while p1 < p2-1 and (nums[p1] == 0 or window > goal):
                if nums[p1] == 1:
                    prefix_0s = 0
                else:
                    prefix_0s += 1
                window -= nums[p1]
                p1 += 1

            # If our current window sums to goal, add all possible subarrays
            if window == goal:
                count += prefix_0s + 1
                
        # Return the number of possible subarrays
        return count

# If we use sliding window, and keep track of how many contiguous 0s exist
# as a prefix of the window, we can easily count how many subarrays which sum
# to the same as our whole window.