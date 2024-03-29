# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # Using sliding window
        n = len(nums)
        subarrays = 0
        
        # First find the maximum element
        maximum = max(nums)

        # Keep track of a window with only k max-elements in it
        # and use it to count number of subarrays
        p1, p2 = 0, 0
        occurences = 0
        while p2 < n:
            # Expand the window
            if nums[p2] == maximum:
                occurences += 1
            p2 += 1
            
            # If it contains k max-elements, shrink it again
            while p1 < p2 and occurences == k:
                if nums[p1] == maximum:
                    occurences -= 1
                p1 += 1
            
            # Then add the number of possible subarrays
            subarrays += p1

        # Return the number of subarrays
        return subarrays
