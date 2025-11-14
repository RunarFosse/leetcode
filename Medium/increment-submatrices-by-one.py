# Author: Runar Fosse
# Time complexity: O(m + n^2)
# Space complexity: O(n^2)

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Using prefix sum 

        # Initialize the matrix with zeros
        matrix = [[0] * n for _ in range(n)]

        # Iterate the queries
        for row1, col1, row2, col2 in queries:
            # Incrementing and decrementing at each corner of the square
            matrix[row1][col1] += 1
            if col2 < n - 1:
                matrix[row1][col2 + 1] -= 1
            if row2 < n - 1:
                matrix[row2 + 1][col1] -= 1
            if max(row2, col2) < n - 1:
                matrix[row2 + 1][col2 + 1] += 1

        # Perform column-wise, followed by row-wise prefix sum
        for row in range(n):
            prefix = 0
            for col in range(n):
                prefix += matrix[row][col]
                matrix[row][col] = prefix
                if row > 0:
                    matrix[row][col] += matrix[row - 1][col]
        
        # Finally, return the resulting matrix
        return matrix


# To solve this using prefix sum, a given square row1, col1, row2, col2, can be set:
# With row1 = 1, col1 = 1, row2 = 3, col2 = 3, in a 6x6 zero-matrix, we have:
#
# 0 0 0 0 0 0
# 0 1 0 0 -1 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 -1 0 0 1 0
# 0 0 0 0 0 0

# First, do column-wise prefix sum, resulting in this matrix:
#
# 0 0 0 0 0 0
# 0 1 1 1 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 -1 -1 -1 0 0
# 0 0 0 0 0 0

# Then, finish with row-wise prefix sum, for our final matrix:
#
# 0 0 0 0 0 0
# 0 1 1 1 0 0
# 0 1 1 1 0 0
# 0 1 1 1 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0