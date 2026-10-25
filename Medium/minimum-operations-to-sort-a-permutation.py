# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # First, check if the array can be sorted
        minimum = n - 1
        for i in range(n - 1):
            if nums[i] == 0:
                minimum = i

            # If the we have a difference not between adjacents, or minimum and maximum
            difference = abs(nums[i] - nums[i + 1])
            if difference not in [1, n - 1]:
                # Then the array cannot be sorted through rotations and reversals
                return -1
        
        # If the array already is sorted, there is no need to perform any operations
        if nums[0] == 0 and nums[-1] == n - 1:
            return 0
        
        # Check if the array is circularly ascending
        ascending = (nums[0] + 1) % n == nums[1]

        # If so, rotate minimum to index 0 either left, or right
        if ascending:
            return min(minimum, n - minimum + 2)
        
        # If not, rotate minimum to index n - 1 either left or right, and reverse
        return min(minimum + 2, n - minimum)


# Rotating preserves the circular ordering of elements, while reversing the array
# only changes the direction of this circular ordering.

# Therefore, the array can only be sorted if it is circularly ascending or circularly
# descending. This can be verified by checking if adjacent elements differ by 1,
# except for the break between the minimum and maximum element.

# The minimum number of operations to sort a circularly ascending array is by moving
# the minimum element to index 0. Either by leftward rotations, or by rightward rotations
# which can be made through a reversal + leftward rotations + another reversal.

# On a circularly descending array we need to have at least 1 reversal to sort the array
# in ascending order. This can either be done then moving the minimum element to
# index n - 1 using leftward rotations, followed by the reversal. Or through an immediate
# reversal followed by leftward rotations to get the minimum element to index 0!