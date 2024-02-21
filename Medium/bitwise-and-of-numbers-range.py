# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Using bit manipulation
        if left == right:
            return left & right

        result = 0
        # Bitwise comparison from left to right
        pointer = floor(log2(right))
        while left >> pointer == right >> pointer:
            result += (left >> pointer & 1) << pointer
            pointer -= 1

        return result


# 0101 - 5
# 0110 - 6
# 0111 - 7

# We see that the bitwise and of all numbers in the inclusive range is equal
# to the contiguous bits from the left that are equal in the edge numbers.