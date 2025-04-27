# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        # Loop over the array
        subarrays = 0
        for i in range(n - 2):
            # Increment count if conditions hold
            if (nums[i] + nums[i + 2]) * 2 == nums[i + 1]:
                subarrays += 1
        
        return subarrays