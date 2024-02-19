# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not n & (n - 1)

# A number is a power of 2 if it is bigger than 0, and it only contains 1 set
# bit. The easiest way to verify that only 1 bit is set is to verify that the
# intersection of n and (n - 1) is 0!