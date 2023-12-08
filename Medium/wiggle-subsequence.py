# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # Using greedy
        if len(nums) == 1:
            return 1
            
        # Find best with intial positive wiggle or initial negative wiggle
        return max(self.wiggle(nums, True), self.wiggle(nums, False))

    def wiggle(self, nums: List[int], positiveWiggle: bool) -> int:
        wiggleLength = 1
        for i in range(1, len(nums)):
            # Positive wiggle and current is bigger
            if nums[i] > nums[i-1] and positiveWiggle:
                wiggleLength += 1
                positiveWiggle = False
            # Negative wiggle and current is smaller
            if nums[i] < nums[i-1] and not positiveWiggle:
                wiggleLength += 1
                positiveWiggle = True

        return wiggleLength
        
# Greedily iterate array.
# If the next number is bigger than current, continue. (On positive wiggle)
# If the next number is smaller or equal to current, "redo". (On positive wiggle)
# If the next number is smaller than current, continue. (On negative wiggle)
# If the next number is bigger or equal to current, "redo". (On negative wiggle)