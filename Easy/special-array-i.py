# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # Iterate the array
        for i in range(1, len(nums)):
            # Verifying that adjacent elements have different parities
            if not (nums[i - 1] + nums[i]) % 2:
                return False
        return True