# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Using Rabin-Karp (rolling hash)
        A = 1069
        B = 4153

        # First hash needle
        i = 0
        needlehash = 0
        for i in range(m := len(needle)):
            needlehash = ((needlehash * A) % B + ord(needle[i])) % B

        # Then roll over haystack, continuously hashing substring 
        # of size m and comparing to needlehash
        i = 0
        hash = 0
        while i < len(haystack):
            if i >= m:
                hash -= (ord(haystack[i - m]) * pow(A, m - 1)) % B
            hash = ((hash * A) % B + ord(haystack[i])) % B
            
            i += 1

            if hash == needlehash:
                return i - m

        return -1