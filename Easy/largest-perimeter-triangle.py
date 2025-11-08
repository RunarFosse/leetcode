# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Using greedy
        n = len(nums)

        # Sort the sides in descending order
        nums.sort(reverse=True)

        # Then iterate every triple of sides
        for i in range(n - 2):
            side3, side2, side1 = nums[i:i+3]
            # If they make a valid triangle
            if side1 + side2 > side3:
                # Return their perimeter
                return side1 + side2 + side3

        # If we have no valid triangle, return zero
        return 0

# The sides of a triangle are valid if side1 + side2 > side3.
# This makes the problem trivial to solve.