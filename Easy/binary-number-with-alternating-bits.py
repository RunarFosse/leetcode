# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Using bit manipulation

        # Iterate the bits of the number
        while n:
            # If any bit pairs are non-alternating, return False
            first, second = n & 1, (n & 2) >> 1
            alternating = not first ^ second
            if alternating:
                return False
            
            # Shift bits one to the right
            n >>= 1
        
        # Otherwise, if all bits are alternating, return True
        return True
