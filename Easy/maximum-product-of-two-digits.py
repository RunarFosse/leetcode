# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def maxProduct(self, n: int) -> int:
        # Iterate all the digits in n
        product, digit = 0, 0
        while n:
            # Extract the current digit
            current = n % 10
            n //= 10

            # Store the maximum product, from multiplication with previous maximum digit
            product = max(current * digit, product)

            # And store the maximum seen digit
            digit = max(current, digit)
        
        # Finally, return this maximum product
        return product
