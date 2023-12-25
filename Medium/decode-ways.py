# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    @functools.cache
    def numDecodings(self, s: str, i: int = 0) -> int:
        # Base cases
        if i == len(s):
            return 1

        # Illegal case
        if s[i] == "0":
            return 0

        # Can only decode 1 digit
        if s[i] > "2" or i == len(s) - 1 or (s[i] == "2" and s[i+1] > "6"):
            return self.numDecodings(s, i+1)
        
        # Can decode both digits
        return self.numDecodings(s, i+1) + self.numDecodings(s, i+2)
        