# Author: Runar Fosse
# Time complexity: O(mnk)
# Space complexity: O(nk)

class Solution:
    mod = int(1e9 + 7)
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        # Using dynamic programming
        m, n = len(grid), len(grid[0])
        opt = [[0] * k for _ in range(n + 1)]

        # Initialize the values for the last row
        suffix = 0
        for j in reversed(range(n)):
            suffix = (suffix + grid[-1][j]) % k
            opt[j][suffix] = 1

        # Iterate the grid bottom-up, right-to-left
        for i in reversed(range(m - 1)):
            for j in reversed(range(n)):
                # Prevent overrides by bottom cell as temporary variable
                temp = opt[j][:]
                
                # Compute the current remainder, and find paths making it k divisible
                remainder = grid[i][j] % k
                for missing in range(k):
                    path = (k - remainder + missing) % k
                    opt[j][missing] = (opt[j + 1][path] + temp[path]) % self.mod

        # Finally, return the number of paths divisible by k
        return opt[0][0]


# opt(i, j, r) - Number of paths starting at (i, j), and having a sum % k == r

# Base case:
# opt(m - 1, n - 1, r) = 1 if (r + grid[i][j]) % k == 0 else 0
# opt(m, j, r) = 0
# opt(i, n, r) = 0

# Recurrency:
# opt(i, j, r) = opt(i + 1, j, remainder) + opt(i, j + 1, remainder)
#               where remainder = (r + grid[i][j]) % k

# No. states = m * n * k
# Runtime per state = O(1)
# Total time complexity -> O(mnk)

# By going row-wise from the bottom-up, and column-wise right-to-left, we can
# solve this by only having a no. states = n * k.