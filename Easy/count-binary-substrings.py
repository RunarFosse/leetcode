# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Using two pointer
        n = len(s)

        # Iterate the array
        substrings = 0
        current, last = 0, 0
        for i in range(n):
            # Increment the current substring size
            current += 1

            # Count substrings and reset counter if we break consecutivity
            if i < n - 1 and s[i] != s[i + 1]:
                substrings += min(current, last)
                current, last = 0, current

        # Finally, return the number of binary substrings
        return substrings + min(current, last)
