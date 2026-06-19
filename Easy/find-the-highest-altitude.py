# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # First, define a helper function storing current and highest altitude
        computeHighest = lambda r, e: (r[0] + e, max(r[0] + e, r[1]))

        # Then, reduce and find the highest altitude
        _, highest = reduce(computeHighest, gain, (0, 0))

        # And return it
        return highest
