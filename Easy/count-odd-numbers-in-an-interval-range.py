# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Using analytical solution
        return (high + 1 >> 1) - (low >> 1)

# x // 2 gives the number of odd numbers on the interval [0, x).
# This makes the solution trivial.