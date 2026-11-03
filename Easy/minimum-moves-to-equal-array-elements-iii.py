# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Increment every element until equal to the array's maximum
        moves = len(nums) * max(nums) - sum(nums)

        # This is the minimum number of moves to make the array equal
        return moves


# To make this array equal we obviously need to increment every element to reach
# the array's maximum value. This can be shortened down to the closed solution:
# len(nums) * max(nums) - sum(nums).