# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        # Create a new, rotated grid
        rotated = [[0] * n for _ in range(m)]

        # Iterate the grid, layer by layer
        layers = min(m // 2, n // 2)
        for layer in range(layers):
            rows, columns = m - 2 * layer, n - 2 * layer
            
            # Then, iterate each position along this layer
            for position in range(2 * (rows - 1 + columns - 1)):
                # Then, compute the rotated target position
                target = (position + k) % (2 * (rows - 1 + columns - 1))

                # Find the row and column coordinates of position and target
                i1, j1 = self.coordinatesOf(position, rows, columns)
                i2, j2 = self.coordinatesOf(target, rows, columns)

                # Inset all coordinates to match current layer
                i1 += layer
                j1 += layer
                i2 += layer
                j2 += layer
                
                # And set value in rotated grid
                rotated[i1][j1] = grid[i2][j2]

        # Finally, return the cyclically rotated grid    
        return rotated
    
    def coordinatesOf(self, position: int, rows: int, columns: int) -> Tuple[int, int]:
        # Helper function to compute cartesian coordinates from integer position
        if position < columns:
            return (0, position)
        elif position < (columns - 1) + rows:
            return (position - (columns - 1), columns - 1)
        elif position < 2 * (columns - 1) + rows:
            return (rows - 1, 2 * (columns - 1) - (position - (rows - 1)))
        return (2 * (rows - 1) - (position - 2 * (columns - 1)), 0)


# We can tackle each layer by themselves, and store coordinates as a single number,
# i.e. step around of the layer, instead of the combined (x, y) coordinates.

# We have that 0 = (0, 0), 1 = (1, 0), ..., n - 1 = (n - 1, 0), n = (n - 1, 1), ...,
# (n - 1) + (m - 1) = (n - 1, m - 1), n + (m - 1) = (n - 2, m - 1), ..., 
# 2 * (n - 1) + (m - 1) = (0, m - 1), ..., 2 * (n - 1) + 2 * (m - 1) = (0, 0)

# This way we can easily modulo the rotations and directly compute the resulting
# position of an element after rotation.

# (x, y) | position < n               = (position, 0)
#        | position < (n - 1) + m     = (n - 1, position - (n - 1))
#        | position < 2 * (n - 1) + m = (2 * (n - 1) - (position - (m - 1)), m - 1)
#        | otherwise                  = (0, 2 * (m - 1) - (position - 2 * (n - 1)))

# From this, we can have the source position,
# and can compute the target (position + k) % (2 * ((n - 1) + (m - 1)))