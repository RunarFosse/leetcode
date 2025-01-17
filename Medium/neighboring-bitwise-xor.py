# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # Set the initial bit value to zero
        first = 0

        # And iterate derived array, computing the last bit value
        last = first
        for parity in derived:
            last = last ^ parity

        # The array is derived from a valid binary array if last equals first
        return last == first