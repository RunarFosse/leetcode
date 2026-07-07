# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Iterate the digits of n
        x, sum, base = 0, 0, 0
        while n:
            digit = n % 10
            n //= 10

            # If the digit is non-zero
            if digit:
                # Add digit to x, and increment sum
                x += digit * pow(10, base)
                sum += digit
                base += 1
        
        # Finally, return the multiplication of x and sum
        return x * sum
