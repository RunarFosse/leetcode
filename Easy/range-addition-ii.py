# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # Iterate ops and find min m, n
        minm, minn = m, n
        for a, b in ops:
            minm = min(a, minm)
            minn = min(b, minn)
        
        return minm * minn

# We want to calculate how many of a maximum number exist.
# If we find which areas ALL operations cover we will have our answer.