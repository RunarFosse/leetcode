# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        # First, count frequency of each letter
        indexOf = lambda c: ord(c) - ord("a")
        frequencies = [0] * 26
        for c in word:
            frequencies[indexOf(c)] += 1
        
        # Iterate every character
        deletions = len(word)
        for i in range(26):
            # Check how many we have to delete given this is our smallest frequency
            current = 0
            for j in range(26):
                if frequencies[j] < frequencies[i]:
                    current += frequencies[j]
                elif frequencies[j] > frequencies[i] + k:
                    current += frequencies[j] - frequencies[i] - k

            # Store the minimum number of deletions needed
            deletions = min(current, deletions)
        
        # And return it
        return deletions