# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        # Using dynamic programming
        self.n, self.nums, self.target = len(nums), nums, target
        return self.opt(0)
    
    @functools.cache
    def opt(self, i: int) -> int:
        # Base case
        if i == self.n - 1:
            return 0
        
        # Find the next index to jump to for maximum total jumps
        can_jump = lambda j: abs(self.nums[i] - self.nums[j]) <= self.target
        jumps = max((self.opt(j) for j in range(i + 1, self.n) if can_jump(j)), default=-1)

        # If last index is not reachable, continue returning -1
        return jumps + (1 if jumps >= 0 else 0)


# opt(i) - The maximum number of jumps to reach index n - 1, starting at i

# Base case:
# opt(n - 1) = 0

# Recurrency:
# opt(i) = jumps + (1 if jumps >= 0 else 0)
#         where jumps = max(
#                   opt(j) for j in range(i + 1, n) if abs(nums[i] - nums[j]) <= target
#                )

# N.o. states = n
# Time complexity per state -> O(n)
# Total time complexity => O(n^2)