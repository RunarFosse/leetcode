# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    @functools.cache
    def uniquePaths(self, m: int, n: int) -> int:
        # Using dynamic programming
        if m == 1 or n == 1:
            return 1
        
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)


# opt(m, n) - Optimal solution starting at top left corner of (m, n) rectangle

# Base case:
# opt(1, n) = 1
# opt(m, 1) = 1

# Recurrency:
# opt(m, n) = opt(m-1, n) + opt(m, n-1)

# Number of states = m*n, runtime per state = O(1)