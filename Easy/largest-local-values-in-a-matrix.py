# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        # For each grid cell
        for i in range(n-2):
            for j in range(n-2):
                # Iterate over the 3x3 matrix and store max
                for x in range(3):
                    for y in range(3):
                        grid[i][j] = max(grid[i+y][j+x], grid[i][j])
                
            # Remove last two values of each row
            grid[i] = grid[i][:-2]
        
        # Return the modified grid with the last two rows removed
        return grid[:-2]

# This is essentially max-pooling with kernel size (3, 3).
# This is a problem which has to be solved using brute-force, however
# we can resuse the grid-matrix given for constant space complexity.