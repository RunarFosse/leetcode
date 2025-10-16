# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(m)

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # Count frequency of numbers modulo value
        frequencies = [0] * value
        for num in nums:
            frequencies[num % value] += 1
        
        # Then, count up until we find the MEX
        mex = 0
        while frequencies[mex % value]:
            frequencies[mex % value] -= 1
            mex += 1

        # And return it
        return mex