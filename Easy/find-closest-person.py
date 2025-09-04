# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # Compute the distance to person 3 from both 1 and 2
        distance1, distance2 = abs(x - z), abs(y - z)

        # If they are equal, return 0
        if distance1 == distance2:
            return 0
        
        # Otherwise, return the closest person
        return 1 if distance1 < distance2 else 2