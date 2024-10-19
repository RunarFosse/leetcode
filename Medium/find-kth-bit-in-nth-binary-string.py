# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Using bit manipulation

        # First compute if we are in the left or right section of the string,
        # which is done by checking if the left most bit is set
        left_most_bit = k & -k

        # Then compute if the original bit is set, by checking the parity
        parity = (k & 1) == 0

        # At last compute if the bit should be inverted compared to its
        # original, by checking if the second bit of the wanted bit
        # in its left section position is set
        should_invert = ((k // left_most_bit) >> 1 & 1)

        # Finally return the bit
        if should_invert:
            parity ^= 1

        return "1" if parity else "0"

# First we note that every odd number is set to 0, and even to 1 originally.
# Then we note that every number in the right section is the inverted
# bit of the one in the left section.
# If we then know how many times each bit has been inverted, we can
# analytically figure out if the wanted bit is set or not.