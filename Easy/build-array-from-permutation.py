# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Iterate, build, and return the array
        return [nums[num] for num in nums]