# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        # Iterate the array
        last = - k - 1
        for i in range(n):
            # If it is 0, skip it
            if not nums[i]:
                continue
            
            # Otherwise, verify that it is at least k positions from the previous
            if i - last <= k:
                return False
            
            # And remember its position
            last = i
        
        # Otherwise, every 1 is at least k positions apart
        return True
