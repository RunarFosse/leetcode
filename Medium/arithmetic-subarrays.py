# Author: Runar Fosse
# Time complexity: O(n*m)
# Space complexity: O(n)

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # Using brute force
        self.nums = nums

        arithmetics = []
        for left, right in zip(l, r):
            arithmetics.append(self.isArithmetic(left, right))
        
        return arithmetics

    @functools.cache
    def isArithmetic(self, left: int, right: int) -> bool:
        # Iterate subarray, storing min and max
        # Also add each num to subarray set
        minnum, maxnum = 1e9, -1e9
        subarray = set()
        for i in range(left, right+1):
            num = self.nums[i]
            subarray.add(num)
            minnum = min(num, minnum)
            maxnum = max(num, maxnum)
        
        # Calculate difference per element, if this is not an integer, the subarray
        # cannot be arithmetic
        length = right - left
        difference = (maxnum - minnum) / length
        if difference != int(difference):
            return False

        # Iteratively check if all numbers from min+difference to max are in the subarray
        current = minnum
        for _ in range(length):
            current += difference
            if current not in subarray:
                return False
        
        return True