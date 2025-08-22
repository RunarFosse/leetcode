# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Iterate the grid
        minimum, maximum = (m, n), (0, 0)
        for i in range(m):
            for j in range(n):
                # Skip if the current cell is not 1
                if not grid[i][j]:
                    continue

                # Otherwise, store the minimum and maximum i and j values
                minimum = (min(i, minimum[0]), min(j, minimum[1]))
                maximum = (max(i, maximum[0]), max(j, maximum[1]))

        # Finally, return the size of the rectangle covering these
        return (maximum[0] - minimum[0] + 1) * (maximum[1] - minimum[1] + 1)