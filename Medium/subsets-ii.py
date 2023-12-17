# Author: Runar Fosse
# Time complexity: O(n2^n)
# Space complexity: O(n2^n)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Using bitmask
        powerset = set()

        mask = pow(2, n := len(nums))
        while mask:
            mask -= 1
            subset = []
            # Add number to subset if bit is set in bitmask
            for i in range(n):
                if mask >> i & 1:
                    subset.append(nums[i])
            powerset.add(tuple(sorted(subset)))
        
        return list(powerset)

# Note, this problem is badly worded. It is not asking for the power set,
# but rather all different sorted subsets of the input (?)