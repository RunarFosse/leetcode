# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)

        # Calculate the absolute ascii difference between
        # all consecutive elements in the string and return it
        score = sum(abs(ord(s[i-1]) - ord(s[i])) for i in range(1, n))        
        return score