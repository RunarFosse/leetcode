# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Keep track of the maximum length of '0' blocks surrounding a '1' block
        maximum, ones = 0, 0

        # Then iterate the string
        left, middle, right = 0, 0, 0
        for c in s:
            # If we have a '1'
            if c == '1':
                # And it is the first of its block
                if right > 0:
                    # Swap counters
                    left, middle, right = right, 0, 0
            
                # And increment '1's current and total counter
                middle += 1
                ones += 1
                continue

            # Otherwise, increment the rightmost '0' counter
            right += 1

            # If we have now have two contiguous '0' blocks surrounding a '1' block
            if left > 0:
                # Compute their cumulative length and store that maximum
                maximum = max(left + right, maximum)
        
        # Finally, return the maximum number of active sections after a trade
        return maximum + ones


# First, we need to ensure that we can trade, which can be done if
# there exists a contiguous block of '1's between '0's.

# To maximize the active sections after a trade we need to find the largest
# contiguous block of '0's. This is guaranteed to be the result of the initial
# trade with the aforementioned contiguous block of '0's - '1's - '0's.

# Thus the problem reduces into finding this block ordering.
# The resulting maximum number of '1's in the string will thus be incremented by
# those left and right contiguous blocks of '0's.

# In short, the maximum number of active sections after a trade is equal to
# the number of '1's initially in the array + the maximum cumulative length of 
# two contiguous blocks of '0's surrounding a block of '1's.