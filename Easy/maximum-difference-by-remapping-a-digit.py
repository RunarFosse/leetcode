# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def minMaxDifference(self, num: int) -> int:
        # Using greedy

        # First, extract the first (not 9) and last occuring digit (not 0)
        first, last, current = None, None, num
        while current:
            current, digit = divmod(current, 10)
            if digit != 9:
                first = digit
            if digit != 0:
                last = digit
        
        # Greedily make the first and last occuring digits 9 and 0 respectively
        maximum, minimum, multiplum = 0, 0, 1
        while num:
            num, digit = divmod(num, 10)
            maximum += (9 if digit == first else digit) * multiplum
            minimum += (0 if digit == last else digit) * multiplum
            multiplum *= 10
        
        # Finally, return the difference
        return maximum - minimum
