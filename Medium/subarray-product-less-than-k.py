# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Using sliding window
        n = len(nums)
        result = 0

        p1, p2 = 0, 0
        current = 1
        while p2 < n:
            # Extend current window
            current *= nums[p2]
            p2 += 1

            # While product of window is larger than k, shrink it
            while p1 < p2 and current >= k:
                current /= nums[p1]
                p1 += 1
            
            # Add the size of the window
            result += p2 - p1

        return result