# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Count character occurence in both, if they match they are anagrams
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        indices = {alphabet[i]:i for i in range(len(alphabet))}

        # Count character frequency of s
        frequencies = [0] * len(alphabet)
        for c in s:
            frequencies[indices[c]] += 1
        
        # Subtract frequency of t
        for c in t:
            # If character frequency is higher in t than s
            if not frequencies[indices[c]]:
                return False
            frequencies[indices[c]] -= 1

        # Verify difference of frequencies are 0
        return not sum(frequencies)

# Note, space complexity is O(1) as we always only store memory equal to the
# size of the english alphabet.
