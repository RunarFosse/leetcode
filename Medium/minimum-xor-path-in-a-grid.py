# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(n)

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        # Using dynamic programming
        m, n = len(grid), len(grid[0])

        # Initialize the DP array
        opt = [[False for x in range(1024)] for j in range(n)]

        # Then, iterate every cell
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                # If we are at the last cell, set base case value
                cell = grid[i][j]
                if (i, j) == (m - 1, n - 1):
                    opt[j][cell] = True
                    continue

                # Create a temporary DP subarray for this cell
                temp = [False] * 1024
                
                # Otherwise, iterate every value for x
                for x in range(1024):
                    # Checking if any such x can be reached down, or right
                    down = i < m - 1 and opt[j][x ^ cell]
                    right = j < n - 1 and opt[j + 1][x ^ cell]
                    temp[x] = down or right
                
                # Setting the DP subarray of this cell
                opt[j] = temp

        # Finally, return the smallest XOR path possible in this grid
        return next(i for i in range(1024) if opt[0][i])


# opt(i, j, x) - If there exists a path from (i, j) to (m - 1, n - 1) with
#                an XOR sum of x.

# Base case:
# opt(m - 1, n - 1, x) = x == grid[m - 1][n - 1]
# opt(m, _, _) = False
# opt(_, n, _) = False

# Recurrency:
# opt(i, j, x) = opt(i + 1, j, x ^ grid[i][j]) or opt(i, j + 1, x ^ grid[i][j])

# No. states = m * n * k             (here k is at most 1023)
# Time complexity per state -> O(1)
# Total time complexity => O(mn)

# By utilizing iterative, bottom-up dynamic programming we can reduce the
# space complexity to O(n)!