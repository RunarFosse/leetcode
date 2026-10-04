# Author: Runar Fosse
# Time complexity: O(k)
# Space complexity: O(1)

class Solution:
    mod = int(1e9 + 7)
    def numberOfSets(self, n: int, k: int) -> int:
        # Using combinatorics
        return comb(n + k - 1, 2 * k) % self.mod


# If we model a line segment as its left and right position, then a set of k
# line segments will look like:
# {(l_0, r_0), (l_1, r_1), ..., (l_(k-1), r_(k-1))}

# For this set to be non-overlapping, we have that:
# l_0 < r_0 <= l_1 < r_1 <= ... <= l_(k-1) < r_(k-1)

# To make this a strictly increasing constraint, we can modify it to:
# l_0 < r_0 < l_1 + 1 < r_1 + 1 < ... < l_(k-1) + (k-1) < r_(k-1) + (k-1)

# The maximum number of different such sets can easily be modeled by the number
# of ways of picking 2 * k (k different left and right positions), from the total number
# of positions in our modified strictly increasing constraint domain, n + k - 1.

# This is because, by picking 2 * k elements, we can always reshuffle them into an order
# which fulfills the strictly increasing constraint above, and thus result
# in k non-overlapping line segments!