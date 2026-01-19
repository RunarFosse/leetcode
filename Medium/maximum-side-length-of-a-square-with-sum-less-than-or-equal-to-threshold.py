# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # Using prefix sum
        m, n = len(mat), len(mat[0])

        # First, compute 2D prefix sum of the matrix
        prefixes = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                # Add the current value
                prefixes[i + 1][j + 1] = mat[i][j]

                # Add previous values, i.e. in above rows and left columns
                prefixes[i + 1][j + 1] += prefixes[i + 1][j]
                prefixes[i + 1][j + 1] += prefixes[i][j + 1]

                # Values prefixed from the upper left corner are counted twice, so remove
                prefixes[i + 1][j + 1] -= prefixes[i][j]
        
        # Then, iterate every position in the matrix again
        side = 1
        for i in range(m):
            for j in range(n):
                # Denote helper functions, checking if square fits and counting sum within
                square_fits = lambda s: i + s <= m and j + s <= n
                square_sum = lambda s: prefixes[i + s][j + s] - prefixes[i][j + s] - prefixes[i + s][j] + prefixes[i][j]

                # While the sum of the square is less than or equal to threshold
                while square_fits(side) and square_sum(side) <= threshold:
                    # Then increment the size of the square
                    side += 1
        
        # At last, return the maximum square with a valid sum
        return side - 1
