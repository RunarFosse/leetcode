# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # Using prefix sum
        n = len(nums)

        # First, compute a prefix sum array over the queries
        prefixes = [0] * (n + 1)
        for l, r in queries:
            prefixes[l] += 1
            prefixes[r + 1] -= 1

        # Then, iterate the nums array and counting prefix sum
        prefix = 0
        for i in range(n):
            prefix += prefixes[i]
            
            # Return False if the current prefix is smaller than the number
            if prefix < nums[i]:
                return False
        
        # Otherwise, return True
        return True