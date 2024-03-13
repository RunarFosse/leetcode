# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def pivotInteger(self, n: int) -> int:
        # Using analytical solution
        x = sqrt(n * (n+1) / 2)
        pivot = int(x)
        return pivot if pivot == x else -1

# We want to find an integer x such that
# 1 + 2 + ... + x = x + (x+1) + ... + n
# 
# The arithmetic progression gives us that this is equal to
# (x(x+1))/2 = ((x+n)(n-x+1))/2
# x(x+1) = (x+n)(n-x+1)
# x^2 + x = xn - x^2 + x + n^2 - xn + n
# x^2 + x = -x^2 + x + n^2 + n
# 2x^2 = n^2 + n
#
# Which gives us that:
# x = sqrt((n^2 + n)/2) = sqrt((n(n+1))/2)

# If x is an integer, this is our pivot! If x is not, the pivot doesn't exist.