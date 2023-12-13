# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)

# XOR is commutative and associative.
# We also have that n ^ n = 0.

# Thus as every element appears twice, we are guaranteed that, for XOR sum:
# n1 ^ n2 ^ n3 ^ ... ^ nk = n1 ^ n1 ^ n2 ^ n2 ^ ... ^ n ^ ... ^ nk ^ nk
# = 0 ^ 0 ^ ... ^ n ^ ... ^ 0 ^ 0 = n, where n is the number appearing once.