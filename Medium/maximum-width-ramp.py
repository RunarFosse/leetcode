# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # Using monotonic stack
        n = len(nums)

        # First, populate the stack with increasing elements
        stack = []
        for i in range(n):
            if stack and nums[stack[-1]] <= nums[i]:
                continue
            stack.append(i)
        
        # Then, iterate the list from the end and store the maximum width ramp
        max_width = 0
        for i in reversed(range(n)):
            while stack and nums[stack[-1]] <= nums[i]:
                max_width = max(i - stack.pop(), max_width)
            
        # Finally, return the maximum width ramp
        return max_width
