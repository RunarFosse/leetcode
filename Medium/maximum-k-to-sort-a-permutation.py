# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # Compute the cumulative bitwise AND of incorrectly placed elements
        k = ~0
        for i, num in enumerate(nums):
            if i != num:
                k &= num
        
        # The maximum k to sort the permutation is this cumulative bitwise AND
        return 0 if k is -1 else k


# To sort this permutation we need to move every element in the wrong position.
# Because nums is a permutation of [0, n - 1], then every number exists in the array.
# If we compute the cumulative AND of all elements incorrectly placed, we'll get a k.
# 0 <= k <= n - 1, meaning k will exist in the array itself.

# Because k is computed from the cumulative AND of all incorrectly placed elements,
# we have that for an incorrect placed x, then:
# x & k == k.

# This allows us to use k as an intermediate swapping element
# to sort the entire permutation!

# We only need to move incorrectly placed elements to sort the entire array permutation.
# Adding k defined as the cumulative bitwise AND allows us to do so freely, with the
# addition that we also now are moving k.