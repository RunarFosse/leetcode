# Author: Runar Fosse
# Time complexity: O(nk)
# Space complexity: O(n)

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Using dynamic programming
        self.n = len(stones)
        self.stones = stones

        return self.opt(0, 0)

    @functools.cache
    def opt(self, i: int, k: int) -> int:
        if i == self.n - 1:
            return True

        for j in range(i+1, min(i+k+2, self.n)):
            difference = self.stones[j] - self.stones[i]
            if abs(difference - k) > 1:
                continue
            
            if self.opt(j, difference):
                return True
        
        return False
        

# This is a basic dynamic programming problem

# opt(i, k) - if frog can land on the last stone from index i given last jump of length k

# Base case:
# opt(n-1, k) = True
# opt(i >= n, k) = False

# Recurrency:
# opt(i, k) = False   if abs(difference - k) > 1 else   opt(j, difference)
# given difference = abs(stones[j] - stones[i])
# do this for j = i+1, i+2, ..., i+k and or the results


# no. states = n, runtime per state = O(k), tc = O(nk)