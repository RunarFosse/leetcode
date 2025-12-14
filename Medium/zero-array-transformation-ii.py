# Author: Runar Fosse
# Time complexity: O(nlog m)
# Space complexity: O(n)

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # Using binary search
        n, m = len(nums), len(queries)

        # Binary search the optimal value for k
        left, right = 0, m + 1
        while left < right:
            pivot = (left + right) // 2

            # Store a prefix sum of all possible decrements of the array
            decrements = [0] * (n + 1)
            for i in range(pivot):
                l, r, val = queries[i]
                decrements[l] += val
                decrements[r + 1] -= val
            
            # Check if we can make array zero
            current, can_zero = 0, True
            for i in range(n):
                current += decrements[i]
                if current < nums[i]:
                    can_zero = False

            # And move bounds correspondingly
            if can_zero:
                right = pivot
            else:
                left = pivot + 1
        
        # If left is larger than m, we cannot zero array
        if left > m:
            return -1

        # Otherwise, return the possible k
        return left
    