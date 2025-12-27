# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Using sliding window
        n = len(nums)

        # Slide a window over the array
        subarrays = 0
        current, start = 0, 0
        for end in range(n):
            # Expand the window by adding value of current element to sum
            current += nums[end]

            # Shrink the window while having a score equal to or larger than k
            while current * (end - start + 1) >= k:
                current -= nums[start]
                start += 1
            
            # Then, count subarrays with score less than k, ending at end
            subarrays += end - start + 1
        
        # Finally, return this number of subarrays of score less than k
        return subarrays
