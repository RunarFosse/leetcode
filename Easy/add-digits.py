# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        remainder = num % 9
        return remainder if remainder else 9

# The solution is obvious when writing out every number
# together with their final 1 digit sum.