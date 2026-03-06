# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)

        # First, iterate the initial ones
        i = 0
        while i < n and s[i] == "1":
            i += 1
        
        # Then, iterate the rest of the string
        while i < n:
            # If we ever see another one, it has more than one segment of ones
            if s[i] == "1":
                return False
            i += 1
        
        # If the loop terminates, it has only one
        return True
