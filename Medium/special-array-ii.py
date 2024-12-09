# Author: Runar Fosse
# Time complexity: O(m + n)
# Space complexity: O(m + n)

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # Iterate nums, counting number of non-special
        non_specials = [0]
        for i in range(len(nums) - 1):
            parity_difference = 1 ^ (nums[i] - nums[i + 1]) % 2
            non_specials.append(non_specials[-1] + parity_difference)
        
        # Iterate every query, verifying that
        # non-specials at each end are equal
        return [non_specials[i] == non_specials[j] for i, j in queries]
    