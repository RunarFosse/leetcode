# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        if negative:
            x = -x

        num = 0
        while x:
            # Check if number will overflow
            if (num >= 2**31/10 and not negative) or (num > 2**31/10 and negative):
                return 0

            num *= 10
            num += x % 10
            x //= 10
            
        return -int(num) if negative else int(num)

# Time complexity is O(log_10(n))