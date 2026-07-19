# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # Using Tarjan's algorithm
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid

        # For Tarjan's algorithm, store discovery and low-link values per cell
        self.discovery = [[-inf] * self.n for _ in range(self.m)]
        self.low = [[-inf] * self.n for _ in range(self.m)]

        # Also keep track of land cells, and articulation points
        self.lands, self.articulations = 0, 0

        # Iterate the grid, counting connected components
        components = 0
        for i in range(self.m):
            for j in range(self.n):
                # If we find an undiscovered land cell, perform DFS
                if self.grid[i][j] and self.discovery[i][j] < 0:
                    self.dfs((i, j), 0, parent=None)

                    # Count this as a connected component
                    components += 1
        
        # If there already are no, or several components
        if components != 1:
            # The islands are already disconnected
            return 0
        
        # If there is only one land cell, or we have an articulation point
        if self.lands == 1 or self.articulations > 0:
            # Then we can disconnect the island in one move
            return 1
        
        # If not, the island can be disconnected in two days
        return 2

    def dfs(self, position: Tuple[int, int], depth: int, parent: Optional[Tuple[int, int]]) -> None:
        # Extract indices from current position
        i, j = position

        # Initially set discovery and low-link depth equal
        self.discovery[i][j] = depth
        self.low[i][j] = depth

        # Count as a land position
        self.lands += 1

        # Traverse neighbours, and count DFS-tree children
        children, is_articulation = 0, False
        for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if not (0 <= i + a < self.m and 0 <= j + b < self.n and self.grid[i + a][j + b]):
                continue
            
            # Do not traverse back to the DFS parent
            if (i + a, j + b) == parent:
                continue

            # If this neighbour has been seen before
            if self.discovery[i + a][j + b] >= 0:
                # Inherit its discovery depth as this low-link value if lower
                self.low[i][j] = min(self.discovery[i + a][j + b], self.low[i][j])
                continue
            
            # Otherwise, this neighbour is undiscovered, count and traverse it
            children += 1
            self.dfs((i + a, j + b), depth + 1, (i, j))

            # If that child has a lower low-link value, inherit it
            self.low[i][j] = min(self.low[i + a][j + b], self.low[i][j])

            # If this is a non-root node, and this node's discovery depth
            # is smaller or equal to the low-link value of our neighbour
            if parent is not None and self.discovery[i][j] <= self.low[i + a][j + b]:
                # Then it is an articulation point
                is_articulation = True

        # After traversing neighbours, if this is a root and has many valid children
        if parent is None and children >= 2:
            # Then this is also an articulation point
            is_articulation = True
        
        # And count this cell as an articulation point if that is the case
        if is_articulation:
            self.articulations += 1


# We can use Tarjan's algorithm to find articulation points, that is, points that, if
# removed, increase the number of connected components. If there is such a point within
# this grid, then that means we can disconnect the island in only 1 day — by removing
# such an articulation point. 
# If there are no such points, we can disconnect the island in 2 days. This follows
# because every island on a finite grid contains a cell with at most two neighbours. 
# Removing those neighbouring cells isolates the chosen cell from the rest of the island.
# If the island itself consists of only 2 cells, it instead takes 2 days to remove both.

# This only applies if the island is not already disconnected, or if the island only
# consists of 1 cell, which can be computed during the initial Tarjan's algorithm DFS.