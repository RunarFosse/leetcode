# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Using greedy
        n = len(nums)

        # First sort the array in ascending order
        nums.sort()

        # Then iterate from behind, finding first index n-i where
        # current value is greater or equal, and next (n-i-1) is smaller
        for i in range(1, n+1):
            if nums[n-i] >= i and (i == n or nums[n-i-1] < i):
                # If so, the array is special for value i
                return i

        # If no such index is found, return -1
        return -1