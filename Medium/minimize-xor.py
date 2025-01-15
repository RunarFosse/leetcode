# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Using bit manipulation
        x, set_bits = 0, num2.bit_count()

        # First make x have the same set bits as num1, from left-to-right
        while set_bits and num1:
            # Find the leftmost set bit in num1
            leftmost_bit = 1 << floor(log2(num1))

            # Remove it from num1 and add it to x
            num1 ^= leftmost_bit
            x ^= leftmost_bit
            set_bits -= 1
        
        # If we still have more bits to set, fill bits from right-to-left
        rightmost_bit = 1
        while set_bits:
            # Move bit until we find one which is unset
            while x & rightmost_bit:
                rightmost_bit <<= 1
            
            # And set the bit in x
            x ^= rightmost_bit
            set_bits -= 1

        # Finally, return x
        return x