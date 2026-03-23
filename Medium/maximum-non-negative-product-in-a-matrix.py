# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    mod = int(1e9 + 7)
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # Using dynamic programming
        m, n = len(grid), len(grid[0])
        
        # Store two arrays, one with the minimum and maximum possible products
        minimum, maximum = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]

        # Initialize the values on the edges
        minimum[0][0] = grid[0][0]
        maximum[0][0] = grid[0][0]
        for i in range(1, m):
            minimum[i][0] = maximum[i - 1][0] * grid[i][0]
            maximum[i][0] = maximum[i - 1][0] * grid[i][0]
        for j in range(1, n):
            minimum[0][j] = maximum[0][j - 1] * grid[0][j]
            maximum[0][j] = maximum[0][j - 1] * grid[0][j]

        # Then iterate the array, from the top-left to the bottom-right
        for i in range(1, m):
            for j in range(1, n):
                # Get the current element
                current = grid[i][j]

                # Compute all possible path values
                paths = (
                    maximum[i - 1][j] * current, 
                    maximum[i][j - 1] * current, 
                    minimum[i - 1][j] * current, 
                    minimum[i][j - 1] * current
                )

                # Then store the maximum and minimum element over these paths
                maximum[i][j] = max(paths)
                minimum[i][j] = min(paths)
        
        # At last, if the maximum element at the bottom right is negative, return -1
        if maximum[-1][-1] < 0:
            return -1
        
        # Otherwise, return the maximum non-negative product
        return maximum[-1][-1] % self.mod
