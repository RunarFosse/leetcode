# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # We cannot have an arithmetic slice if array size is less than
        # minimum possible size of said slice.
        if len(nums) < 3:
            return 0

        i = 1
        diff, size = 0, 0
        arithmetic_slices = 0
        while i < len(nums):
            # If at the start of slice, count difference
            if size == 0:
                diff = nums[i] - nums[i-1]
                size = 2
                i += 1
                continue

            # If difference matches, count slice size and add to total slices
            if nums[i] - nums[i-1] == diff:
                size += 1
                arithmetic_slices += (size - 2)
                i += 1
                continue

            # If not, continue from end
            diff, size = 0, 0
        
        return arithmetic_slices

# For each number in the array, we check if it starts an arithmetic subarray.
# If it does, continue counting until it doesn't. Then continue from there.


# Note: Given a "largest" arithmetic subarray of size k, then the total number
# of arithmetic subarrays that can be created from said subarray is equal to
# sum([1..k-2]).

# E.g., subarray [1, 2, 3, 4, 5] has size 5, and can create sum([1..3]) = 6
# arithmetic slices:
#  [1, 2, 3, 4, 5]
#  [1, 2, 3, 4], [2, 3, 4, 5]
#  [1, 2, 3], [2, 3, 4], [3, 4, 5]