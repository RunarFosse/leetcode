# Author: Runar Fosse
# Time complexity: O(sqrt(c))
# Space complexity: O(1)

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Loop over every value of a on the bounded interval [0, sqrt(c)]
        for a in range(floor(sqrt(c)+1)):
            b = sqrt(c - pow(a, 2))
            if b.is_integer():
                return True
        
        # If the loop terminates, no integer b satisfies the equation
        return False

# We are can solve this by finding out if there exists a positive integer b
# for any value of a such that a^2 + b^2 = c. Reformulated, for every 
# integer a we check if b = sqrt(c - a^2) also is an integer. If so, we have
# found our pair.

# We know that we have a lower bound of 0 for both numbers, meaning that
# there could exist a solution a^2 = c, leading to an upperbound a = sqrt(c).

# This solution is more efficient than using binary search, as the sqrt
# operation runs in O(1) time, as it consist of a single floating point operation.