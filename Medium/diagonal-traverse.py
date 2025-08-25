# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])

        # Return an array of the matrix traversed diagonally
        return [mat[i][j] for i, j in self.diagonalRange(m, n)]
    
    def diagonalRange(self, m: int, n: int) -> Iterator[Tuple[int, int]]:
        # Declare helper functions
        increment = lambda i, j, pred: (i - 1, j + 1) if pred else (i + 1, j - 1)
        bounded = lambda i, j, pred: (i >= 0 and j < n) if pred else (j >= 0 and i < m)

        # Get a diagonal traversal of an (m x n) matrix
        forward = True
        for k in range(m + n):
            # Initialize the current indices to be valid
            i, j = (k, 0) if forward else (0, k)
            if i >= m or j >= n:
                i, j = (m - 1, k - m + 1) if forward else (k - n + 1, n - 1)
            
            # And iterate over them diagonally
            while bounded(i, j, forward):
                yield i, j
                i, j = increment(i, j, forward)
            
            # At the end, flip the direction
            forward = not forward

        
# Indices in diagonal order (of a 3x3 matrix):
# [0][0] - [0][1] - [1][0] - [2][0] - [1][1] - [0][2] - [1][2] - [2][1] - [2][2]