# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def countBits(self, n: int) -> List[int]:
        set_bits = [0]
        leftmost = 1
        for i in range(n):
            if i+1 >= leftmost << 1:
                leftmost <<= 1 
            set_bits.append(1 + set_bits[i+1 - leftmost])
        return set_bits

# Following incremental iterative unrolling of set bits it is easy to see
# that for a number n, the set bits is equal to 1 + the number of set bits in the
# number n - 2**leftmost_bit.