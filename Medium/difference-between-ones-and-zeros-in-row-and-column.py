# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(m+n)

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        # Calculate sum of rows and columns
        rows = [sum(row) for row in grid]
        columns = []
        for j in range(n):
            column_sum = 0
            for i in range(m):
                column_sum += grid[i][j]
            columns.append(column_sum)
        
        # Override grid for linear space complexity
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2 * (rows[i] + columns[j]) - (m + n)
        
        return grid
        

# Sum over each row and column, then compare. 

# For each position (i, j) we have that:
# diff[i][j] = rows[i] + columns[j] - (m - rows[i]) - (n - columns[j])
#            = 2 * (rows[i] + columns[j]) - (m + n)