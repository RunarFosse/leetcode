# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx, dy = abs(sx - fx), abs(sy - fy)
        if not dx and not dy:
            # If you start at (fx, fy) you can only return for t >= 2
            return t != 1

        # First find how far you can walk diagonally
        diagonal = min(dx, dy)

        # Then the rest is a straight walk
        distance = diagonal + max(dx - diagonal, dy - diagonal)
        return distance <= t
        
# If you can reach the cell at any time s, you can reach it in any other time s+n
# where n > 0 simply by taking a detour. Therefore, this problem is asking if 
# we can reach (fx, fy) from (sx, sy) in t time. This is a simple distance check.