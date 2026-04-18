# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def mirrorDistance(self, n: int) -> int:
        # Compute the mirror of the given number
        mirror = self.reverse(n)

        # And return the mirror distance
        return abs(n - mirror)
    
    def reverse(self, n: int) -> int:
        # Reverse the digits of a given number
        reverse = 0
        while n:
            reverse *= 10
            reverse += n % 10
            n //= 10
        
        return reverse
