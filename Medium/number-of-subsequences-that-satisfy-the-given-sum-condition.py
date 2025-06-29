# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    mod = int(1e9 + 7)
    def numSubseq(self, nums: List[int], target: int) -> int:
        # Using two-pointer
        n = len(nums)

        # First, sort the array in ascending order, storing each original index
        nums.sort()

        # Then, iterate all subsequence bounds
        subsequences = 0
        minimum, maximum = 0, n - 1
        while minimum <= maximum:
            # If maximum is too large, move it
            while minimum <= maximum and nums[minimum] + nums[maximum] > target:
                maximum -= 1

            # Then count all possible subsequences
            elements = maximum - minimum
            subsequences = (subsequences + self.subsequences(elements)) % self.mod

            # And move minimum pointer
            minimum += 1
        
        # Finally, return all valid subsequences
        return subsequences
    
    @functools.cache
    def subsequences(self, i: int) -> int:
        if i <= 0:
            return 1 if i == 0 else 0
        return 2 * self.subsequences(i - 1) % self.mod