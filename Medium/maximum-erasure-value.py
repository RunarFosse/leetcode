# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Using sliding window
        n = len(nums)

        # Slide a window over the array
        start, elements = 0, set()
        current, score = 0, 0
        for end in range(n):
            # If we ever have duplicate elements, shrink it
            while nums[end] in elements:
                current -= nums[start]
                elements.remove(nums[start])
                start += 1
            
            # Then add the current element
            current += nums[end]
            elements.add(nums[end])
            
            # And store the maxmium score
            score = max(current, score)
        
        # Finally, return the maximum score
        return score