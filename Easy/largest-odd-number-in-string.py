# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in reversed(range(len(num))):
            if int(num[i]) % 2:
                return num[:i+1]

        return ""
        

# This is a simple problem.
# From the back, find the first odd digit. 
# If the first (from behind) odd digit is at index i, then the largest
# odd number substring in num will be num[:i+1], obviously.