# Author: Runar Fosse
# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        # Using set
        n = len(nums)

        # Iterate every subarray
        maximum = 0
        for i in range(n):
            evens, odds = set(), set()
            for j in range(i, n):
                # Store distinct even and odd numbers
                num = nums[j]
                if num % 2:
                    odds.add(num)
                else:
                    evens.add(num)
                
                # If the current subarray is balanced, store maximum subarray size
                if len(evens) == len(odds):
                    maximum = max(j - i + 1, maximum)
        
        # Finally, return this said maximum balances subarray size
        return maximum
