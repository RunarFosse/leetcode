# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        operations = 0
        flipped_bits = 0
        while n:
            # Find the leftmost set bit
            leftmost = floor(log2(n))

            # Add the number of operations to flip this bit, following formula found below
            operations += (pow(2, leftmost+1) - 1) * (-1 if flipped_bits % 2 else 1)

            n -= pow(2, leftmost)
            flipped_bits += 1

        return operations
            

# n = 0 (0000) => 0
# n = 1 (0001) => 1
# n = 2 (0010) => 3
# n = 3 (0011) => 2
# n = 4 (0100) => 7
# n = 5 (0101) => 6
# n = 6 (0110) => 4
# n = 7 (0111) => 5
# n = 8 (1000) => 15
# n = 9 (1001) => 14
# etc...

# We can see that there exists a pattern here.

# 1. The operations needed when only the n'th bit is set is equal to 2^n - 1, unless n = 0.
# 2. When two bits are set n_1 and n_2 (n_1 > n_2), the operations needed is equal to:
#       (2^n_1 - 1) - (2^n_2 - 1) = 2^n_1 - 2^n_2
# 3. This is generalized to, for bits set n_1, n_2, ..n_m we have that the operations:
#       (2^n_1 - 1) - ((2^n_2 - 1) - ((2^n_3 - 1) - (... - (2^n_m - 1))))

# We can easily find the leftmost bit by taking floor(log_2(n)).
# This makes the problem trivial.