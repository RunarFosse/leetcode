# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Using two-pointer approach
        n = len(nums)
        result = [0] * n

        # Add the square of the largest number to the current end of list
        p1, p2 = 0, n-1
        insertion = n-1
        while p1 <= p2:
            if abs(nums[p1]) > abs(nums[p2]):
                result[insertion] = pow(nums[p1], 2)
                p1 += 1
            else:
                result[insertion] = pow(nums[p2], 2)
                p2 -= 1
            insertion -= 1
        
        return result