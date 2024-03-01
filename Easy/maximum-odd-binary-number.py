# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # First we count the number of ones
        ones = sum(1 for c in s if c == "1")

        # Then place all '1's except one to the left
        # '0's in the middle, and a last '1' all the way to the right
        return "1" * (ones - 1) + "0" * (len(s) - ones) + "1"

# This is easily solved grouping all '1's at the left,
# except one, placed all the way to the right.