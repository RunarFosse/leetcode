# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        # Iterate the sequence
        depth, split = 0, []
        for c in seq:
            # If we find an open parenthesis, increment the depth
            if c == "(":
                depth += 1

            # Split the current character based on the current depth
            split.append(depth % 2)

            # If we find a closed parenthesis, decrement the depth
            if c == ")":
                depth -= 1
        
        # Finally, return the sequence splitting
        return split


# We want to split the sequence into two subsequences minimizing the depth.
# This can be done by setting half the depths' parenthesis in one split, and
# the other half in the other.

# The simplest way of splitting these in two is based on the parity of the current depth.
# Because roughly half the numbers have one parity, half the other, if nested closely,
# we can achieve an even splitting which minimizes the deepest nesting depth!