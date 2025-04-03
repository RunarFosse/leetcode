# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Using suffix max
        value, i, difference = 0, 0, 0
        for num in nums:
            # First, compute maximum value
            value = max(difference * num, value)

            # Then, store maximum difference
            difference = max(i - num, difference)

            # At last, store maximum value for i
            i = max(num, i)
        
        # Finally, return the maximum value
        return max(value, 0)

# This solution is identical to Maximum Value of an Ordered Triplet I.