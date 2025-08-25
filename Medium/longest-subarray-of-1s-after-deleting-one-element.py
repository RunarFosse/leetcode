# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Using sliding window
        n = len(nums)

        # Keep a window of the last, and current subarray of 1s
        longest = 0
        start, split = 0, None
        for i in range(n):
            # Count subarray size if current element is a 1
            if nums[i] == 1:
                longest = max(i - start + (1 if split is None else 0), longest)
                continue
            
            # Otherwise, perform a new split and update windows
            if split is not None:
                start = split + 1
            split = i
        
        # If there are no zeroes, remove a 1 :(
        if split is None:
            longest -= 1
        
        # Finally, return the longest subarray of 1's after removing the split
        return longest
            

            
