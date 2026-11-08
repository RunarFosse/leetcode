# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(m + n)

class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        # Count the number of servers at each row and column
        m, n = len(grid), len(grid[0])
        rows = [sum(row) for row in grid]
        columns = [sum(column) for column in zip(*grid)]

        # Then iterate the grid
        communicates = 0
        for i in range(m):
            for j in range(n):
                # A server communicates with another if it shares a row or a column
                if grid[i][j] and (rows[i] > 1 or columns[j] > 1):
                    communicates += 1
        
        # Finally, return the number of server which communicate with another
        return communicates
