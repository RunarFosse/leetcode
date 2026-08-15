# Author: Runar Fosse
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # Using greedy
        n = len(nums)

        # Compute the XOR sum of the array
        xor, zeros = 0, 0
        for num in nums:
            xor ^= num
            if not num:
                zeros += 1
            
        # If there does not exist any non-zero numbers in the array
        if zeros == n:
            # Then there does not exist any subsequence with a non-zero XOR sum
            return 0
        
        # Otherwise, the length of this longest subsequence with a non-zero XOR sum
        return n if xor else (n - 1)


# The bitwise XOR of a sequence is zero if and only if each bit
# cumulatively occurs an even amount of times in the sequence.

# We can greedily find the longest subsequence taking the XOR sum of the whole array.
# If this is non-zero, we have our solution.
# Otherwise, find remove any non-zero number. 
# This is because a number can either have a bit set or non-set.
# If all are non-set, the number is zero.
# If it has at least 1 bit set, then removing it will result in that bit having an
# odd frequency in the cumulative XOR sum over the sequence. I.e. it being non-zero!

# Observation: If there does not exist any non-zero numbers in the array, then
# there is no longest subsequence with a non-zero XOR sum.