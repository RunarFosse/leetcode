# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Using deduction
        return True


# This is a trivial problem. There are two cases:

# Either the array is already all evens or all odds.
# Or, the array has a combination of evens and odds.

# In the first case, the array is already uniform.
# In the second case, we can use the fact that any even - odd = odd. Thus we can use
# "one" of the odds to turn all other even numbers into odd numbers, making it uniform.