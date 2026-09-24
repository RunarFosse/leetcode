# Author: Runar Fosse
# Time complexity: O(nlog m)
# Space complexity: O(1)

# where m is the maximum element of the array

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # Iterate the array
        for i, num in enumerate(nums):
            # Compute the digit sum
            digits = 0
            while num:
                digits += num % 10
                num //= 10
            
            # Returning the first index where the digit sum is equal
            if digits == i:
                return i
        
        # If loop terminates, there is no such number
        return -1
