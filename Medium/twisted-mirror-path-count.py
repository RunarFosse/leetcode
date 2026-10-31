# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(n)

class Solution:
    mod = int(1e9 + 7)
    def uniquePaths(self, grid: List[List[int]]) -> int:
        # Using dynamic programming
        m, n = len(grid), len(grid[0])

        # Create the DP array
        opt = [[0, 0] for _ in range(n)]

        # Iterate the grid
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                # If we are at the end cell, terminate all paths
                if (i, j) == (m - 1, n - 1):
                    opt[j] = [1, 1]
                    continue
                
                # Compute right and down paths
                right = opt[j + 1][0] if j < n - 1 else 0
                down = opt[j][1]

                # If we are a mirror cell, reflect paths
                if grid[i][j]:
                    opt[j] = [down, right]
                else:
                    # Otherwise, all directions can go everywhere
                    paths = (right + down) % self.mod
                    opt[j] = [paths, paths]
        
        # Finally, return the total number of paths from (0, 0) to (m - 1, n - 1)
        return opt[j][0]


# opt(i, j, dir) - The number of unique valid paths from (i, j) to (m - 1, n - 1),
#                  given (i, j) is entered from the dir: 0 = left, dir: 1 = top.

# Base case:
# opt(m - 1, n - 1, _) = 1
# opt(m, _, _) = 0
# opt(_, n, _) = 0

# Recurrency:
# opt(i, j, dir) | grid[i][j] == 1 = opt(i + 1, j, 1) if dir == 0 else opt(i, j + 1, 0)
#                | otherwise = opt(i + 1, j, 1) + opt(i, j + 1, 0)

# No. states = m * n * 2
# Time complexity per state -> O(1)
# Total time complexity => O(mn)

# By using bottom-up iterative dynamic programming we can reduce
# the space complexity to O(n)!