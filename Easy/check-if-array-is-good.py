# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # Iterate the array, counting frequency of elements and storing maximum
        frequencies, maximum = defaultdict(int), 0
        for num in nums:
            frequencies[num] += 1
            maximum = max(num, maximum)
        
        # Then, the array is good if the maximum element has exactly two entries
        good = frequencies.pop(maximum) == 2

        # And if all other elements on [1, maximum) occurs exactly once
        good = good and len(frequencies) == (maximum - 1) and len(nums) == (maximum + 1)

        # Finally, return if the array is good
        return good
