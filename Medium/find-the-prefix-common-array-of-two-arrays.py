# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # Using bitmask
        common = []

        # Store the occurence of a given integer in the bits of a number
        seen_a, seen_b = 0, 0
        for a, b in zip(A, B):
            # And mark the current numbers as seen
            seen_a |= 1 << a
            seen_b |= 1 << b

            # Add into common prefix array
            seen = seen_a & seen_b
            common.append(seen.bit_count())

        # Return the prefix common array
        return common

# As the number of possible numbers in the arrays are low
# (<= 50), we can represent an integer being seen as a set bit
# in a number instead of a set. 