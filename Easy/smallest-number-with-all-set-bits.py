# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def smallestNumber(self, n: int) -> int:
        # Get the most significant set bit in n
        largest = n.bit_length()

        # And return the number with all bits up to this bit set
        return (1 << largest) - 1
