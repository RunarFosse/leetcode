# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # Iterate over each character in the bit array, up until the last bit
        i, n = 0, len(bits)
        while i < n - 1:
            # If the first bit is zero, it is a one-bit character
            i += 1 if bits[i] == 0 else 2

        # If we end at the last bit, the last character is a one-bit
        return i == n - 1
        