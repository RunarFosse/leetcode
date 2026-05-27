# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Store the last index of lower case, first index of upper case characters
        lower, upper = [None] * 26, [None] * 26
        indexOf = lambda c: ord(c) - ord("a")

        # Iterate the word
        for i, c in enumerate(word):
            index = indexOf(c.lower())
            if c.islower():
                lower[index] = i
            elif upper[index] is None:
                upper[index] = i
        
        # Finally, return the number of special characters
        isSpecial = lambda i: (
            lower[i] is not None and 
            upper[i] is not None and 
            lower[i] < upper[i]
        )
        return sum(1 for i in range(26) if isSpecial(i))
