# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def reverseBits(self, n: int) -> int:
        # 32 bit integer, therefore we run to 32
        reverse = 0
        for _ in range(32):
            reverse = (reverse << 1) | (n & 1)
            n >>= 1
        
        return reverse