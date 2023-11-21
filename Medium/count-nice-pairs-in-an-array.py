# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    mod = int(1e9)+7
    def countNicePairs(self, nums: List[int]) -> int:
        # Reverse number function
        rev = lambda n : int(str(n)[::-1])

        nice_nums = 0
        diffs = {}
        for num in nums:
            diff = num - rev(num)

            # Check if difference already is in hashmap
            # If it is, add number of nice pairs
            same_diffs = diffs.get(diff)
            if same_diffs:
                nice_nums = (nice_nums + same_diffs) % self.mod
            # If not, add it to hashmap
            else:
                diffs[diff] = 0
            diffs[diff] += 1

        return nice_nums