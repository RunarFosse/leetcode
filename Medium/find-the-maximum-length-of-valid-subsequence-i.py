# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Using dynamic programming
        self.n, self.nums = len(nums),nums

        # Compute each of the subsequence lengths given start index and modulo
        lengths = (self.opt(i, even) for i in range(self.n) for even in [True, False])

        # Return the longest one
        return max(lengths)
        
    @functools.cache
    def opt(self, i: int, even: bool) -> int:
        # Base case
        if i == self.n:
            return 0
        
        # Find the next index with modulo equal to even
        j = i + 1
        while j < self.n and (self.nums[i] + self.nums[j]) % 2 != even:
            j += 1

        # Count it and continue
        return 1 + self.opt(j, even)

# N.o. states = 2 * n
# Time complexity per state => O(n)
# Total time complexity: O(n^2)