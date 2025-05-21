# Author: Runar Fosse
# Time complexity: O(nlog m)
# Space complexity: O(1)

# where m denotes the maximum element

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # Using binary search
        n = len(nums)

        # Binary search the minimum possible capability
        left, right = 0, max(nums)
        while left < right:
            capability = (left + right) // 2
            
            # For a given capability, check if it is possible
            index, houses = 0, 0
            while index < n:
                if nums[index] <= capability:
                    houses += 1
                    index += 2
                else:
                    index += 1
            
            # Given the amount of houses we can rob, move the feasible interval
            if houses >= k:
                right = capability
            else:
                left = capability + 1
        
        # Finally, return the minimum possible capability
        return left