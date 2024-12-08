# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # Using dynamic programming
        n = len(grid)

        # If grid is one cell, there is only one valid answer
        if n == 1:
            return grid[0][0]

        # Store last row's total falling path sum
        total_min, total_second_min = None, None

        # First fill initial values from first row
        for j in range(n):
            value = grid[0][j]
            if not total_min or value <= total_min[0]:
                total_second_min = total_min
                total_min = (value, j)
            elif not total_second_min or value <= total_second_min[0]:
                total_second_min = (value, j)
        
        # Then iterate the rest of the rows, downwards
        for i in range(1, n):
            # First find current rows first and second minimum
            current_min, current_second_min = None, None
            for j in range(n):
                # Count current valid falling sum
                if j != total_min[1]:
                    value = grid[i][j] + total_min[0]
                else:
                    value = grid[i][j] + total_second_min[0]

                # Update current mins
                if not current_min or value <= current_min[0]:
                    current_second_min = current_min
                    current_min = (value, j)
                elif not current_second_min or value <= current_second_min[0]:
                    current_second_min = (value, j)
            
            # Then change rows
            total_min = current_min
            total_second_min = current_second_min

        # Finally return the minimum total falling path sum
        return total_min[0]

# This is a shortest path through a DAG problem, with the constraint
# that we can never go straight down. (but to any other cell below!)

# opt(i, j) - Shortest path through grid starting at row i, column j

# Base case:
# opt(m, j) = 0
# opt(i, j < 0 or j >= n) = inf

# Recurrency:
# opt(i, j) = grid[i, j] + min(opt(i+1, j') for j' in range(n) if j != j')

# From this, a very good optimization follows, that we only need to remember
# the current minimum and second minimum value from the last row! This is
# because either the current minimum is, or isn't the cell directly above!
# This will make our final space complexity be O(1)!!