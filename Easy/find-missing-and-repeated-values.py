# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # First iterate the grid, computing the sum, and sum of squares
        sums = (0, 0)
        for row in grid:
            for num in row:
                sums = (sums[0] + num, sums[1] + pow(num, 2))
        
        # Then, compute the difference from real sum
        n_squared = pow(len(grid), 2)
        actual = (
            n_squared * (n_squared + 1) // 2,
            n_squared * (n_squared + 1) * (2 * n_squared + 1) // 6
        )
        difference = sums[0] - actual[0]
        difference_squared = (sums[1] - actual[1]) // difference

        # And compute a and b
        a = (difference + difference_squared) // 2
        b = (difference_squared - difference) // 2
        return [a, b]

# We have that the sum of all numbers [1, n^2] is equal to:
# n^2 * (n^2 + 1) / 2
#
# And we have that the grid sum is equal to:
# n^2 * (n^2 + 1) / 2 - b + a
# 
# Meaning the difference between the grid sum and the sum is:
# a - b
#
# The sum of all square numbers of [1, n^2] is equal to:
#
# n^2 * (n^2 + 1) * (2n^2 + 1) / 6
#
# By computing the sum of squares as well, we have the difference:
# a^2 - b^2 = (a + b)(a - b)
#
# By dividing with the previous difference, we find
# (a^2 - b^2) / (a - b) = a + b
#
# These are two equations, which we can use to find both a and b:
# 
# a = ((a - b) + (a + b)) / 2
# b = ((a + b) - (a - b)) / 2
# 
# Voila.