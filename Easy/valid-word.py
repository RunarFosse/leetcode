# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def isValid(self, word: str) -> bool:
        # Check each of the constraints
        length = len(word) >= 3
        alnum = word.isalnum()
        vowel = any(map(lambda c: c.lower() in "aeiou", word))
        consonant = any(map(lambda c: not (c.isdigit() or c.lower() in "aeiou"), word))

        # And return True if fulfulling them all
        return length and alnum and vowel and consonant