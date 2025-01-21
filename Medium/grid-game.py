# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # Using prefix sum
        n = len(grid[0])

        # Compute suffix sum of the first row, prefix sum of the second row
        for i in range(1, n):
            grid[0][n - i - 1] += grid[0][n - i]
            grid[1][i] += grid[1][i - 1]

        # Then for each index i
        points = None
        for i in range(n):
            # Compute the maximum points robot 2 gets
            current = 0
            if i > 0:
                current = max(grid[1][i - 1], current)
            if i < n - 1:
                current = max(grid[0][i + 1], current)
            
            # And make sure robot 1 minimizes it
            points = current if points is None else min(current, points)
        
        # Finally, return robot 2's optimal points
        return points
        

# The grid is constrained to only having two rows. This reduces the complexity
# of our problem. Our first robot will therefore pick i values from the
# first row, then (n - i) values from the second row.

# Afterwards, the second robot can either choose to pick the remaining
# (n - i) values from the first row, or the first i values from the second.

# Therefore, we need to find an i such that the remaining maximum possible
# value (from either (n - i) from first or i from second) is minimized!