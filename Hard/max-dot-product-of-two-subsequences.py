# Author: Runar Fosse
# Time complexity: O(nm)
# Space complexity: O(nm)

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # Using Dynamic programming
        self.nums1 = nums1
        self.nums2 = nums2
        return self.opt(0, 0)
    
    @functools.cache
    def opt(self, i1: int, i2: int) -> int:
        if i1 == len(self.nums1) or i2 == len(self.nums2):
            return None

        prod = self.nums1[i1] * self.nums2[i2]

        currentmax = -1e9 # Negative infinity
        skip1 = self.opt(i1+1, i2)
        skip2 = self.opt(i1, i2+1)
        skipboth = self.opt(i1+1, i2+1)

        if skip1 != None:
            currentmax = max(currentmax, skip1)
        if skip2 != None:
            currentmax = max(currentmax, skip2)
        if skipboth != None:
            currentmax = max(currentmax, skipboth)
            currentmax = max(currentmax, skipboth + prod)

        return max(currentmax, prod)


# Dynamic programming, each iteration has 5 choices.
# Pick first number from both, pick one skip other, skip one pick other,
# skip both or skip rest.
# 
# opt(i1, i2) = Optimal solution for nums1[i1:] and nums2[i2:]

# Base case:
# opt(len(nums1), i2) = 0
# opt(i1, len(nums2)) = 0

# Recurrency;
# opt(i1, i2) = max(
#    opt(i1+1, i2+1) + nums1[i1] * nums2[i2],   # Pick both
#    opt(i1+1, i2),                             # Skip nums1[i1]
#    opt(i1, i2+1),                             # Skip nums2[i2]
#    opt(i1+1, i2+1),                           # Skip both
#    nums1[i1] * nums2[i2]                      # Skip rest
#)

# Pickboth and skipboth both include opt(i1+1, i2+1), so we
# only need to perform one calculation of opt(i1+1, i2+1).

# N.o. states = O(nm), time per state = O(1)
# giving time complexity of O(nm)