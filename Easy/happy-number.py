# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

# Complexity notes:
# n is the number of steps needed to check if n is a happy number, or loops.
# Space is O(1) as generators do not use extra auxillary space.

class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()
        while n not in visited:
            if n == 1:
                return True

            # Add current number to set
            visited.add(n)

            # Square all individual digits in n
            n = sum(pow(int(d), 2) for d in str(n))
        
        return False