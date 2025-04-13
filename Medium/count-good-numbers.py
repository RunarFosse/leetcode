# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    mod = int(1e9 + 7)
    def countGoodNumbers(self, n: int) -> int:
        # Using fast modular exponentiation
        fives = self.modularExponentiation(5, ceil(n / 2))
        fours = self.modularExponentiation(4, floor(n / 2))
        return (fives * fours) % self.mod
    
    def modularExponentiation(self, base: int, exponent: int) -> int:
        result = 1
        while exponent > 0:
            if exponent & 1:
                result = (result * base) % self.mod
            exponent >>= 1
            base = (base * base) % self.mod
        return result
        
# There are 5 even digits (0, 2, 4, 6, 8) and 4 prime digits (2, 3, 5, 7).
# This means that, for a number of length n, we can have:
# 5 * 4 * 5 * 4 .... * 5 * 4 different good numbers, with n/2 5s and n/2 4s.

# I.e., the number of good numbers are 5^(n/2) * 4^(n/2).

# These numbers become really large really fast, so we use the fast modular
# exponentiation algorithm using the right-to-left binary method.