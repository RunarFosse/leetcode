# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"

        # Keep a frequency count of all the letters
        indexOf = lambda c: ord(c) - ord("a")
        frequencies = [0] * 26

        # Iterate the string
        max_vowel, max_consonant = 0, 0
        for c in s:
            # Counting frequencies
            frequencies[indexOf(c)] += 1

            # And keeping track of maximum frequency for both vowel and consonant
            frequency = frequencies[indexOf(c)]
            if c in vowels:
                if frequency > max_vowel:
                    max_vowel = frequency
            else:
                if frequency > max_consonant:
                    max_consonant = frequency
        
        # Finally, return the sum of the maximum vowel and consonant frequencies
        return max_vowel + max_consonant