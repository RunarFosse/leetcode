# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Using monotonic stack
        
        # Iterate the array
        operations, stack = 0, []
        for num in nums:
            # Keeping a decreasing, monotonic stack
            while stack and stack[-1] > num:
                stack.pop()
            
            # Skip if we reach a zero
            if not num:
                continue
            
            # Otherwise, if not the current smallest element in the stack
            if not stack or stack[-1] < num:
                # Add it to the stack and count as an operation
                stack.append(num)
                operations += 1
            
        # Finally, return the minimum number of operations to zero out the array
        return operations
