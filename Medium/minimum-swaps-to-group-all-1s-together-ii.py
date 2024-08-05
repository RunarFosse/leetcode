# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Using sliding window
        n = len(nums)

        # Count number of ones in the array
        ones = sum(nums)

        # If there are no ones in the array the answer is trivial
        if not ones:
            return 0

        # Slide a "ones"-sized window over the array
        start, end = 0, 0
        zeros, min_zeros = 0, 1e9
        while end < 2*n:
            # Expand the window until big enough
            while end-start < ones:
                if not nums[end%n]:
                    zeros += 1
                end += 1
            
            # Store minimum number of zeros
            min_zeros = min(zeros, min_zeros)

            # Shrink the window
            if not nums[start%n]:
                zeros -= 1
            start += 1
        
        # Return the minimum number of zeros
        return min_zeros
        

# Here, as the array is circular, we work with an "extended array"
# (just two arrays appended together) to find the correct answer.