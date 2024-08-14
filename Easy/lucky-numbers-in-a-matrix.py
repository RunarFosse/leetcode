# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        # Extract desired values from row and column
        maximal_row_min = max(min(row) for row in matrix)
        minimal_col_max = min(max(col) for col in zip(*matrix))

        # If they are equal, lucky number exists, if not return empty list
        return [maximal_row_min] if maximal_row_min == minimal_col_max else []

# By nature of the definition of a lucky number in a matrix,
# there can at any poiny only exist at most one such lucky number.
# This number is the minimum number in its row, and maximum in its column.

# Therefore, we can greedily solve this problem by:
# 1. Iterate all rows, finding the maximal minimum value of every row.
# 2. Iterate all columns, finding the minimal maximum value of every column.
# 3. Compare these, if they are equal we have our lucky number.