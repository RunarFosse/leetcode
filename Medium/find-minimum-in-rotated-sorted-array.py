# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Using binary search
        n = len(nums)

        # Binary search the largest element in the array
        left, right = 0, n
        while left < right:
            pivot = (left + right) // 2

            # If the element at left is smaller than at pivot
            if nums[left] < nums[pivot]:
                # Then every element left of pivot is smaller
                left = pivot
            else:
                # Otherwise, there is a larger element to the left
                right = pivot
        
        # The smallest element is the one following the largest
        left = (left + 1) % n
        
        # Finally, return this smallest element
        return nums[left]
