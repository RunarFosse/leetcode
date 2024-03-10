# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Using greedy
        # Sort in descending order
        nums.sort(reverse = True)

        # Pair together two-and-two biggest numbers,
        # which is equivalent to adding every second entry of the sorted array together
        return sum(nums[i] for i in range(1, len(nums), 2))
        
# This asks us to maximize the minimum entry of a pair (a_i, b_i).
# The solution to this is obviously pairing together two-and-two biggest numbers.