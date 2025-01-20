# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        # First store coordinate of each number in a dictionary
        positions = {}
        for i in range(m):
            for j in range(n):
                positions[mat[i][j]] = (i, j)
        
        # Then store count of painted numbers in each row and column
        rows, columns = [0] * m, [0] * n

        # And for each element in the array
        for k, num in enumerate(arr):
            # Paint the current number in row and column
            i, j = positions[num]
            rows[i] += 1
            columns[j] += 1

            # If any row or column is fully painted, return
            if rows[i] == n or columns[j] == m:
                return k