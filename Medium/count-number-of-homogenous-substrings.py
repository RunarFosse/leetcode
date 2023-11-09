# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    mod = int(1e9 + 7)
    def countHomogenous(self, s: str) -> int:
        count_homogenous = 0

        char, count = s[0], 1
        for i in range(1, len(s)):
            if s[i] != char:
                count_homogenous += count*(count+1)//2
                char = s[i]
                count = 0
            count += 1
        count_homogenous += count*(count+1)//2

        return count_homogenous % self.mod
        
# This problem can be reduced to finding the length of every longest homogenous substring
# in the string, as we easily can extrapolate the total number of homogenous substrings.

# i.e. "aaaa" contains 1 "aaaa", 2 "aaa", 3 "aa", 4 "a".
# This holds for all homogenous substrings.