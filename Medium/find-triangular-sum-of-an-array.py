# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # Using Pascal's triangle
        n = len(nums)

        # Keep count of Pascal's triangle, split into numerator/denominator for precision
        pascal = [1, 1]

        # Iterate the pairwise elements of the initial row, towards the middle
        triangular = 0
        for i in range(n // 2):
            # Adding to the current triangular sum
            multiplier = pascal[0] // pascal[1] % 10
            triangular = (triangular + nums[i] * multiplier) % 10
            triangular = (triangular + nums[n - i - 1] * multiplier) % 10
            
            # And updating the next entry in Pascal's triangle
            pascal[0] *= n - i - 1
            pascal[1] *= i + 1
        
        # If there is a middle element, compute this alone
        if n % 2 == 1:
            multiplier = pascal[0] // pascal[1] % 10
            triangular = (triangular + nums[n // 2] * multiplier) % 10
        
        # Finally, return the full triangular sum
        return triangular

# It can easily be seen that the triangular sum of the array is equal to the element
# in the initial row multiplied by the corresponding element in Pascal's triangle!
# Thus the result can be solved in linear time and constant space!