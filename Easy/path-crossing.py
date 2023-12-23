# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Start at (0, 0)
        x, y = 0, 0
        visited = set([(x, y)])
        for direction in path:
            # Move in given direction
            match direction:
                case 'N':
                    y -= 1
                case 'S':
                    y += 1
                case 'E':
                    x -= 1
                case 'W':
                    x += 1

            # Check if crossing path
            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False
        