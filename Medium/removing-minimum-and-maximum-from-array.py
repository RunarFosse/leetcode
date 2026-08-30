# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        # First, find the index of the minimum and maximum element
        minimum, maximum = 0, 0
        for i in range(1, n):
            if nums[i] < nums[minimum]:
                minimum = i
            if nums[i] > nums[maximum]:
                maximum = i
        
        # And compute the minimum number of removals needed to remove both
        left, right = min(minimum, maximum), max(minimum, maximum)
        removals = min(
            right + 1,
            n - left,
            left + 1 + (n - right)
        )
        return removals
