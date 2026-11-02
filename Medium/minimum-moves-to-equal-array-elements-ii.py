# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # Using greedy
        n = len(nums)

        # Compute the median element of the array
        median = sorted(nums)[n // 2]

        # Then, make every element equal to the median
        moves = sum(abs(median - num) for num in nums)

        # This is the minimum number of moves to make all array elements equal
        return moves
