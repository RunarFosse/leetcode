# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count frequencies of characters in string
        indexOf = lambda c : ord(c) - ord("A")
        frequencies = [0] * 58
        for c in s:
            frequencies[indexOf(c)] += 1
        
        # Add together all evenly occuring characters,
        # keeping track if there ever is an odd-occuring character
        length, exists_odd = 0, False
        for freq in frequencies:
            if freq % 2:
                exists_odd = True
            length += (freq // 2) * 2
        
        # Return length of longest palindrome
        return length + 1 if exists_odd else length

