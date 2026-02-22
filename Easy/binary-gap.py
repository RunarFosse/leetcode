# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def binaryGap(self, n: int) -> int:
        # Using Brian Kernighan's
        
        # Strictly iterate every set bit in n
        gap, last = 0, None
        while n:
            # Flip the all bits right of the rightmost set bit
            flipped = n - 1

            # Unset this rightmost bit
            unset = n & flipped

            # Extract the value of this unset bit
            bit = n ^ unset

            # If we've seen another set bit
            if last is not None:
                # Store the longest binary gap
                gap = max(bit.bit_length() - last.bit_length(), gap)
            
            # Set variables and continue
            n, last = unset, bit
        
        # Finally, return the largest binary gap
        return gap


# Using Brian Kernighan's algorithm we strictly only iterate every set bit,
# instead of iterating every bit value. This is a heuristic which does not
# modify the worst case time complexity, although pragmatically it is more efficient.
