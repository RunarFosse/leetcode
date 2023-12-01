# Author: Runar Fosse
# Time complexity: O(mn(m+n))
# Space complexity: O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # Check rows
        for i in range(m):
            noned = False
            # Check columns
            for j in range(n):
                # If cell is 0
                if matrix[i][j] == 0:
                    # None out row (if not already noned)
                    if not noned:
                        noned = True
                        for k in range(n):
                            # If current value is not 0
                            if matrix[i][k]:
                                matrix[i][k] = None

                    # None out column
                    for k in range(m):
                        if matrix[k][j]:
                            matrix[k][j] = None

        # At the end, replace all Nones with zeroes
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
        
        return matrix
