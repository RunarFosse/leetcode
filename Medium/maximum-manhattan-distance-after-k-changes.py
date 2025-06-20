# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # Simulate the movement
        maximum, x, y = 0, 0, 0
        for i, c in enumerate(s):
            if c in "NS":
                y += 1 if c == "N" else -1 if c == "S" else 0
            else:
                x += 1 if c == "E" else -1 if c == "W" else 0
            
            # Compute the current possible distance by swapping k directions
            distance = abs(x) + abs(y) + 2 * k

            # The highest current distance is given by a straight line from
            # the origin, and we therefore cap it by the current index
            maximum = max(min(distance, i + 1), maximum)
        
        # Finally, return the maximum distance
        return maximum