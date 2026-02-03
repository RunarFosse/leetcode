# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)

        # Iterate the array
        decrease, increase = None, None
        for i in range(1, n - 1):
            # If we have any adjacent duplicates, array cannot be trionic
            if nums[i - 1] == nums[i] or nums[i] == nums[i + 1]:
                return False

            # If we have a point of initial decrease
            if nums[i - 1] < nums[i] > nums[i + 1]:
                # Store it, but return False if already set
                if decrease is not None:
                    return False
                decrease = i
            
            # If we have a point of initial increase
            if nums[i - 1] > nums[i] < nums[i + 1]:
                # Store it, but return False if already set
                if increase is not None:
                    return False
                increase = i
        
        # Finally, array is trionic if decrease happens before increase, both being set
        return not (decrease is None or increase is None) and decrease < increase
