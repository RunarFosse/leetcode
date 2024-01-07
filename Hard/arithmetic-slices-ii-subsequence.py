# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n^2)

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Using dynamic programming
        n = len(nums)

        arithmetic_slices = 0
        opt = [defaultdict(lambda : 0) for _ in range(n)]
        # Count arithmetic slices ending in index i
        for i in range(n):
            # For every 2nd last entry j
            for j in range(i):
                # Count the diff
                diff = nums[i] - nums[j]
                opt[i][diff] += 1

                # And if j is the last entry of an arithmetic slice with the
                # same difference, then we can add ALL j_slices as possible
                # slices ending at index i.
                # This also means that we have a slice of at least size 3, thus
                # add to total number of arithmetic slices.
                j_slices = opt[j].get(diff)
                if j_slices:
                    opt[i][diff] += j_slices
                    arithmetic_slices += j_slices
        
        # Return the total number of arithmetic slices
        return arithmetic_slices

# opt(i, j) - The size of an arithmetic sequence where nums[i] is the last entry 
#             of an arithmetic slice with the difference between each entry is j.

# How to calculate total number of arithmetic slices within a single "largest"
# arithmetic subsequence is explained in this solution: 
# https://leetcode.com/problems/arithmetic-slices/

# We can solve this from a bottom-up approach, as we need to count the number
# of valid arithmetic subsequences, and not the lengths.

# There are n^2 states, where each state has a runtime of O(1).