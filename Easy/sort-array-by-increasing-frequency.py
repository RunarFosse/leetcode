# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count frequency of each number
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1

        # Return numbers sorted in the wanted order
        return sorted(nums, key=lambda num: (frequencies[num], -num))

