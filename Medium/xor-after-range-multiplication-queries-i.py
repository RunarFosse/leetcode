# Author: Runar Fosse
# Time complexity: O(mn)
# Space complexity: O(1)

class Solution:
    mod = int(1e9 + 7)
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # Using simulation

        # Iterate the queries
        for l, r, k, v in queries:
            # And apply them
            for i in range(l, r + 1, k):
                nums[i] *= v
                nums[i] %= self.mod
        
        # Finally, return the XOR of the final nums array
        return reduce(lambda r, e: r ^ e, nums)
