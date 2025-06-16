# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # Using greedy

        # Iterate the array
        difference, minimum = -1, nums[0]
        for num in nums:
            # Store maximum difference if constraints are upheld
            if minimum < num:
                difference = max(num - minimum, difference)
            # Otherwise, update current minimum
            else:
                minimum = num

        # Finally, return that maximal difference
        return difference
