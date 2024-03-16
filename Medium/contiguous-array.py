# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Using prefix sum
        n = len(nums)
        prefixes = {}

        # Compute prefix sum, storing maximal difference between equal prefixes
        result = 0
        prefix, prefixes[0] = 0, -1
        for i in range(n):
            prefix += 1 if nums[i] else -1
            if prefix in prefixes:
                result = max(i - prefixes[prefix], result)
            else:
                prefixes[prefix] = i
        
        return result
