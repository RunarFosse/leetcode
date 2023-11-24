# Author: Runar Fosse
# Time complexity: O(n2^n)
# Space complexity: O(n2^n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Using exponential time
        n = len(nums)
        mask = pow(2, n) - 1

        subsets = [[]]
        while mask:
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            
            subsets.append(subset)
            mask -= 1

        return subsets