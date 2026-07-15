# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        # First, sort upper triangle in ascending order
        for i in range(n):
            # By extracting the values
            values = [grid[j][i + j] for j in range(n - i)]
            
            # Sorting them in order
            values.sort()

            # And placing them in said order
            for j in range(n - i):
                grid[j][i + j] = values[j]
        
        # Then, do the same for lower triangle, but in decreasing order
        for i in range(n):
            values = [grid[i + j][j] for j in range(n - i)]
            values.sort(reverse=True)

            for j in range(n - i):
                grid[i + j][j] = values[j]
        
        # Finally, return the resulting grid
        return grid
