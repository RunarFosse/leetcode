# Author: Runar Fosse
# Time complexity: O(nd)
# Space complexity: O(nd)

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # Using dynamic programming
        self.jobDifficulty = jobDifficulty
        minimum_difficulty = self.opt(0, d)
        return minimum_difficulty if minimum_difficulty < 1e9 else -1

    @functools.cache
    def opt(self, i: int, d: int) -> int:
        n = len(self.jobDifficulty)
        # Base cases
        if i == n:
            return 0 if d == 0 else 1e9
        if d == 0:
            return 1e9
        
        # Recurrency
        min_diff = 1e9
        max_current_diff = 0
        for j in range(i, n-d+1):
            max_current_diff = max(self.jobDifficulty[j], max_current_diff)
            min_diff = min(max_current_diff + self.opt(j+1, d-1), min_diff)
        
        return min_diff

# opt(i, d) - Minimum difficulty of jobs from index i, given d days

# Base case:
# opt(n, 0) = 0
# opt(n, d > 0) = Infinity
# opt(i, 0) = Infinity

# Recurrency:
# opt(i, d) = min(
#            max(jobDifficulty[i:j]) + opt(j+1, d-1) for j in [i..n]
#)

# n.o. states = n*d, runtime per state = n. Tc = O(n^2*d)
# However, we often compute the same exact state given different initial states,
# reducing our total time complexity to O(nd)!