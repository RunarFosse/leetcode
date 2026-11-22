# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def checkString(self, s: str) -> bool:
        # Iterate every pair of characters
        for c1, c2 in pairwise(s):
            # If we ever find a b before an n
            if c1 == "b" and c2 == "a":
                # Then not all a's appear before all b's
                return False

        # Otherwise if loop terminates, we know all a's appear before all b's
        return True
