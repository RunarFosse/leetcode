# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Using analytical solution
        return True


# We are ensured that the length of the stone piles will be even.
# This results in the set of indices:
# {1, 2, 3, ..., n - 1, n},         where n is even.

# As the current player can only pick stones from either end of the array,
# the first player can force itself to pick either only even or odd indexed stones.
# The second player will then be forced to pick the remaining indexed stones.
# The first player is guaranteed to win if they pick the one with the
# maximal cumulative sum (which exists as the total sum of stones in the array is odd).

# Proof:
# We have the indices: {1, 2, 3, ..., n - 1, n},         where n is even.
#
# The first player picks either odds: 1, or evens: n.
# The next player is then forced to pick the other evens (2 or n), or odds (1 or n - 1).
# The first player then picks the same, odd (3 or n - 1), or even (2 or n - 2),
# that opens up based on the next player's choice.
#
# This goes on until there are no more stones and the first player has the highest score!