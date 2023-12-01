# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # One-pass algorithm (follow up problem)
        p, n = 0, len(nums)
        start, end = 0, n - 1
        while p <= end:
            # If color is 0, swap to beginning
            if nums[p] == 0:
                nums[start], nums[p] = nums[p], nums[start]
                start += 1
                # Swapping to beginning means adding a number behind, increasing p
                p += 1
            # If color is 2, swap to end
            elif nums[p] == 2:
                nums[end], nums[p] = nums[p], nums[end]
                end -= 1
            # If color is 1, let it stay
            else:
                p += 1
        
        return nums
        