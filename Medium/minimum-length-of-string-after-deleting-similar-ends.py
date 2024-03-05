# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minimumLength(self, s: str) -> int:
        # Using two pointer approach
        p1, p2 = 0, len(s)-1
        while p1 <= p2:
            c = s[p1]
            
            # If we can not remove any char, return current length
            if p1 == p2 or c != s[p2]:
                return p2 - p1 + 1
            else:
                # If we can, remove as much as possible
                while p1 <= p2 and s[p1] == c:
                    p1 += 1
                while p2 > p1 and s[p2] == c:
                    p2 -= 1
                
        # If we ever escape the while loop, string is empty
        return 0

# Greedily remove any character we can until we can't. This is our minimum length.