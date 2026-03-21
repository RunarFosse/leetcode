# Author: Runar Fosse
# Time complexity: O(k^2)
# Space complexity: O(1)

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # Iterate the upper half of the submatrix
        for i in range(k // 2):
            for j in range(y, y + k):
                # Flip the submatrix vertically
                top_i, bottom_i = x + i, x + k - i - 1
                grid[top_i][j], grid[bottom_i][j] = grid[bottom_i][j], grid[top_i][j]
        
        # Then return the updated matrix
        return grid
