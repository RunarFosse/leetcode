# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        # Iterate the array
        smaller, larger = 0, 0
        for num in nums:
            # Counting elements smaller than and larger than target
            if num < target:
                smaller += 1
            elif num > target:
                larger += 1
        
        # The indices equal to target after sorting are the indices in between
        indices = range(smaller, len(nums) - larger)
        return list(indices)
