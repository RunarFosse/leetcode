# Author: Runar Fosse
# Time complexity: O(2^n)
# Space complexity: O(2^n)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Using dynamic programming
        self.n, self.nums = len(nums), nums
        return self.backtrack(0, target)

    @functools.cache
    def backtrack(self, i: int, target: int) -> int:
        # If we are at the end, return
        if i == self.n:
            return 1 if target == 0 else 0
        
        # Otherwise, compute further
        expressions = 0
        expressions += self.backtrack(i+1, target + self.nums[i])
        expressions += self.backtrack(i+1, target - self.nums[i])

        return expressions