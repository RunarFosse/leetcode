# Author: Runar Fosse
# Time complexity: O(mnN)
# Space complexity: O(mnN)

class Solution:
    mod = int(1e9 + 7)
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.m, self.n = m, n
        return self.opt(startRow, startColumn, maxMove)

    @functools.cache
    def opt(self, i: int, j: int, m: int) -> int: 
        # Check if position is outside
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return 1
        
        # Else if no moves left, return 0
        if not m:
            return 0
        
        # Walk up, down, left or right
        paths = self.opt(i-1, j, m-1) + self.opt(i+1, j, m-1)
        paths += self.opt(i, j-1, m-1) + self.opt(i, j+1, m-1)

        return paths % self.mod

        
# opt(i, j, m) - Number of paths to move ball out of grid boundary
#                starting at position (i, j) with m moves

# Base case:
# opt(i, j, 0) = 0
# opt(i outside, j outside, m) = 1

# Recurrency:
# opt(i, j, m) = opt(i-1, j, m-1) + opt(i+1, j, m-1)
#              + opt(i, j-1, m-1) + opt(i, j+1, m-1)


# n.o. states = m*n*N, runtime per state = O(1)
# Total tc of O(mnN)