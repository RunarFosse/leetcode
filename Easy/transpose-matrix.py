# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = [[] for _ in range(len(matrix[0]))]
        for row in matrix:
            for i, num in enumerate(row):
                transposed[i].append(num)

        return transposed