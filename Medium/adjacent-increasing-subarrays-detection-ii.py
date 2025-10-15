# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        # Iterate the array
        maximum, current, last = 0, 1, 0
        for i in range(1, n):
            # Keep count of the number of strictly increasing elements
            if nums[i] <= nums[i - 1]:
                last = current
                current = 0
            current += 1

            # Storing the maximum adjacent subarray sizes as we go
            maximum = max(min(current, last), current // 2, maximum)

        # Finally, return this maximum adjacent subarray size
        return maximum
