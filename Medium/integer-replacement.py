# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def integerReplacement(self, n: int) -> int:
        operations = 0
        while n > 1:
            if n % 2:
                if n % 4 == 1 or n == 3:
                    n -= 1
                else:
                    n += 1
                operations += 1
            
            n //= 2
            operations += 1
        
        return operations

        
# We greedily find the solution. Whenever n is odd, we check mod 4.
# If mod 4 is 3, the best solution would be to add 1. Otherwise, subtract 1.
# Note, this does not hold for n == 3, as here subtracting 1 is always optimal.