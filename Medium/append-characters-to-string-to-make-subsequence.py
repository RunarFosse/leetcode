# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Using two pointers
        n, m = len(s), len(t)

        p1, p2 = 0, 0
        while p1 < n and p2 < m:
            # If we find two characters that match, move second pointer
            if s[p1] == t[p2]:
                p2 += 1
            p1 += 1
        
        # The remaining ("uniterated") part of t are the characters
        # we need to add to s for t to become a subsequence
        return m - p2