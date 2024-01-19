# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Using dynamic programming
        n = len(matrix)
        for i in reversed(range(n-1)):
            for j in range(n):
                belows = (matrix[i+1][max(min(k, n-1), 0)] for k in [j-1, j, j+1])
                matrix[i][j] += min(belows)

        return min(matrix[0][j] for j in range(n))

# opt(i, j) - minimum sum of falling path starting at row i, column j

# Base case:
# opt(n, j) = 0
# opt(i, j < 0 or j >= n) = Infinity

# Recurrency:
# opt(i, j) = matrix[i, j] + min(opt(i+1, j-1), opt(i+1, j), opt(i+1, j+1))


# N.o. states = n^2, runtime per state = O(1)
# => TC and SC of O(n^2).

# However, if we instead perform the iterative, bottom-up dp, we can reduce
# space complexity by overwriting given matrix instead! Thus giving SC of O(1)!