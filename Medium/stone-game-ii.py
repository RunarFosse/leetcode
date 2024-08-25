# Author: Runar Fosse
# Time complexity: O(n^3)
# Space complexity: O(n)

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # Using dynamic programming
        self.n = len(piles)

        # First create a suffix sum list out of the piles list
        self.suffix = [0] * self.n
        self.suffix[-1] = piles[-1]
        for i in reversed(range(self.n-1)):
            self.suffix[i] = piles[i] + self.suffix[i+1]
        
        print(self.suffix)
        
        # Then perform dynamic programming
        return self.opt(0, 1)
    
    @functools.cache
    def opt(self, i: int, m: int) -> int:
        # Take all stones if current player can
        if i + 2 * m >= self.n:
            return self.suffix[i]
        
        # If not, return the maximum amount they can take
        return max(self.suffix[i] - self.opt(i+x, max(m, x)) for x in range(1, 2*m+1))


# opt(i, m) - Maximum number of stones the current player can get, starting
#             from index i, given m

# Base case:
# opt(i, m) = suffix[i]       given that i + 2m >= n 

# Recurrency:
# opt(i, m) = max(suffix[i] - opt(i+x+1, max(m, x)) for x in range(1, 2m+1))

# N.o. states = n^2
# Runtime per state is O(n)
# Final time complexity is O(n^3)