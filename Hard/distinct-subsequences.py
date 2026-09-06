# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(n)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Using dynamic programming
        m, n = len(s), len(t)

        # Iterate every index in s
        opt = [0] * n + [1]
        for i in reversed(range(m)):
            for j in range(n):
                # If it matches a subsequence in t
                if s[i] == t[j]:
                    # Increment said subsequence
                    opt[j] += opt[j + 1]
        
        # Finally, return all finished subsequences of t
        return opt[0]


# opt(i, j) - The number distinct subsequences from s[i:] matching t[j:]

# Base case:
# opt(m, _) = 0
# opt(_, n) = 1

# Recurrency:
# opt(i, j) | s[i] == t[j] = opt(i + 1, j + 1) + opt(i + 1, j)
#           | otherwise = opt(i + 1, j)

# No. states = m * n
# Time complexity per state -> O(1)
# Total time complexity => O(mn)

# By using iterative bottom-up dynamic programming we can reduce 
# the space complexity to O(n)!