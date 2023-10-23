# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and not log2(n) % 2
    
# A function is a power of 4, 4^x, can be rewritten as 2^(2x).
# A number power 4 can also not be <= 0.
# Therefore if the logarithm base 2 of n is an even number, and n > 0,
# then n is a power of 4.