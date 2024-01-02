# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(m)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Using dynamic programming
        m, n = len(s1), len(s2)
        if len(s3) != m + n:
            return False

        # Base cases
        opt = [True] + [False] * n
        for i in range(n):
            opt[i+1] = opt[i] and s2[i] == s3[i]
        
        # Recurrency
        for j in range(m):
            # Store if s1[:j] == s3[:j]
            opt[0] = opt[0] and s1[j] == s3[j]
            for i in range(n):
                opt[i+1] = (opt[i] and s2[i] == s3[i+j+1]) or (opt[i+1] and s1[j] == s3[i+j+1])

        return opt[n]

# opt(i) - If we can interleave s3[:i+j+1] for any j using s1[:j], s2[:i].

# This is a pick/skip scenario.

# Base case:
# opt(0) = True
# opt(i) = True for any i such that s2[:i] == s3[:i]

# Recurrency:
# opt(i) = (opt(i-1) and s2[i-1] == s3[i+j-1]) or (opt(i) and s1[j-1] == s3[i+j-1])


# N.o. states = m, runtime per state = n.
# Time complexity -> O(mn)