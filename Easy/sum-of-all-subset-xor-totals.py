# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Using bit manipulation
        n = len(nums)
        return reduce(lambda prev, elem : prev | elem, nums) << (n-1)

# Due to us XOR-ing every subset, it will be the case that any overlapping
# bits will be set to 1 in half of the subsets, and 0 in half of the subsets.

# This means that we can compute which bits are set over the whole array,
# using OR sum of the array, and multiply by the number of subsets / 2.
# (As bits will be set in HALF of all subsets, we count ones and multiply
# by the number of subsets in HALF of all subsets, i.e. no. subsets / 2).

# As the number of possible subsets is 2^n, we have that half the
# number of subsets is equal to 2^(n-1).