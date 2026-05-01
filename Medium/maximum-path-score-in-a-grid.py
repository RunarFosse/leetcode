# Author: Runar Fosse
# Time complexity: O(mnk)
# Space complexity: O(nk)

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        # Using dynamic programming
        m, n = len(grid), len(grid[0])

        # Iterate the grid
        opt = [[-1] * (k + 1) for _ in range(n)]
        for i in reversed(range(m)):
            # Store the current row as a temporary array
            temp = [[-1] * (k + 1) for _ in range(n)]

            # Then, iterate the row from the right
            for j in reversed(range(n)):
                for cost in range(k + 1):
                    # Compute the new cost given current grid cell value
                    new_cost = cost + (1 if grid[i][j] > 0 else 0)
                    if new_cost > k:
                        break

                    # If we are at the end cell, set base case value
                    if (i, j) == (m - 1, n - 1):
                        temp[j][cost] = grid[i][j]
                        continue

                    # Otherwise, get the highest path score by going down and rightwards
                    down = opt[j][new_cost] if i < m - 1 else -1
                    right = temp[j + 1][new_cost] if j < n - 1 else -1
                    
                    # If either path is valid, store the best score
                    if max(down, right) >= 0:
                        temp[j][cost] = grid[i][j] + max(down, right)
            
            # Then, override the current opt row from the temporary array
            opt = temp

        # Finally, get the maximum path score in the grid and return it
        return opt[0][0]


# opt(i, j, k) - Maximum path score starting from (i, j) with an initial cost of k

# Base case:
# opt(m - 1, n - 1, k) = grid[i][j]
# opt(m, _, _) = -inf
# opt(_, n, _) = -inf
# opt(_, _, -1) = -inf

# Recurrency:
# opt(i, j, k) = grid[i][j] + max(opt(i + 1, j, k_new), opt(i, j + 1, k_new))
#               where k_new = k - (1 if grid[i][j] > 0 else 0)

# N.o. states = m*n*k
# Runtime per state -> O(1)
# Total time complexity => O(mnk)

# With space optimization, space complexity goes to O(nk)