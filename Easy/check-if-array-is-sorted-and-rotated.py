# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        # Iterate the array, counting breaks in ascending order
        breaks = 0
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                breaks += 1
        
        # The array is sorted and rotated if breaks is less than 2
        return breaks < 2