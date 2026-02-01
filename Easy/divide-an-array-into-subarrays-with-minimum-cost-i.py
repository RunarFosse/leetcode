# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # Using Greedy
        n = len(nums)
        
        # Iterate the tail of the array
        minimums = (1e9, 1e9)
        for i in range(1, n):
            # Storing the two minimum elements
            if nums[i] < minimums[0]:
                minimums = (nums[i], minimums[0])
            elif nums[i] < minimums[1]:
                minimums = (minimums[0], nums[i])
        
        # The smallest cost is equal to the initial element plus these two minimums
        return nums[0] + sum(minimums)


# As the first element always is included in the sum, and the first subarray always
# start at the first element of the array, we can solve it like this:

# Add the first element to the sum, it will always be included.
# Find the two minimum elements in the remaining subarray.