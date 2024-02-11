# Author: Runar Fosse
# Time complexity: O(mn^2)
# Space complexity: O(mn^2)

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # Using dynamic programming
        m, n = len(grid), len(grid[0])
        opt = [[0 for _ in range(n)] for _ in range(n)]

        for i in reversed(range(m)):
            current_row = [[0 for _ in range(n)] for _ in range(n)]
            for j1 in range(n-1):
                for j2 in range(j1+1, n):
                    current_row[j1][j2] = grid[i][j1] + grid[i][j2]
                    current_row[j1][j2] += max(
                        opt[j1_][j2_]
                        for j1_ in range(max(j1-1, 0),min(j1+2, n))
                        for j2_ in range(max(j2-1, 0),min(j2+2, n))
                        if j1_ < j2_
                        )
            opt = current_row
        
        # Return the values if for intial robot positions
        return opt[0][n-1]
        
# This is a longest path problem, and can be solved using dynamic programming.
# As we have 2 robots, we put an additional constraint keeping robot 1 left of
# robot 2 at all times, and never let them overlap.
# We also know that they will have the same i-index at all times, as they
# both move downwards at the same constant pace.

# opt(i, j1, j2) - Maximum number of cherries collected by robots at j1 and j2
#                  respectively, if they start at row i.

# Base case:
# opt(m, j1, j2) = 0

# Recurrency;
# opt(i, j1, j2) = grid[i, j1] + grid[i, j2] + max(
#     opt(i+1, j1_, j2_) 
#     for j1_ in [j1-1..j1+1] for j2_ in [j2-1..j2+1]   if j1_ < j2_
#)