# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        # Iterate the array
        current, last = 1, None
        for i in range(1, n):
            # Keep count of the number of strictly increasing elements
            if nums[i] <= nums[i - 1]:
                last = current
                current = 0
            current += 1

            # If the we have two k-sized strictly increasing subarrays adjacent
            if current >= 2 * k or (current >= k and last != None and last >= k):
                # Return true
                return True
        
        # Otherwise, return false
        return False