# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # Iterate the array
        sum, minimum = 0, inf
        for num in nums:
            # Storing the minimum element
            minimum = min(num, minimum)

            # And computing the total sum
            sum += num
        
        # The number of operations is equal to sum of differences from minimum
        operations = sum - len(nums) * minimum
        return operations


# Incrementing (n - 1) elements effectively results in decrementing the last
# element by 1, relative to all the others.

# Since uniformally incrementing all elements preserves the difference between
# elements, it doesn't affect our result.

# Therefore, we can use this as our "complement problem" and instead compute the
# number of element decrements needed to make all elements equal.

# This is the same number of operations as by incrementing (n - 1)!