# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Analytical solution
        return floor(-1/2 + sqrt(1+8*n)/2)

# This can be solved analytically.

# We see that the number of coins needed for a full staircase with k rows is
# equal to sum([1..k]). This is equal to the equation k*(k+1)/2.

# Given we have n coins, we want to find the lowest positive k
# such that this inequality holds: 

# n <= k*(k+1)/2
# 2*n <= k*(k+1)
# 0 <= k^2 + k - 2*n

# This can be solved through the quadratic equation:
# k = (-1 +- sqrt(1^2+8*n))/2 = -1/2 +- sqrt(1+8*n)/2

# Here it is obvious we only want the positive solution (as negative is < 0).

# Therefore, the answer is k = -1/2 + sqrt(1+8*n)/2.

# Now note, this solution has to be rounded down, as n might not fit the number
# of coins needed to build an exact staircase (the last row might be incomplete).