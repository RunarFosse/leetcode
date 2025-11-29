# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # The number of operations is equal to the sum of the array modulo k
        return sum(nums) % k