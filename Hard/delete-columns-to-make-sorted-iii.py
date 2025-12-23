# Author: Runar Fosse
# Time complexity: O(mn^2)
# Space complexity: O(n)

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Using dynamic programming
        self.n, self.strs = len(strs[0]), strs

        # Return the complemented longest common lexicographical subsequence
        longest = max(self.opt(i) for i in range(self.n))
        return self.n - longest

    @functools.cache
    def opt(self, i: int) -> int:
        # Count all common lexicographical subsequences with this index
        isValid = lambda j: all(row[i] <= row[j] for row in self.strs)
        subsequences = (self.opt(j) + 1 for j in range(i + 1, self.n) if isValid(j))
        
        return max(subsequences, default=1)

# We can compute the minimum possible column deletion by computing and complementing
# the maximum number of non-deleted columns.
# These said columns are equal to the longest common lexicographical subsequence.

# opt(i) - Longest common lexicographical subsequence of strs including each row at i.

# Base case:
# opt(n - 1) = 1

# Recurrency:
# opt(i) = max(opt(j) + 1 for j in [i+1..n-1] if all rows[i] <= rows[j])

# No. states = n
# Time complexity per state = mn
# Total time complexity -> O(mn^2)

# Space complexity per state is constant due to generator usage!