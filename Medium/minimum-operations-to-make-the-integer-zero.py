# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # Iterate every potential value of k
        for k in range(1, 61):
            # Compute the remaining sum of powers of 2
            remaining = num1 - k * num2

            # If this is negative, we cannot make num1 equal to 0
            if remaining < 0:
                return -1
            
            # However, if the remaining number can be created using k powers of 2
            if remaining.bit_count() <= k <= remaining:
                # We have found the minimum number of operations to zero num1
                return k

        # If loop terminates, we cannot make num1 equal to 0
        return -1

        
# We want to find the number of operations k such that:
# num1 = 2^i_1 + num2 + 2^i_2 + num2 + ... + 2^i_k + num2
#      = (2^i_1 + 2^i_2 + ... + 2^i_k) + k * num2
#
# Which gives:
# num1 - k * num2 = (2^i_1 + 2^i_2 + ... + 2^i_k)
# 
# with (2^i_1 + 2^i_2 + ... + 2^i_k) being a binary number, a sum of powers of 2.
# 
# The number of powers of 2, k, that can be used to create a bit string b is
# on the interval [set bits in b, b].

# E.g. for the number 6 = b0110, we can either use two b0100 + b0010,
# or we could use 6 * b0001. Any number in between is also valid.

# Thus, if we find a k such that num1 - k * num2 >= 0, and the resulting number can
# be created using k powers of 2, then we have our minimum operations.