# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        # Using sliding window
        n = len(nums)

        # Initially, compute the target sum of the inner subarray
        target = sum(nums) - x

        # If the target is negative or zero, we already have our answer
        if target <= 0:
            # As if it is zero, we need the whole array as our subarray,
            # but if it is negative, no subarray sum can ever equal it
            return n if target == 0 else -1

        # Slide a window over the array
        maximum = 0
        start, window = 0, 0
        for end in range(n):
            # Expand it
            window += nums[end]

            # If the window sum is greater than the target
            while window > target:
                # Shrink it
                window -= nums[start]
                start += 1
            
            # If we have found a subarray with a sum equalling the target
            if window == target:
                # Storing the maximum size of this subarray
                maximum = max(end - start + 1, maximum)
        
        # If there is no such subarray
        if maximum == 0:
            # We cannot reduce x to 0
            return -1
        
        # Otherwise, the minimum number of operations equals the complement subarray size
        return n - maximum


# Another way of thinking of this problem is finding a subarray inside of nums s.t.
# sum(nums) - sum(subarray) = x,
# which can be rearranged as:
# sum(subarray) = sum(nums) - x

# This is trivially done using a sliding window, with the minimum number of operations
# equalling the complement of the maximum sized such subarray.