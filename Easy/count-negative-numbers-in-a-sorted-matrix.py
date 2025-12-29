# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(1)

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Using staircase method
        m, n = len(grid), len(grid[0])

        # Keep count of negative numbers in the grid
        negatives = 0

        # Iterate each column in the grid
        i = m
        for j in range(n):
            # While the current element is negative, move row pointer upwards
            while i and grid[i - 1][j] < 0:
                i -= 1
            
            # At the end of this column, count its number of negative numbers
            negatives += m - i

        # And return the total number of negative numbers
        return negatives

# Staircase method has time complexity O(m + n) as we at most iterate either every
# column index once (trivial from the for loop), or row index at most once, due
# to the while loop always incrementing upwards.