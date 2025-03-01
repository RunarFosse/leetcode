# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pointer = None
        for i in range(n):
            # Apply the operation
            if i < n - 1 and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            
            # Check if we should set first zero pointer
            if pointer is None:
                if not nums[i]:
                    pointer = i

            # Otherwise, swap with first occuring zero
            elif nums[i]:
                nums[pointer], nums[i] = nums[i], 0
                pointer += 1
        
        # Finally, return the array
        return nums