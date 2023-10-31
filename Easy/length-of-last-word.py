# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        i = len(s)
        while i and s[i-1] == " ":
            i -= 1
        
        wordlength = 0
        while i and s[i-1] != " ":
            wordlength += 1
            i -= 1
        
        return wordlength
