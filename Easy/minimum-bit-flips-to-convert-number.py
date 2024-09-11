# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        return xor.bit_count()

# The bits to flip such that we convert the start number to the goal number
# is easily calculated by performing the XOR operation and inspecting which
# bits differ in each number. From the bit_count() function we can easily
# extract how many bits are set in the XOR number, i.e. how many we should
# flip.