# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # First verify that we have enough characters to create k palindromes
        if len(s) < k:
            return False
        
        # If we do, check how many characters are even/odd
        odds = 0
        indexOf = lambda c: ord(c) - ord("a")
        for c in s:
            odds ^= 1 << indexOf(c)

        # Verify that the number of odds are less than or equal to k
        return odds.bit_count() <= k
