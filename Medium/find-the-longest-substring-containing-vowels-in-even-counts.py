# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    indices = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
    def findTheLongestSubstring(self, s: str) -> int:
        # Using bitmask prefix sum
        prefix = 0

        # Store first occurence of each even/odd character pairing
        first_occurence = [None] * 32
        first_occurence[0] = -1
        
        # Calculate prefixes on the fly, aswell as length of longest substring
        longest_substring = 0
        for i, c in enumerate(s):
            if c in self.indices:
                prefix ^= 1 << self.indices[c]
            
            if first_occurence[prefix] is None:
                first_occurence[prefix] = i
            else:
                current_substring = i - first_occurence[prefix]
                longest_substring = max(current_substring, longest_substring)
            
        # Finally return the length of the longest valid substring
        return longest_substring

# We use bitmasks to represent if a given letter has appeared an
# even or odd number of times before a given index i.
# i.e. a number of 01010 represents the letters 'e' and 'o' appearing odd
# times prior.