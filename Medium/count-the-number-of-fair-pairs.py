# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Using greedy

        # First sort the array in ascending order
        nums.sort()

        # Then iterate the array
        fairs = 0
        for i, num in enumerate(nums):
            # Compute the bounds
            bounds = (lower - num, upper - num)

            # Binary search indices contained within the bounds,
            # restricted to only the already seen parts of the array
            left = bisect_left(nums, bounds[0], hi=i)
            right = bisect_right(nums, bounds[1], hi=i)
            
            # Count the number of fair pairs
            fairs += right - left
        
        # Finally return the number of fair pairs
        return fairs


# We have that for each number i and j, then:
# lower <= nums[i] + nums[j] <= upper

# This can be reordered to:
# lower - nums[i] <= nums[j] <= upper - nums[i]

# Here we get a formal definition for bounds, which we can
# use to count how many fair pairs exist. When sorting the array,
# this allows us to perform binary search.