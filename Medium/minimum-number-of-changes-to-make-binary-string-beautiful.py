# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)

        # Iterate the string in steps of two
        changes = 0
        for i in range(0, n, 2):
            # If a pair of numbers do not match, perform a swap
            if s[i] != s[i+1]:
                changes += 1
        
        # Return the number of changes
        return changes
        