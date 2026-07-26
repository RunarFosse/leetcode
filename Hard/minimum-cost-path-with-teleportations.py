# Author: Runar Fosse
# Time complexity: O(mn(log(mn) + k))
# Space complexity: O(mn)

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        # Using dynamic programming
        m, n = len(grid), len(grid[0])

        # First, sort all cells in ascending order of cost
        cells = [(i, j) for i in range(m) for j in range(n)]
        cells.sort(key=lambda e: grid[e[0]][e[1]])

        # Then, iterate every teleportation iteration
        opt = [[inf] * n for _ in range(m)]
        opt[m - 1][n - 1] = 0
        for t in range(k + 1):
            # First, perform a teleporation relaxation pass, if that is available
            if t > 0:
                minimum, start = inf, 0
                for end, (i, j) in enumerate(cells):
                    # By finding the minimum cost path cell we currently can jump to
                    minimum = min(opt[i][j], minimum)
                    if end < len(cells) - 1:
                        i_next, j_next = cells[end + 1]
                        if grid[i][j] == grid[i_next][j_next]:
                            continue
                
                    # And for each of the cells, jump if that cost is lower
                    for index in range(start, end + 1):
                        i, j = cells[index]
                        opt[i][j] = min(minimum, opt[i][j])
                    start = end + 1
                
            # Then, relax state by moving right- or downwards
            for i in reversed(range(m)):
                for j in reversed(range(n)):
                    # Choosing the path with least cost
                    if i < m - 1:
                        opt[i][j] = min(grid[i + 1][j] + opt[i + 1][j], opt[i][j])
                    if j < n - 1:
                        opt[i][j] = min(grid[i][j + 1] + opt[i][j + 1], opt[i][j])
        
        # Finally, return the minimum cost path from (0, 0) to (m - 1, n - 1)
        return opt[0][0]


# opt(i, j, t) - The cost of moving from cell (i, j) to (m - 1, n - 1)
#                using at most t teleportations.

# Base case:
# opt(m - 1, n - 1, _) = 0
# opt(m, j, _) = inf
# opt(i, n, _) = inf

# Recurrency:
# opt(i, j, t) = min(
#                   opt(i + 1, j, t) + grid[i + 1][j],
#                   opt(i, j + 1, t) + grid[i][j + 1],
#                   opt(i', j', t - 1),
#                )
#                where (i', j') = argmin(
#                                        opt(y, x, t - 1) 
#                                        for all (y, x) 
#                                        where grid[y][x] <= grid[i][j]
#                                  )

# No. states = m * n * k
# Time complexity per state -> O(mn)
# Total time complexity => O(m^2n^2k)

# Using bottom-up dynamic programming, teleportation steps can be done iteratively.
# This reduces space complexity to O(mn).

# Through sorting, argmin cells can then also be precomputed in O(mn) time
# per teleport iteration, further reducing time complexity per state to O(1).
# (this is a total O(mnk) complexity)

# This results in a final time complexity of O(mnk).