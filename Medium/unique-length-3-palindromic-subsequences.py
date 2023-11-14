# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Find first and last occurence of a character
        # (this includes finding out if they occur twice)
        occurences = {}
        for i, c in enumerate(s):
            occurence = occurences.get(c)
            if not occurence:
                occurences[c] = (i, -1)
            else:
                occurences[c] = (occurence[0], i)
        
        # Then, for each character that occured (max 26, as those in the english alphabet)
        # we find number of unique characters between (O(26*n)=O(n))
        palindromes = 0
        uniques, seen = 0, set()
        for start, end in occurences.values():
            for i in range(start+1, end):
                if s[i] not in seen:
                    uniques += 1
                    seen.add(s[i])
            palindromes += uniques

            uniques = 0
            seen.clear()

        return palindromes
        
# A palindrome of length 3 can be generalized as a string with same start and end character,
# with an arbitray character in between.

# Counting all unique length-3 palindromic subsequences can thus be eliminated down to
# counting all unique characters between two occurences of the same character.
# Summing these will solve the problem!