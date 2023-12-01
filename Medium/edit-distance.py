# Author: Runar Fosse
# Time complexity: O(m*n)
# Space complexity: O(n)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Using Levenshtein distance (Two row approach)
        if not word1:
            return len(word2)

        m, n = len(word1), len(word2)
        previous, current = [i for i in range(n+1)], [0 for _ in range(n+1)]
        
        for i in range(0, m):
            current[0] = i+1

            for j in range(0, n):
                if word1[i] == word2[j]:
                    current[j+1] = previous[j]
                else:
                    current[j+1] = 1 + min(current[j], previous[j+1], previous[j])

            previous = current.copy()
        
        return current[n]
