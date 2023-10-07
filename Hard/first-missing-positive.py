# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Using modified Cyclic sort
        i = 0
        while i < len(nums):
            j = nums[i]
            # We only care to swap numbers within the range [1, len(nums)]
            if j > 0 and j <= len(nums) and j != nums[j-1]:
                # Swap nums[i] and nums[j]
                nums[i], nums[j-1] = nums[j-1], nums[i]
            else:
                i += 1

        missing = 1
        for n in nums:
            if n == missing:
                missing += 1

        return missing


# The trick with this one is understanding that "O(1) auxiliary space"
# does not prevent modification of the given array.
# Therefore we can use a version of Cyclic sort (which is O(n) and in-place!)