# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(m + n)

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        # Using dynamic programming
        m, n = len(word2), len(word1)

        # First, find the longest possible suffix of word2 we can match in word1
        opt, j = [0] * (n + 1), m - 1
        for i in reversed(range(n)):
            opt[i] = opt[i + 1]
            if j >= 0 and word1[i] == word2[j]:
                opt[i] += 1
                j -= 1

        # Then try to greedily pick low indices from word1, replacing the one we found
        indices, j, replaced = [], 0, False
        for i in range(n):
            # We replace this character if we afterwards can create the rest of word2
            canReplace = not replaced and opt[i + 1] >= m - j - 1
            if word1[i] == word2[j] or canReplace:
                replaced = replaced or word1[i] != word2[j]
                indices.append(i)
                j += 1
                if j == m:
                    break
        
        # If our indices do not create the whole word2
        if len(indices) < m:
            # Then there is no such index subsequence
            return []
        
        # Otherwise, return our lexicographically smallest index subsequence
        return indices


# opt(i) - The length of the longest suffix of word2 that exists as a subsequence
#          of indices in word1, at or after index i.

# Base case:
# opt(n) = 0

# Recurrency:
# opt(i) | word1[i] == next = 1 + opt(i + 1)
#        | otherwise = opt(i + 1)
#        where next = word2[m - opt(i + 1) - 1]

# No. states = n
# Time complexity per state -> O(1)
# Total time complexity => O(n)