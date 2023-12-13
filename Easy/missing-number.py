# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = max(nums) + 1
        missing = reduce(xor, nums) ^ reduce(xor, range(n))
        if not missing and any([x == 0 for x in nums]):
            return n
        
        return missing

# XOR sum of nums ^ XOR sum of range [0,n] is equal to the missing number.
# However, if the above calculation is 0, then it indicates that the missing number
# is at the end of the range, i.e. n, if and only if nums contains 0.