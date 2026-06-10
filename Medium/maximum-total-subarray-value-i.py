# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # Using greedy

        # Find the maximum and the minimum of the array
        maximum, minimum = 0, 1e9
        for num in nums:
            maximum = max(num, maximum)
            minimum = min(num, minimum)

        # Count the subarray containing maximum and minimum, k times
        subarray = maximum - minimum
        return subarray * k
