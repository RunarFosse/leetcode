# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # First we find the maximum value in the array
        maximum = max(nums)

        # Then we iterate the array
        longest, current = 0, 0
        for num in nums:
            # Count size of homogeneous subarrays containing array's maximum
            if num == maximum:
                current += 1
                longest = max(current, longest)
            else:
                current = 0

        # Return the size of the longest subarray
        return longest
        
# This problem is asking us to find the longest homogeneous subarray 
# containing only values equal to the maximum value of the array.