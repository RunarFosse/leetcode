# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Using bit manipulation
        n = len(s)

        # Iterate every k-sized substring of s
        substrings, current = set(), 0
        for i in range(n):
            # Ensure that the current substring is strictly sized k
            current <<= 1
            current &= (1 << k) - 1

            # Add the next bit
            current += int(s[i])

            # Set number as seen, if it contains more than k bits from s
            if i >= k - 1:
                substrings.add(current)
        
        # The string contains all binary codes of size k if set is sized 2^k
        return len(substrings) == (1 << k)
