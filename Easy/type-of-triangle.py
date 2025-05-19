# Author: Runar Fosse
# Time complexity: O(1)
# Space complexity: O(1)

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # First, extract the side lengths
        s1, s2, s3 = nums

        # The sum of a triangle's two side lengths have to exceed the third
        if s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1:
            return "none"

        # If the sides are equal, the triangle is equilateral
        if s1 == s2 == s3:
            return "equilateral"
        
        # If only two sides are equal, it is an isosceles
        if s1 == s2 or s1 == s3 or s2 == s3:
            return "isosceles"
        
        # Otherwise it is a scalene
        return "scalene"