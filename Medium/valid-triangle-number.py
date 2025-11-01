# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Using greedy
        n = len(nums)

        # First, sort the numbers in ascending order
        nums.sort()

        # Then, iterate all number triplets
        triangles = 0
        for i in range(n):
            k = i + 2
            for j in range(i + 1, n):
                # While side k is smaller than the sum of the two others
                while k < n and nums[i] + nums[j] > nums[k]:
                    # Increment it
                    k += 1
                
                # And count all current valid triangle numbers
                triangles += max((k - 1) - j, 0)
        
        # Finally, return the number of valid triangle numbers
        return triangles

# The sides of a triangle are valid if side1 + side2 > side3.
# This makes the problem trivial to solve.