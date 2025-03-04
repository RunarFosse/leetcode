# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            # Check if division results in a 2
            if n % 3 == 2:
                return False

            # Divide the number by 3
            n //= 3
        
        # If loop terminates, it is a sum of powers of 3
        return True

# We have that a power of 3 can create the numbers:
# 3^0 = 1
# 3^1 = 3
# 3^2 = 9
# ...
# And any combinations of these are a sum of powers of 3.
# We can see, that both 1 and 3 are powers of 3, but not 2.
# Therefore, we can continue dividing by 3, and checking if we at
# any point have a remainder of 2. If so, it will not be a sum of powers of 3.