# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(log n)

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Using greedy
        nums.sort()
        n = len(nums)

        maximum = 0
        for i in range(n//2 + 1):
            maximum = max(nums[i] + nums[n-i-1], maximum)

        return maximum


# The minimal maximum pair sum in an array will obviously be attained by adding 
# the biggest element with the smallest, 2nd biggest with 2nd smallest etc.
# Then keep track of the maximum sum.