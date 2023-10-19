# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # Using prefix min/max
        left, right = 0, indexDifference
        prefixmin = prefixmax = 0

        for _ in range(len(nums) - indexDifference):
            if nums[left] < nums[prefixmin]:
                prefixmin = left
            if nums[right] - nums[prefixmin] >= valueDifference:
                return [prefixmin, right] 

            if nums[left] > nums[prefixmax]:
                prefixmax = left
            if nums[prefixmax] - nums[right] >= valueDifference:
                return [prefixmax, right]
            
            left += 1
            right += 1

        return [-1, -1]