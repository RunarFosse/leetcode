# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Using greedy
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]

        # Start from the top row, adding the biggest number you can to each
        # cell, ensuring neither row or column sum becomes negative.
        row, column = 0, 0
        while row < m and column < n:
            # Insert the max value such that neither become negative
            value = min(rowSum[row], colSum[column])

            matrix[row][column] += value
            colSum[column] -= value
            rowSum[row] -= value

            # If any sum is 0, increment pointers
            if not rowSum[row]:
                row += 1
            if not colSum[column]:
                column += 1

        # Return the populated matrix
        return matrix
        