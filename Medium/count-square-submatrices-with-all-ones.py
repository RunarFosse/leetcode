# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Using dynamic programming
        m, n = len(matrix), len(matrix[0])

        opt = [[0] * (n + 1) for _ in range(m + 1)]
        count = 0
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                # If the current element is 1
                if matrix[i][j]:
                    # Add current and all subsequent square submatrices of 1s
                    opt[i][j] = 1 + min(
                        opt[i + 1][j], opt[i][j + 1], opt[i + 1][j + 1]
                        )

                # And add current square submatrices to count
                count += opt[i][j]
        
        # Finally return the count of square submatrices of 1s
        return count
        
# opt(i, j) - The number of square matrices filled with strictly 1s,
#             with a upper left most corner at index (i, j)