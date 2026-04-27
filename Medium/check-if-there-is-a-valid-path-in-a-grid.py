# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # Using DFS
        self.m, self.n, self.grid = len(grid), len(grid[0]), grid

        # Declare valid road connections given movement
        self.connections = {
            (0, -1): [1, 4, 6],
            (0, 1): [1, 3, 5],
            (-1, 0): [2, 3, 4],
            (1, 0): [2, 5, 6]
        }

        # Follow the path given the initial start cell, returning if a valid path exists
        match grid[0][0]:
            case 1:
                return self.validPath((0, -1))
            case 2:
                return self.validPath((-1, 0))
            case 3:
                return self.validPath((0, -1))
            case 4:
                return self.validPath((0, 1)) or self.validPath((1, 0))
            case 5:
                return False
            case 6:
                return self.validPath((-1, 0))

    def validPath(self, last: Tuple[int, int]) -> bool:
        # Start at the upper-left corner
        position = (0, 0)

        # Follow the road, remembering the last visited cell
        while 0 <= position[0] < self.m and 0 <= position[1] < self.n:
            # Ensure that the current cell is a valid connection to the previous cell
            (i, j) = position
            movement = (i - last[0], j - last[1])
            if self.grid[i][j] not in self.connections[movement]:
                break
            
            # If we are at the end, there exists a valid path
            if position == (self.m - 1, self.n - 1):
                return True

            # If not, follow the path
            match self.grid[i][j]:
                case 1:
                    position = (i, j + 1) if (i, j + 1) != last else (i, j - 1)
                case 2:
                    position = (i + 1, j) if (i + 1, j) != last else (i - 1, j)
                case 3:
                    position = (i + 1, j) if (i + 1, j) != last else (i, j - 1)
                case 4:
                    position = (i, j + 1) if (i, j + 1) != last else (i + 1, j)
                case 5:
                    position = (i - 1, j) if (i - 1, j) != last else (i, j - 1)
                case 6:
                    position = (i - 1, j) if (i - 1, j) != last else (i, j + 1)
            
            # And update the last seen position
            last = (i, j)

            # If we ever return to the start, we have a loop
            if position == (0, 0):
                break
        
        # If we are out of the loop, there does not exist a valid path
        return False
