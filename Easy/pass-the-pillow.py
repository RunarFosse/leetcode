# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Direction is 0 if indices are increasing, 1 if decreasing
        direction = time // (n-1) % 2
        
        # Offset is how far pillow is from "initial" person this direction
        offset = time % (n-1)
        
        # Return index given current direction of pillow
        return 1+offset if not direction else n-offset