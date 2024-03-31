# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # Using sliding window
        n = len(nums)
        subarrays = 0

        minLast, maxLast = -1, -1

        p1, p2 = 0, 0
        while p2 < n:
            # Expand the window to the right
            if nums[p2] == minK:
                minLast = p2
            if nums[p2] == maxK:
                maxLast = p2
            p2 += 1
            
            # Reset window if last element was outside fixed bounds
            if nums[p2-1] < minK or nums[p2-1] > maxK:
                p1 = p2
            
            # Calculate number of subarrays with fixed bounds within window
            if minLast >= p1 and maxLast >= p1:
                subarrays += min(minLast, maxLast) - p1 + 1
        
        return subarrays