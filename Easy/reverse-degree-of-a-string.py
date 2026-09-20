# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def reverseDegree(self, s: str) -> int:
        # Create a helper function getting each character's reversed alphabet position
        reversedPositionOf = lambda c: ord("z") - ord(c) + 1

        # Then compute and return the reverse degree of the string
        return sum((i + 1) * reversedPositionOf(c) for i, c in enumerate(s))
