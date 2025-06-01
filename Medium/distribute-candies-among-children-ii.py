# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Using analytical solution

        # First, denote a function for computing the natural sum up to a number
        natural_sum = lambda x: 0 if x < 0 else (x - 1) * x // 2

        # Then, compute the total number of solutions
        total = natural_sum(n + 2)

        # Then, subtract the solutions where a child receives more than limit
        total -= 3 * natural_sum(n - limit + 1)

        # By doing the previous, we've over counted, so we need to add back
        # half the solutions where two children receive more than the limit
        total += 3 * natural_sum(n - 2 * (limit + 1) + 2)

        # However, we've over counted again, so remove half the solutions
        # where all children receive candies over the limit
        total -= natural_sum(n - 3 * (limit + 1) + 2)

        # Finally, we are left with the number of valid solutions
        return total


# We solve this question by computing how many invalid solutions there are,
# and subtract this from the total number of solutions, giving us
# the total number of valid solutions.