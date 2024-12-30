# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # Using prefix sum
        n = len(nums)

        # Calculate the residual sum we need to remove from nums,
        # to make the remaining sum of array divisible by p
        residual = sum(nums) % p
        if residual == 0:
            return 0
        
        # Now iterate the array, tracking the indices of prefix sums mod p
        prefixes = {0: -1}
        current, min_length = 0, n
        for i in range(n):
            current = (current + nums[i]) % p

            # Check the difference between the current sum and the residual
            difference = (current - residual) % p

            # If this difference exists previously, store subarray
            if difference in prefixes:
                min_length = min(i - prefixes[difference], min_length)
            
            # Store index of current sum modulo p
            prefixes[current] = i
        
        # Finally, return the minimum size of subarray to be removed
        return min_length if min_length < n else -1