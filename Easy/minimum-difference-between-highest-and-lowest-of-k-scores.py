# Author: Runar Fosse
# Time complexity: O(nlog n)
# Space complexity: O(n)

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Using sliding window
        n = len(nums)

        # First, sort the scores in ascending order
        nums.sort()

        # Then, iterate the array
        minimum = 1e9
        for i in range(n - k + 1):
            # Find the maximum difference of scores in a k sized window
            difference = nums[i + k - 1] - nums[i]

            # And store the minimum difference in the whole array
            minimum = min(difference, minimum)
        
        # Finally, return this minimum score difference
        return minimum
