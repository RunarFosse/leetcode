# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def maxDiff(self, num: int) -> int:
        # First, find the two first digits
        first, second, third = self.findFirstDigits(num)

        # Replace the first non-9 with a 9
        maximum = self.replaceDigit(num, first if first != 9 else second, 9)

        # In addition, replace the first with 1 if not already
        if first != 1:
            minimum = self.replaceDigit(num, first, 1)
        # Otherwise, replace the second with 0 if not already
        elif second != 0:
            minimum = self.replaceDigit(num, second, 0)
        # Otherwise, the third has to become 0
        else:
            minimum = self.replaceDigit(num, third, 0)

        # Lastly, return the difference
        return maximum - minimum
        
    def findFirstDigits(self, num: int) -> (int, int):
        first, second, third = None, None, None
        while num:
            num, remainder = divmod(num, 10)
            if remainder != first:
                if remainder != second:
                    third = second
                second = first
                first = remainder
        
        return first, second, third
    
    def replaceDigit(self, num: int, replace: int, digit: int) -> int:
        result, multiplum = 0, 1
        while num:
            num, remainder = divmod(num, 10)
            result += (digit if remainder == replace else remainder) * multiplum
            multiplum *= 10
        
        return result