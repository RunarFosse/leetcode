# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(mn)

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # Using dynamic programming
        self.s1, self.s2 = s1, s2
        self.m, self.n = len(s1), len(s2)
        return self.opt(0, 0)

    @functools.cache
    def opt(self, i: int, j: int) -> int:
        # Base case
        if i == self.m or j == self.n:
            return sum(map(ord, chain(self.s1[i:], self.s2[j:])))
        
        # If the current characters are equal, continue
        if self.s1[i] == self.s2[j]:
            return self.opt(i + 1, j + 1)
        
        # Otherwise, delete either one leading to the minimal sum
        left = ord(self.s1[i]) + self.opt(i + 1, j)
        right = ord(self.s2[j]) + self.opt(i, j + 1)
        return min(left, right)

# opt(i, j) - The minimum ASCII delete sum of s1[i:] and s2[j:]

# Base case:
# opt(m, j) = ord(s2[j:])
# opt(i, n) = ord(s1[i:])

# Recurrency:
# opt(i, j) | if s1[i] == s2[j] = opt(i + 1, j + 1)
#           | otherwise = min(ord(s1[i]) + opt(i + 1, j), ord(s2[j]) + opt(i, j + 1))

# No. states = mn
# Time complexity per state = O(1)
# Total time complexity -> O(mn)