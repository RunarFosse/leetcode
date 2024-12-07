# Author: Runar Fosse
# Time complexity: O(nlog m)
# Space complexity: O(1)

# where m is the maximum entry of nums

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Using binary search
        self.nums = nums
        self.maxOperations = maxOperations

        # Binary search minimum possible penalty after operations
        l, r = 1, max(nums)
        while l < r:
            pivot = (l + r) // 2

            if self.canSplit(pivot):
                r = pivot
            else:
                l = pivot + 1

        # Return the minimum possible split
        return l
    
    def canSplit(self, maxBalls: int) -> bool:
        # Iterate every bag of balls
        operations = 0
        for balls in self.nums:
            # Compute number of operations needed to have less than maxBalls
            operations += ceil(balls / maxBalls) - 1

            # If we ever exceed maxOperations, return False
            if operations > self.maxOperations:
                return False
        return True
        


# We have that a bag of balls is comprised of:
# balls <= operations * maxBalls

# Thus we have:
# operations >= balls / maxBalls

# To 'integerize' this count, we have:
# operations >= ceil(balls / maxBalls) - 1