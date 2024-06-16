# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # Using greedy
        patches = 0

        # Patch highest n until it reaches or exceeds n
        highest_n, pointer = 0, 0
        while highest_n < n:
            # Check if we can patch for "free" using nums element
            if pointer < len(nums) and nums[pointer] <= highest_n+1:
                highest_n += nums[pointer]
                pointer += 1
            # If not, patch by "adding" element to nums
            else:
                highest_n += highest_n+1
                patches += 1

        # Return the minimum number of patches
        return patches
    
# Greedily fill in the smallest missing number until we have
# covered every sum in [1, n]. This can easily be done in a while loop,
# keeping track of every "free patch" as the elements in the nums array.