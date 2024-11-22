# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # First create a grid of the cells
        cells = [[0] * n for _ in range(m)]
        
        # Declare constants
        UNSEEN, SEEN = 0, 1
        GUARD, WALL = 2, 3

        # Assign guard and wall cells
        for guard in guards:
            cells[guard[0]][guard[1]] = GUARD
        for wall in walls:
            cells[wall[0]][wall[1]] = WALL

        # Declare a helper function for iterating cells
        def updateCells(i: int, j: int, visible: bool) -> bool:
            cell = cells[i][j]
            if cell == UNSEEN and visible:
                cells[i][j] = SEEN
            
            if cell == GUARD:
                return True
            if cell == WALL:
                return False

            return visible
        
        # Then iterate each row
        for i in range(m):
            # From left to right
            visible = False
            for j in range(n):
                visible = updateCells(i, j, visible)

            # From right to left
            visible = False
            for j in reversed(range(n)):
                visible = updateCells(i, j, visible)
        
        # And then iterate each column
        for j in range(n):
            # From top to bottom
            visible = False
            for i in range(m):
                visible = updateCells(i, j, visible)

            # From bottom to top
            visible = False
            for i in reversed(range(m)):
                visible = updateCells(i, j, visible)
        
        # Finally return all unseen cells
        return sum(cell == UNSEEN for row in cells for cell in row)