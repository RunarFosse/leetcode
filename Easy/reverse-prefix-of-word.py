# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)

        # Find first occurence of ch
        for i in range(n):
            if word[i] == ch:
                # If at the end, reverse whole string
                if i == n-1:
                    return word[::-1]
                
                # If not, construct string with prefix reversed
                return word[(i-n)::-1] + word[(i+1):]
        
        # If ch does not exist in word, do nothing
        return word