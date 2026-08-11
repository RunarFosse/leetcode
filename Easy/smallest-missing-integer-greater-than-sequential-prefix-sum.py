# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(n)

# where m is the maximum element in the array

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # First, compute the value of the longest sequential prefix
        prefix, last = 0, None
        for num in nums:
            if last is not None and num != last + 1:
                break
            prefix += num
            last = num
        
        # Then, because n is small, find the next largest not in the array by brute force
        elements = set(nums)
        while prefix in elements:
            prefix += 1
        
        # Finally, return this prefix as our integer x
        return prefix
