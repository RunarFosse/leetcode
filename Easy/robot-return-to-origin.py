# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Using simulation

        # Store the robot's current position
        x, y = 0, 0
        
        # Simulate all of the robot's moves
        for move in moves:
            match move:
                case "U":
                    y += 1
                case "D":
                    y -= 1
                case "L":
                    x += 1
                case "R":
                    x -= 1
            
        # Finally, if we are back at the origin, return True
        return (x, y) == (0, 0)
