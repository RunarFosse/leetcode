# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    mod = 12345
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # Using prefix sum
        m, n = len(grid), len(grid[0])

        # Compute the prefix and suffix product of the grid
        prefixes, suffixes = [1], [1]
        for i in range(m):
            for j in range(n):
                prefixes.append(prefixes[-1] * grid[i][j] % self.mod)
                suffixes.append(suffixes[-1] * grid[m - i - 1][n - j - 1] % self.mod)

        # Then, compute and return the full product matrix
        return [[prefixes[n * i + j] * suffixes[-(n * i + j + 2)] % self.mod for j in range(n)] for i in range(m)]
