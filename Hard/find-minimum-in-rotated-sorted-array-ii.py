# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Using binary search
        n = len(nums)

        # Binary search the minimum element
        left, right = 0, n - 1
        while left < right:
            pivot = (left + right) // 2

            # If the pivot element is smaller than the right
            if nums[pivot] < nums[right]:
                # The minimum element is not in the right partition
                right = pivot
            
            # Otherwise, if the pivot element is larger
            elif nums[pivot] > nums[right]:
                # The minimum element is not in the left partition
                left = pivot + 1
            
            # Finally, there might be duplicates entries
            else:
                # If so, decrement the right pointer
                right -= 1
        
        # Return the minimum element in the array
        return nums[left]
