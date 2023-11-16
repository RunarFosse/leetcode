# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        bitstring = ""
        complement = lambda b : "0" if b == "1" else "1"
        for i in range(len(nums)):
            bitstring += complement(nums[i][i])

        return bitstring

# Add complement of i'th bit in the i'th bitstring to our final bitstring
# will generate a unique bitstring following Cantor's diagonal argument.