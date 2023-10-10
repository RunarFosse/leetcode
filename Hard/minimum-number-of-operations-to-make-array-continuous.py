# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(1)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Using sliding window
        nums.sort()

        # Remove duplicates from list
        uniques = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[uniques] = nums[i]
                uniques += 1
        
        operations = len(nums)
        start, end = 0, 0
        while start < uniques and end < len(nums):
            while end < uniques and nums[end] - nums[start] < len(nums):
                end += 1
            operations = min(operations, len(nums) - (end - start))
            start += 1

        return operations
    