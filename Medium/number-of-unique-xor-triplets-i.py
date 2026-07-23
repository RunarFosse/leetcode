# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # Using bit manipulation
        n = len(nums)

        # If we have less than 2 different values
        if n <= 2:
            # We are very constrained in which values we can create
            return n

        # Otherwise, compute k as the most significant bit of the whole array
        k = max(nums).bit_length()

        # And compute the number of possible values
        return (1 << k)


# The number of numbers we can create depend on the number of linearly independent
# numbers (e.g. numbers with only 1 set and different bit. -> 00010 and 00100 and 01000).

# Using 00001 and 00010 and 00011 and 00100 and 00101 we can create:
# 00001 and 00010 and 00011 and 00100 and 00101, but we can also create
# 00000 and 00111 and 00110.

# In fact, given numbers [1..n] with n having the (1-indexed) k as the most significant 
# bit, we can create all numbers of the range [0..2^(k - 1)] (exactly like above),
# if using three different numbers as an XOR triplet!

# However, if we have less than 2 values, this is not the case. This is because we can't
# create 0. In either case, we can only reconstruct either of the values in the array.

# This however makes the problem trivial.