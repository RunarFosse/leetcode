# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # Turn the array of numbers into a set
        nums = set(nums)

        # Multiply original by two while it is in the set, and then return
        while original in nums:
            original <<= 1
        return original
