# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Using Binary search
        l, r = 0, len(nums)-1

        if nums[r] < target:
            return r + 1
        if nums[l] >= target:
            return l

        while l < r:
            pivot = (l + r) // 2

            if nums[pivot] < target:
                l = pivot
            else:
                r = pivot

            if l == r - 1:
                return r
        
        return r