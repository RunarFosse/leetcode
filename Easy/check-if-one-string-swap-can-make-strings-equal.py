# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)

        # Iterate both strings
        indices = (None, None)
        for i in range(n):
            c1, c2 = s1[i], s2[i]
            # Continue if they are equal
            if c1 == c2:
                continue
            
            # If we've already found two unequals, return False
            if indices[1] is not None:
                return False
            
            # Otherwise check if this is first
            if indices[0] is None:
                indices = (i, None)
                continue

            # If it is second
            indices = (indices[0], i)

            # Also check that the swaps are valid
            if not (s1[indices[0]] == s2[i] and s1[i] == s2[indices[0]]):
                return False
            
        # Strings are equal if both or neither swap indices are set
        return indices[0] is None or indices[1] is not None