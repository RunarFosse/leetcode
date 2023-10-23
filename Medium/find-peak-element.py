# Author: Runar Fosse
# Time complexity: O(log n)
# Space complexity: O(1)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Binary search
        n = len(nums)

        # Use central difference method to calculate gradient,
        # following it to a local peak (Gradient ascent)
        left, right = 0, n - 1
        while left < right:
            pivot = (left + right) // 2
            num = nums[pivot]
            numleft, numright = nums[pivot-1] if pivot > 0 else -1e9, nums[pivot+1] if pivot < n-1 else -1e9

            # Check if this is a peak
            if num > numleft and num > numright:
                return pivot
            
            # Check if we are finished
            # (if left = right -1 and pivot == left)
            if left == right - 1:
                break

            gradient = numright - numleft
            if gradient > 0:
                left = pivot
            elif gradient < 0:
                right = pivot
            else:
                # If we are in a local minimum, pick right route
                left = pivot

        return left if nums[left] > nums[right] else right