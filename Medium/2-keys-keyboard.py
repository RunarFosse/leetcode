# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minSteps(self, n: int) -> int:
        # Using prime factorization
        operations = 0
        prime = 2
        while n > 1:
            # If prime is a factor of n, perform divison operations
            # (equivalent to one copy and prime-1 pastes)
            while not n % prime:
                n //= prime
                operations += prime
            
            # Then increment the prime number
            prime += 1
        
        # Return the minimum number of operations
        return operations
