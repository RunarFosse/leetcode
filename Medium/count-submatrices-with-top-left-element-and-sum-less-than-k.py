# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(n)

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        # Using prefix sum
        m, n = len(grid), len(grid[0])

        # Compute the column prefix sum of the grid
        count, columns = 0, [(0)] * n
        for i in range(m):
            # For each row, compute the current submatrix sum
            current = 0
            for j in range(n):
                # Update the column prefix sum
                columns[j] += grid[i][j]

                # Update the current submatrix sum
                current += columns[j]

                # If the current submatrix sums to less than or equal to k, count it
                if current <= k:
                    count += 1
        
        # Finally, return the number of valid submatrices
        return count
