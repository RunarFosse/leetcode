# Author: Runar Fosse
# Time complexity: O(2^n)
# Space complexity: O(n)

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Using backtracking
        self.nums, self.n = nums, len(nums)

        # First, compute the OR sum of the array
        or_sum = reduce(lambda e, r: e | r, nums)

        # Then, count subsets with this OR sum
        return self.backtrack(0, 0, or_sum)

    def backtrack(self, i: int, current_or: int, or_sum: int) -> int:
        if i == self.n:
            return 1 if current_or == or_sum else 0
        
        pick = self.backtrack(i + 1, current_or | self.nums[i], or_sum)
        skip = self.backtrack(i + 1, current_or, or_sum)
        return pick + skip