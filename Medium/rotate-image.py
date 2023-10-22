# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Rotating by 90 degrees is the same as reversing
        # then transposing the whole matrix

        # Reverse
        matrix.reverse()

        # Transpose
        n = len(matrix)
        for i in range(n):
            row, col = i, 0
            for _ in range(ceil(i/2)):
                matrix[row][col], matrix[i-row][i-col] = matrix[i-row][i-col], matrix[row][col]
                # If we are not on the center diagonal (bottom left to top right)
                if i != n-1:
                    matrix[n-1-row][n-1-col], matrix[n-1-i+row][n-1-i+col] = matrix[n-1-i+row][n-1-i+col], matrix[n-1-row][n-1-col]

                row -= 1
                col += 1