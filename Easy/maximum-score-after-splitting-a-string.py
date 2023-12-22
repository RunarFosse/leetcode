# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxScore(self, s: str) -> int:
        ones = sum(int(c) for c in s)

        maxscore = 0
        left, right = 0, ones
        for i in range(len(s)-1):

            if s[i] == '0':
                left += 1
            else:
                right -= 1

            maxscore = max(left+right, maxscore)
        
        return maxscore