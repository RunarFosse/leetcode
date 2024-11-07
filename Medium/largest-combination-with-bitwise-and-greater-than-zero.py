# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # Iterate every bit position
        largest_combination = 0
        for i in range(24):
            # Iterate candidates and count how many has this bit set
            hasBitSet = lambda candidate: 1 if candidate >> i & 1 else 0
            count = sum(hasBitSet(candidate) for candidate in candidates)
            largest_combination = max(count, largest_combination)
        
        # Finally return the largest combination
        return largest_combination

        
# As the maximum number in candidates is 10^7, 
# we have that log_2(10^7) = 23.25...
# This means that the largest number is upperbounded by 24 bits.

# For this we can compute the largest combination of candidates for any
# one bit to remain set after AND. Picking the largest one of
# these combinations will give us our wanted result.