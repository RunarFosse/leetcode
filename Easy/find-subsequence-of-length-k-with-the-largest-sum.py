# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Using greedy

        # Sort the array in descending order, grouped with their indices
        values = sorted(((num, i) for i, num in enumerate(nums)), reverse=True)

        # Pick the k-largest values, and sort them by index
        indices = sorted(i for _, i in values[:k])

        # Finally, return the respective indices' numbers
        return [nums[i] for i in indices]