# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # Increment n at most nine times
        for _ in range(10):
            # Compute the current digit product
            current, product = n, 1
            while current:
                product *= current % 10
                current //= 10

            # If the digit product becomes divisible by t
            if product % t == 0:
                # We've found our smallest solution
                break
            
            # Otherwise, increment n by one
            n += 1
        
        # So return it
        return n


# We need to find the smallest number greater than or equal to n, such that
# its digit product is divisible by t.

# Luckily, the problem does not require strictly non-zero digit solutions.
# The number zero is divisible by all number, meaning the simple solution
# would be to fish for this trivial solution.
# At most, any number is only nine increments away from a zero digit.