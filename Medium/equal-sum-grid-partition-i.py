# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(m + n)

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # Using prefix sum
        m, n = len(grid), len(grid[0])

        # Compute prefix sum of rows and columns, as well as total grid sum
        rows, columns, total = [0] * m, [0] * n, 0
        for i in range(m):
            for j in range(n):
                current = grid[i][j]
                rows[i] += current
                columns[j] += current
                total += current

        # Iterate each row sum, checking if horizontal cuts make each partition equal
        prefix = 0
        for i in range(m):
            prefix += rows[i]
            if prefix == total - prefix:
                return True
        
        # Then iterate each column sum, doing the same
        prefix = 0
        for j in range(j):
            prefix += columns[j]
            if prefix == total - prefix:
                return True
        
        # If both loops terminate, we cannot find an equal sum grid partition
        return False
