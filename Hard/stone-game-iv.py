# Author: Runar Fosse
# Time complexity: O(nsqrt(n))
# Space complexity: O(n)

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # Using dynamic programming
        return self.opt(n)
    
    @functools.cache
    def opt(self, i: int) -> bool:
        # If there are no stones left to take, we've lost
        if i == 0:
            return False
        
        # Otherwise, pick any non-zero square number less than i
        current = 1
        while current * current <= i:
            # If picking this amount wins, return early
            if not self.opt(i - current * current):
                return True
            current += 1
        
        # If neither pick can win, this results in a loss
        return False


# opt(i) - If the current player can win by both players playing optimally,
#          given that the current player can pick from i stones.

# Base case:
# opt(0) = False

# Recurrency:
# opt(i) = any(not opt(i - j * j) for j in [1..sqrt(i) + 1])

# No. states = n
# Time complexity per state -> O(sqrt(n))
# Total time complexity => O(nsqrt(n))