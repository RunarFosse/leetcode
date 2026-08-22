# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # First, compute the digit sum and digit product
        sum, product, current = 0, 1, n
        while current:
            digit = current % 10
            current //= 10

            sum += digit
            product *= digit
        
        # And check if n is divisible by their sum
        return n % (sum + product) == 0
