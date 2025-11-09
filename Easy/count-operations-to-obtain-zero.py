# Author: Runar Fosse
# Time complexity: O(log min(n, m))
# Space complexity: O(1)

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # Using Euclidean Algorithm

        # First, set num1 to be the larger
        if num2 < num1:
            num1, num2 = num2, num1
        
        # Then, iterate our algorithm
        operations = 0
        while num2:
            # Compute the operations at this iteration
            operations += num1 // num2

            # Perform modulo
            num1 %= num2

            # And swap to ensure that num1 stays larger
            num1, num2 = num2, num1

        # Finally, return the total number of operations
        return operations


# Given a and b, and a >= b, we have that:
# Iteration 1:
# a = a % b  b = b
# Iteration 2:
# a = a      b = b % a
# Iteration 3:
# a = a % b  b = b
# And so on, until either becomes zero.
# At each iteration, the number of operations is the (larger number // smaller number)

# This is in fact, the Euclidean Algorithm.