# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        # Iterate the array
        maximum = 0
        for i in range(n):
            # If a number is negative, count it
            if nums[i] < 0:
                maximum += 1
            
            # The first positive number we see
            elif nums[i] > 0:
                # Compute the maximum count of negative and positives
                maximum = max(n - i, maximum)

                # And escape the loop
                break
        
        # Finally, return the maximum count between negatives and positives
        return maximum