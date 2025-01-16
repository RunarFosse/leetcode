# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(1)

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Using bit manipulation
        result = 0
        
        # First denote a lambda for computing XOR sum of array
        xor_sum = lambda l: reduce(lambda e, r: e ^ r, l)

        # If nums1 has odd number of entries, add XOR of all in nums2
        if len(nums1) % 2:
            result ^= xor_sum(nums2)
        
        # If nums2 has odd number of entries, add XOR of all in nums1
        if len(nums2) % 2:
            result ^= xor_sum(nums1)
        
        # Finally return the XOR sum of nums3
        return result
        

# For two arrays nums1 = [a, b], nums2 = [c, d, e],
# we are looking to return the XOR of all numbers in
# nums3 = [a ^ c, a ^ d, a ^ e, b ^ c, b ^ d, b ^ e]

# This is equivalent to:
# a ^ c ^ a ^ d ^ a ^ e ^ b ^ c ^ b ^ d ^ b ^ e
# which is equal to
# a ^ a ^ a ^ b ^ b ^ b ^ c ^ c ^ d ^ d ^ e ^ e

# The property of XOR makes all integers which appear an
# even number of times cancel out.

# This leads us to the final result:
# a ^ b