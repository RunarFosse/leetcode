# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Using dynamic programming
        self.dictionary = set(dictionary)
        self.s, self.n = s, len(s)
        return self.opt(0)
    
    @functools.cache
    def opt(self, i: int) -> int:
        if i == self.n:
            return 0
        
        # Keep count of the current word
        word = ""

        # Iterate the rest of the string, keeping track on least extra chars
        extraCharacters = self.n
        for j in range(i, self.n):
            word += self.s[j]

            # If the current word is in the dictionary, try breaking it
            if word in self.dictionary:
                extraCharacters = min(self.opt(j+1), extraCharacters)

            # If not, count it as extra characters
            extraCharacters = min(len(word) + self.opt(j+1), extraCharacters)

        # Return the minimum number of extra characters
        return extraCharacters


# opt(i) - Minimum number of extra characters left over breaking up
#          the string s[i:]

# Base case:
# opt(n) = 0

# Recurrency:
# opt(i) = min(opt(j) if s[i:j+1] in dictionary else opt(j) + (j-i)
#              for j in range(i+1, n))

# N.o. states = n
# Runtime per state = O(n)
# Time complexity -> O(n^2)