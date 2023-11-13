# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def sortVowels(self, s: str) -> str:
        # First extract vowel string
        vowels = { "a", "e", "i", "o", "u" }
        vowelstring = []
        for c in s:
            if c.lower() in vowels:
                vowelstring.append(c)
        
        # Sort vowelstring
        vowelstring.sort()

        # Recreate string with sorted vowels
        i = 0
        string = ""
        for c in s:
            if c.lower() in vowels:
                string += vowelstring[i]
                i += 1
            else:
                string += c
        
        return string