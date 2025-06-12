# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)

        # Iterate the array
        maximum = 0
        for i in range(n):
            # Keeping track of difference between adjacent elements
            difference = abs(nums[i % n] - nums[(i + 1) % n])

            # And storing the maximum
            maximum = max(difference, maximum)

        return maximum