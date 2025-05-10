# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(1)

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Using greedy
        
        # First compute the sum of both arrays, and count their respective zeros
        sum1, sum2 = 0, 0
        zeros1, zeros2 = 0, 0
        for num in nums1:
            if not num:
                zeros1 += 1
            sum1 += num
        for num in nums2:
            if not num:
                zeros2 += 1
            sum2 += num
        
        # Then, greedily make all zeros to ones
        sum1 += zeros1
        sum2 += zeros2

        # If the lesser one of these have no zeros, we cannot make them equal
        if sum1 < sum2 and not zeros1 or sum2 < sum1 and not zeros2:
            return -1

        # Otherwise return the maximum
        return max(sum1, sum2)
