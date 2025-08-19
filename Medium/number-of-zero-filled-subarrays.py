# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count, current = 0, 0
        for num in nums:
            # Increment current
            current += 1

            # But reset if number is not a zero
            if num:
                current = 0

            # Count all current zero filled subarrays
            count += current
        
        # And return them
        return count
