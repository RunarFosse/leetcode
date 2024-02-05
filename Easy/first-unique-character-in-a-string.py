# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        indexOf = lambda c : ord(c) - ord("a")
        occurences = [0] * 26

        # Count character occurences´
        for c in s:
            occurences[indexOf(c)] += 1
        
        # Reiterate string, returning index of first char occuring only once
        for i, c in enumerate(s):
            if occurences[indexOf(c)] == 1:
                return i
        
        # If no such character is found, return -1
        return -1