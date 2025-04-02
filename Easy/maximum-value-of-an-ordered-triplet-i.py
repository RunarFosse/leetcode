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

# To find a value which maximizes (nums[i] - nums[j]) * nums[k] for i < j < k,
# we can deduce that we, for every i, need to check every j and multiply with
# a largest nums[k].

# To optimize this, we can store the maximum (nums[i] - nums[j]) as a running
# variable. To achieve this, we also need to store the maximum nums[i] in the
# same way. Then, we can greedily compute the maximum value in one fell swoop.