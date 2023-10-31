# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Using greedy algorithm

        reach = 0
        for i in range(n := len(nums)):
            if reach < i:
                return False

            reach = max(i + nums[i], reach)
            if reach >= n:
                return True

        return True