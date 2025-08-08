# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def soupServings(self, n: int) -> float:
        # Using dynamic programming

        # First, convert n into multiples of 25 mL
        n = (n + 24) // 25

        # If the probability of emptying slower is marginal, approximate it to 1
        if n > 200:
            return 1

        # Otherwise, count probability that A empties before B
        return self.opt(n, n)
    
    @functools.cache
    def opt(self, a: int, b: int) -> float:
        # Base case, return with base probabilities
        if min(a, b) <= 0:
            if max(a, b) <= 0:
                return 0.5
            return 1 if a <= 0 else 0
        
        # Return the total probability that A empties before B
        return 0.25 * (
            self.opt(a - 4, b) +
            self.opt(a - 3, b - 1) +
            self.opt(a - 2, b - 2) +
            self.opt(a - 1, b - 3)
        )
    
# N.o. states = n
# Time complexity per state = O(1)