# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)

        # Read and ignore leading whitespace
        while i < n and s[i] == " ":
            i += 1
        if i >= n:
            return 0
        
        # Check sign of number
        negative = False
        if s[i] == "+" or s[i] == "-":
            negative = s[i] == "-"
            i += 1
        
        # Read in all digits
        number, digits = 0, [str(n) for n in range(10)]
        while i < n and s[i] in digits:
            number *= 10
            number += int(s[i])
            i += 1

            # Check if number has overflown, if so, clamp it
            if number > 2**31 and negative:
                return -2**31
            if number >= 2**31 and not negative:
                return 2**31 - 1
        
        # Turn number negative if it should be
        if negative:
            number *= -1
        
        return number 