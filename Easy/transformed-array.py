# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        # Using simulation
        n = len(nums)

        # Construct the resulting array using the set rules
        result = [nums[(nums[i] + i) % n] for i in range(n)]
        return result


# It is obvious that the three rules given is in fact only a single, simple rule.
# Set result[i] to be the value of nums[nums[i] + i], in a circular array (wrapping).