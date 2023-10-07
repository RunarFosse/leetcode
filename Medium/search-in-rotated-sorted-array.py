# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Using Binary search

        left,right = 0, len(nums) - 1
        pivot = (left+right)//2

        while abs(left-right) > 1:
            if nums[pivot] == target:
                return pivot
                
            if nums[pivot] < target: # If pivot is less
                if nums[left] == target:
                    return left

                if nums[left] < target: # if left pointer is less
                    if nums[left] < nums[pivot]: # if left is less than pivot
                        left = pivot # then target is between pivot and right
                    else:
                        right = pivot # else target is between left and pivot
                else:
                    left = pivot # else target is between pivot and right
            
            if nums[pivot] > target: # Analogous arguments here
                if nums[left] == target:
                    return left

                if nums[left] < target:
                    right = pivot
                else:
                    if nums[left] < nums[pivot]:
                        left = pivot
                    else:
                        right = pivot

            pivot = (left+right)//2
                
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1