# Author: Runar Fosse
# Time complexity: O(m+n)
# Space complexity: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Using two pointer approach
        p1, p2 = 0, 0
        while p1 < len(s):
            # If we reach t's end, s is not a subsequence of t
            if p2 == len(t):
                return False

            # Increment pointers if characters are equal
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        
        # If we escape the loop, s is a subsequence of t
        return True
        