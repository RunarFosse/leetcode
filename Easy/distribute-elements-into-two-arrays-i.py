# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # First assign initial values to arrs
        arr1, arr2 = [ nums[0] ], [ nums[1] ]
        # Then iterate, performing valid operations
        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        
        # Return the concatenation of the arrays
        return arr1 + arr2