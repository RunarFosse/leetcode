# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    mod = int(1e9 + 7)
    def numSub(self, s: str) -> int:
        # Iterate the string
        substrings, ones = 0, 0
        for c in s:
            # Count the current number of subsequent ones
            if c == "1":
                ones += 1
            else:
                ones = 0
            
            # And count every substring
            substrings += ones
            substrings %= self.mod

        # Finally, return the total number of substrings of only ones
        return substrings
