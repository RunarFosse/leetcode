# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(min(m,n))

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # If text2 is shorter than text1, swap them
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        n, m = len(text1), len(text2)
        opt = [0] * n
        # For each start index in text2 j
        for j in range(m):
            # Calculate the longest common subsequence of text1
            prev = 0
            for i in range(n):
                temp = opt[i]
                if text1[i] == text2[j]:
                    opt[i] = 1 + prev
                elif i > 0:
                    opt[i] = max(opt[i], opt[i-1])
                prev = temp

        # Return the longest common subsequence
        return opt[n-1]

        
# opt(i) is the longest common subsequence for text1[i:] and text2

# Base case:
# opt(n) = 0

# Recurrency:
# opt(i) = max(longest subsequence for text1[i:] in text2, opt(i+1))

# n.o. states = min(m, n), runtime per state O(m+n)
# Gives time complexity of O(mn), space complexity of O(min(m,n))
