# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # Using array rotation
        m, n = len(grid), len(grid[0])

        # First, normalize the rotation around the grid
        k %= m * n

        # If the number of rotations is a multiple of the grid
        if not k:
            # Then the grid will result in the same without modification
            return grid

        # Otherwise, rotate the grid k times by first reversing entire grid
        self.reverse(grid, 0, m * n - 1, n)
        
        # Then, reverse the first k elements
        self.reverse(grid, 0, k - 1, n)

        # Finally, reverse the remaining elements
        self.reverse(grid, k, m * n - 1, n)

        # And return the resulting shifted 2D grid
        return grid
    
    def reverse(self, grid: List[List[int]], left: int, right: int, n: int) -> None:
        # Reverse the [left, right) elements in a grid, in-place
        (i1, j1), (i2, j2) = (left // n, left % n), (right // n, right % n)

        # By iterating every cell on the interval
        while i1 < i2 or (i1 == i2 and j1 < j2):
            # And swapping their positions accordingly
            grid[i1][j1], grid[i2][j2] = grid[i2][j2], grid[i1][j1]

            # And moving the two pointers together
            j1 += 1
            if j1 >= n:
                j1 -= n
                i1 += 1
            j2 -= 1
            if j2 < 0:
                j2 += n
                i2 -= 1


# Rotating an array k times is can be done by:
# 1. Reversing the whole array
# 2. Reversing the k first new elements
# 3. Reversing the remaining elements