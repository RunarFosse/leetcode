# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        indexOf = lambda c : ord(c) - ord("a")
        
        # Count letter frequencies of s
        frequencies = [0] * 26
        for c in s:
            frequencies[indexOf(c)] += 1
        
        # Subtract the frequencies of t
        for c in t:
            frequencies[indexOf(c)] -= 1
        
        # Calculate the cumulative letter frequency difference
        return sum(abs(frequency) for frequency in frequencies) // 2


# Count frequency of each letter in s and t. The minimum number of steps to make
# t an anagram of s will be the cumulative difference of every letter frequency
# divided by two (as replacing one character would mean modifying two frequencies)