# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Using bitwise operations
        quotient = 0

        # Compute sign of result, and make both positive
        either = (abs(dividend) != dividend or abs(divisor) != divisor)
        both = (abs(dividend) != dividend and abs(divisor) != divisor)
        sign = -1 if either and not both else 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)

        # If dividend is less than divisor, answer is always 0
        if dividend < divisor:
            return 0

        # Perform bitwise division algorithm
        n = floor(log2(dividend))
        while n >= 0:
            if dividend >= divisor << n:
                dividend -= divisor << n
                quotient += pow(2, n)
            n -= 1
        
        # Return clamped output
        return min(max(sign * quotient, -pow(2, 31)), pow(2, 31) - 1)