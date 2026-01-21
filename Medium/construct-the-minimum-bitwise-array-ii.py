# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # Using bit manipulation
        n = len(nums)

        # Iterate the array
        for i in range(n):
            # We can only find a valid answer number if the number is odd
            if not nums[i] % 2:
                nums[i] = -1
                continue
            
            # In it, flip the last of the initial set bits
            answer, bit = nums[i], 0
            while nums[i] & (1 << bit):
                answer = nums[i] - (1 << bit)
                bit += 1
            nums[i] = answer
    
        # Finally, return the resulting array
        return nums


# 010010111
# 010010011 OR 010010100 = 010010111

# Given a number x, we know that (x + 1) will be identical to x in 
# its bit representation, after the initial contiguously set bits. If we flip the last
# of these initial set bits, we will find the minimal number such that y OR (y + 1) = x,
# where y is x with the last initial bit flipped.