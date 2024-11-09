# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # Initialize the number to x
        num = x
        
        # For the n'th number in the array, solve by inserting bits of
        # n-1 in the non-set bits position of x
        x_i, n_i = 0, 0
        while (n-1) >> n_i:
            # If the bit is not set in x
            if not x >> x_i & 1:
                # Add the bit value from (n-1)
                num += ((n-1) >> n_i & 1) << x_i
                n_i += 1
            x_i += 1

        # Finally return the resulting number
        return num

# Solved analytically, the pattern is as shown below:

# Starting with x = 4
# 000 100
# 000 101
# 000 110
# 000 111
# 001 100

# Starting with x = 7
# 000 111
# 001 111
# 010 111
# 011 111
# 100 111
# 101 111