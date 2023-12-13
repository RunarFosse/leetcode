# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ones = []

        rows, columns = [], []
        # Iterate rows
        for i in range(m):
            rows.append(sum(mat[i]))
        # Iterate columns
        for j in range(n):
            column_sum = 0
            for i, row in enumerate(mat):
                column_sum += row[j]
                # If cell is 1, add to ones-queue
                if row[j]:
                    ones.append((i,j))
            columns.append(column_sum)

        # Iterate ones-queue, verifying special positions
        special_positions = filter(lambda pos : rows[pos[0]] == 1 and columns[pos[1]] == 1, ones)
        return len(list(special_positions))
        
# First iterate over every column and row, storing their sum.
# Then, given a position (i, j), we can verify that it is a special position given
# that both the column and row sum will be 1.
# Also, on this first iteration, store positions containing 1-s.