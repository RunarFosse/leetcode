# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # Using sliding window
        n = len(nums)

        powers, consecutives = [], 0
        for i in range(n):
            # Increment consecutive count if elements are consecutive
            if i > 0 and nums[i - 1] == nums[i] - 1:
                consecutives += 1
            else:
                consecutives = 1
            
            # And store power if current consecutive subarray is sized k
            if i >= k - 1:
                powers.append(-1 if consecutives < k else nums[i])

        # Finally, return the powers of all subarrays
        return powers