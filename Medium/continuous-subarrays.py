# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # Using two pointer
        n = len(nums)

        # Iterate the list
        subarrays, start = 0, 0
        max_min = (0, 0)
        for i in range(n):
            # Update max and min for current window
            max_min = (max(nums[i], max_min[0]), 
                       min(nums[i], max_min[1]))

            # If window is not continuous
            if max_min[0] - max_min[1] > 2:
                # Expand window backwards from i
                start = i
                max_min = (nums[i], nums[i])
                while start and abs(nums[i] - nums[start - 1]) <= 2:
                    start -= 1
                    max_min = (max(nums[start], max_min[0]), 
                               min(nums[start], max_min[1]))
            
            # Count number of new continuous subarrays
            subarrays += i - start + 1
        
        # Return total number of continuous subarrays
        return subarrays
            