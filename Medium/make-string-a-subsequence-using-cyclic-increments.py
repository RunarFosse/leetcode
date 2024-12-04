# Author: Runar Fosse
# Time complexity: O(n + m)
# Space complexity: O(1)

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # Using two pointers
        m, p = len(str2), 0

        # Iterate the first string
        for c in str1:
            # If c can be operated into str2's char, increment the pointer
            if p < m and ord(str2[p]) - ord(c) in [-25, 0, 1]:
                p += 1
        
        # If all chars in str2 are iterated, then str2 can be a subsequence
        return p == m