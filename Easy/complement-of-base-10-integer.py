# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Compute a mask of all the bits in n
        bits = max(n.bit_length(), 1)
        mask = (1 << bits) - 1

        # And use the mask to flip all bits in n
        return n ^ mask
